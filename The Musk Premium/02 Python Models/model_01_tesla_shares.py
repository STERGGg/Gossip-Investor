"""
MODEL 01  What has happened to Tesla's shares, and why?
1. Nasdaq daily closes for Tesla since January 2024, with the record close, the change in
   2026 so far, and the moves around the Roadster reveal (evening of 15 October 2026).
2. Tesla's quarterly operating income, net income, operating cash flow and capex for the
   four quarters to June 2026, from Nasdaq cash flow and income statements via OpenBB.
3. Annual net income 2022 to 2025, to show the trend in profits behind the share price.
"""
from common import *

style()
px = prices()["TSLA"].dropna()
fin = pd.read_csv(DATA / "tesla_financials.csv")
q = fin[fin.period == "quarter"].set_index("period_ending")
a = fin[fin.period == "annual"].set_index("period_ending")
rec = px.max(); rec_d = px.idxmax()
ytd = (px.iloc[-1] / px.loc[:"2025-12-31"].iloc[-1] - 1) * 100
moves = px.pct_change().mul(100).loc["2026-10-14":]
res = pd.Series({"record_close": rec, "record_date": str(rec_d.date()), "last_close": px.iloc[-1],
                 "from_record_pct": (px.iloc[-1] / rec - 1) * 100, "ytd_2026_pct": ytd,
                 "ttm_net_income_bn": q.net_income_bn.sum(), "ttm_revenue_bn": q.revenue_bn.sum(),
                 "q2_2026_free_cash_flow_bn": q.operating_cash_flow_bn.iloc[-1] - q.capex_bn.iloc[-1]})
save_table(res.to_frame("value"), "m01_tesla_summary"); save_table(moves.round(2).to_frame("daily_change_pct"), "m01_roadster_week")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.35, 1]})
ax = axes[0]
s = px.loc["2024-01-01":]
ax.plot(s.index, s.values, color=BLUE, lw=1.6)
for d, lab, dx, dy in (("2025-11-06", "Pay package\napproved", -95, 35), ("2025-12-16", "Record close\n$489.88", 70, 15),
                   ("2026-06-12", "SpaceX IPO", -40, -110), ("2026-10-16", "Roadster\nreveal", 0, -110)):
    y = s.loc[:d].iloc[-1]
    ax.annotate(lab, (pd.Timestamp(d), y), (pd.Timestamp(d) + pd.Timedelta(days=dx), y + dy), fontsize=7.5, ha="center", color=INK2,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_ylabel("Share price, USD"); ax.set_title("Tesla's shares since 2024", fontsize=11); ax.set_ylim(100, 560)
import matplotlib.dates as mdates; ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")); ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7])); ax.tick_params(axis="x", labelsize=8)
ax = axes[1]
lab = ["Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]; x = np.arange(4)
ax.bar(x - 0.2, q.operating_income_bn, 0.4, color=BLUE, label="Operating profit")
ax.bar(x + 0.2, q.operating_cash_flow_bn - q.capex_bn, 0.4, color=[GREEN if v > 0 else RED for v in q.operating_cash_flow_bn - q.capex_bn], label="Free cash flow")
for i, (o, f) in enumerate(zip(q.operating_income_bn, q.operating_cash_flow_bn - q.capex_bn)):
    ax.text(i - 0.2, o + 0.08, f"{o:.1f}", ha="center", fontsize=8); ax.text(i + 0.2, max(f, 0) + 0.08, f"{f:.1f}", ha="center", fontsize=8)
ax.axhline(0, color=INK2, lw=0.8); ax.set_xticks(x); ax.set_xticklabels(lab, fontsize=8.5)
ax.set_ylabel("USD bn"); ax.grid(axis="x", visible=False); ax.legend(fontsize=8, loc="upper right")
ax.set_title("Profits are shrinking", fontsize=11)
finish(fig, "Figure 1: Tesla's shares have fallen with its profits, not because of the Roadster",
       "author's model 01; Nasdaq prices and Tesla income and cash flow statements via OpenBB (to 19 Oct 2026).", "fig01_tesla_shares.png")
print(res); print(moves.round(2)); print(a[["revenue_bn", "net_income_bn"]])
