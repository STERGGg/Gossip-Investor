"""
MODEL 06  How French listed companies have traded through the crisis

Data: daily closes of the iShares MSCI country ETFs listed in New York
(EWQ France, EWG Germany, EWI Italy, EWP Spain, EZU euro area), via Nasdaq.
All are priced in dollars, so the euro/dollar rate cancels out when France is
compared with another euro country. Prices exclude dividends, which slightly
understates all of them by similar amounts.

1. Relative performance: France against a peer basket (equal weight Germany,
   Italy, Spain), rebased to 100 on 7 June 2024, the last close before the
   dissolution of the National Assembly.
2. Event study (market model). For each political event:
      estimate  r_FR = a + b x r_peers  on the 250 trading days before the window
      abnormal return each day = r_FR - (a + b x r_peers)
      cumulative abnormal return (CAR) = sum over the event window
   A negative CAR means French stocks fell more than their normal relationship
   with European peers would predict.
"""
from common import *

style()
px = pd.read_csv(DATA / "etf_daily_close.csv", index_col=0, parse_dates=True).dropna()
ret = np.log(px).diff().dropna()
ret["PEERS"] = ret[["EWG", "EWI", "EWP"]].mean(axis=1)

events = [
    ("Dissolution of the Assembly", "2024-06-07", "2024-06-14"),
    ("Barnier government censured", "2024-11-29", "2024-12-06"),
    ("Bayrou calls confidence vote", "2025-08-22", "2025-08-29"),
    ("Bayrou loses vote, Fitch downgrade", "2025-09-05", "2025-09-12"),
    ("Lecornu resigns then returns", "2025-10-03", "2025-10-10"),
    ("Lycee riots and 2027 budget", "2026-09-17", "2026-10-16"),
]
rows = []
for name, start, end in events:
    est = ret.loc[:start].iloc[-251:-1]
    X = np.column_stack([np.ones(len(est)), est.PEERS])
    a, b = np.linalg.lstsq(X, est.EWQ.values, rcond=None)[0]
    resid_sd = np.std(est.EWQ - (a + b * est.PEERS), ddof=2)
    win = ret.loc[start:end].iloc[1:]
    ab = win.EWQ - (a + b * win.PEERS)
    car = ab.sum()
    t = car / (resid_sd * np.sqrt(len(win)))
    rows.append({"event": name, "window": f"{start} to {end}", "days": len(win), "beta": b,
                 "france_return_pct": (np.exp(win.EWQ.sum()) - 1) * 100,
                 "peers_return_pct": (np.exp(win.PEERS.sum()) - 1) * 100,
                 "CAR_pct": car * 100, "t_stat": t})
ev = save_table(pd.DataFrame(rows).set_index("event").round(2), "m06_event_study")

# Relative performance since dissolution
base = "2024-06-07"
lvl = px / px.loc[base]
peers_lvl = np.exp(ret[["EWG", "EWI", "EWP"]].loc[base:].iloc[1:].cumsum().mean(axis=1))
rel = (lvl.loc[base:, "EWQ"].iloc[1:] / peers_lvl) * 100
end = px.index[-1]
perf = pd.DataFrame({
    "since_dissolution_pct": (px.loc[end] / px.loc[base] - 1) * 100,
    "2026_ytd_pct": (px.loc[end] / px.loc[:"2025-12-31"].iloc[-1] - 1) * 100,
    "from_2026_aug_high_pct": (px.loc[end] / px.loc["2026-08"].max() - 1) * 100,
})
save_table(perf.round(1), "m06_performance")
# Pre dissolution relative trend for comparison (Oct 2016 to Jun 2024)
pre = (px.loc[base] / px.iloc[0] - 1) * 100

fig, ax = plt.subplots(figsize=(8.5, 4))
ax.plot(rel.index, rel.values, color=BLUE)
ax.axhline(100, color=GREY, lw=1)
for name, start, endd in events:
    d = pd.Timestamp(endd)
    v = rel.loc[:d].iloc[-1]
    ax.scatter([d], [v], color=RED, s=22, zorder=3)
ax.set_ylabel("France vs DE/IT/ES basket, 7 Jun 2024 = 100")
ax.set_title("Figure 14: French equities have lagged since the dissolution")
ax.text(rel.index[-1], rel.iloc[-1], f"  {rel.iloc[-1]:.0f}", color=BLUE, va="center", fontsize=9)
source_note(fig, "Author's model 06: Nasdaq daily closes of iShares MSCI ETFs (EWQ, EWG, EWI, EWP). Red dots mark political events.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig09_equities_relative.png"); plt.close(fig)

with open(TABLES / "m06_summary.txt", "w") as fh:
    fh.write(ev.round(2).to_string() + "\n\n" + perf.round(1).to_string() + "\n\n")
    fh.write(f"Relative index France vs peers on {end.date()}: {rel.iloc[-1]:.1f}\n")
    fh.write("Oct 2016 to Jun 2024 price change: " + pre.round(1).to_string() + "\n")
print(open(TABLES / "m06_summary.txt").read())

# ---------- Appendix figure A6: event study ----------
fig, ax = plt.subplots(figsize=(8.5, 4))
e = ev.iloc[::-1]
se = (e.CAR_pct / e.t_stat).abs()
colors = [RED if abs(t) > 1.96 else GREY for t in e.t_stat]
ax.barh(range(len(e)), e.CAR_pct, color=colors, height=0.55, xerr=1.96 * se, error_kw={"ecolor": INK2, "capsize": 3, "lw": 1})
ax.set_yticks(range(len(e))); ax.set_yticklabels(e.index, fontsize=8.5)
ax.axvline(0, color=INK2, lw=0.8)
for i, (v, t) in enumerate(zip(e.CAR_pct, e.t_stat)):
    ax.text(v + (0.25 if v >= 0 else -0.25), i + 0.3, f"{v:+.1f}% (t {t:.1f})", fontsize=8, ha="left" if v >= 0 else "right")
ax.set_xlabel("Cumulative abnormal return of French equities vs DE/IT/ES, %")
ax.set_title("Figure 13: Model 06, only the dissolution moved French shares")
source_note(fig, "Author's model 06: market model on 250 prior days; bars show 95% intervals; red = significant at 5%.")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(CHARTS / "figA6_model06_event_study.png"); plt.close(fig)
