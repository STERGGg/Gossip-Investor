"""
MODEL 03  How much of the French spread is politics?

Idea: estimate how euro area bond markets price fiscal fundamentals in a calm
period, then ask what spread France "should" pay given its own debt and deficit.
Whatever is left over is a premium that fundamentals do not explain; I call it
the political and social premium.

Data
    Spreads: ECB 10 year convergence yields, annual averages, minus Germany (bp)
    Fundamentals: IMF WEO gross debt and overall balance, % of GDP
    Countries: France, Italy, Spain, Greece, Belgium, Portugal, Austria,
               Netherlands, Ireland, Finland (Germany is the benchmark)

Regression (ordinary least squares, estimated 2017 to 2023)
    spread(i,t) = country effect(i) + b1 x debt(i,t) + b2 x balance(i,t) + year effect(t) + error
Country effects capture each country's normal premium (liquidity, history, the
"core" status France used to enjoy). Year effects soak up anything that moved
every country together (Covid, the ECB hiking cycle). Greece is left out of the
estimation because until 2023 it was below investment grade and priced on its
programme exit, not on normal fundamentals.
For 2024 to 2026 the year effect is measured from the other eight countries
only, so France cannot contaminate its own benchmark. France's residual in
2024, 2025 and 2026 is the premium that neither its numbers nor its own normal
standing explain.
"""
from common import *

style()
w = weo(); sp = spreads_bp(); h = hand()
countries = ["FRA", "ITA", "ESP", "GRC", "BEL", "PRT", "AUT", "NLD", "IRL", "FIN"]
ann = sp.groupby(sp.index.year).mean()
ann.loc[2026] = sp.loc["2026-01":"2026-09"].mean()  # 2026 to date

rows = []
for c in countries:
    for yr in range(2017, 2027):
        rows.append({"c": c, "yr": yr, "spread": ann.loc[yr, c],
                     "debt": w["GGXWDG_NGDP"].loc[yr, c], "bal": w["GGXCNL_NGDP"].loc[yr, c]})
panel = pd.DataFrame(rows)
train = panel[(panel.yr <= 2023) & (panel.c != "GRC")].dropna()

years = sorted(train.yr.unique())
cs = sorted(train.c.unique())
X = np.column_stack([train.debt, train.bal] + [(train.yr == t).astype(float) for t in years[1:]]
                    + [(train.c == c).astype(float) for c in cs])
beta, *_ = np.linalg.lstsq(X, train.spread.values, rcond=None)
b_debt, b_bal = beta[:2]
fitted = X @ beta
resid = train.spread.values - fitted
r2 = 1 - (resid ** 2).sum() / ((train.spread - train.spread.mean()) ** 2).sum()
# classical standard errors
sigma2 = (resid ** 2).sum() / (len(train) - X.shape[1])
se = np.sqrt(np.diag(sigma2 * np.linalg.inv(X.T @ X)))[:2]

ceff = dict(zip(cs, beta[2 + len(years) - 1:]))
out = []
for yr in range(2017, 2027):
    g = panel[(panel.yr == yr) & (panel.c != "GRC")].set_index("c")
    core = g.debt * b_debt + g.bal * b_bal + pd.Series(ceff)
    others = g.drop(index="FRA")
    year_eff = (others.spread - core.drop(index="FRA")).mean()
    for c in ["FRA", "ITA", "ESP", "BEL"]:
        pred = core[c] + year_eff
        out.append({"year": yr, "country": c, "actual_bp": g.loc[c, "spread"], "fundamentals_bp": pred,
                    "unexplained_bp": g.loc[c, "spread"] - pred})
res = pd.DataFrame(out)
save_table(res.round(1).set_index(["country", "year"]), "m03_spread_decomposition")

fr = res[res.country == "FRA"].set_index("year")
# The September 2026 month and October peak against 2026 fundamentals
fr26_fund = fr.loc[2026, "fundamentals_bp"]
sep26 = sp.loc["2026-09", "FRA"].iloc[0]

# Chart
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(fr.index - 0.2, fr.fundamentals_bp, width=0.4, color="#b9d2f0", label="Explained by debt and deficit")
ax.bar(fr.index + 0.2, fr.actual_bp, width=0.4, color=BLUE, label="Actual spread over Bunds")
for yr in fr.index:
    u = fr.loc[yr, "unexplained_bp"]
    if yr >= 2024:
        ax.text(yr + 0.2, fr.loc[yr, "actual_bp"] + 2, f"+{u:.0f}", ha="center", fontsize=8.5, color=INK)
ax.set_ylabel("basis points"); ax.set_xticks(fr.index)
ax.set_title("Figure 7: Since 2024 France pays more than its numbers justify")
ax.legend(loc="upper left")
source_note(fig, "Author's model 03: ECB 10y yields, IMF WEO; 9 country panel fitted 2017 to 2023; 2026 = Jan to Sep.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig05_spread_premium.png"); plt.close(fig)

with open(TABLES / "m03_summary.txt", "w") as fh:
    fh.write(f"Country effects (bp): " + str({k: round(v,1) for k,v in ceff.items()}) + "\n")
    fh.write(f"Observations {len(train)}, R squared {r2:.3f}\n")
    fh.write(f"b_debt {b_debt:.3f} bp per pp of debt (se {se[0]:.3f}); b_balance {b_bal:.3f} bp per pp of balance (se {se[1]:.3f})\n")
    fh.write(res[res.year >= 2022].round(1).to_string() + "\n")
    fh.write(f"\nSeptember 2026 spread {sep26:.1f}bp vs 2026 fundamentals {fr26_fund:.1f}bp -> unexplained {sep26-fr26_fund:.1f}bp\n")
    fh.write(f"October 2026 peak {h['spread_peak_oct2026']}bp -> unexplained {h['spread_peak_oct2026']-fr26_fund:.1f}bp\n")
print(open(TABLES / "m03_summary.txt").read())

# ---------- Appendix figure A3: model fit ----------
fig, ax = plt.subplots(figsize=(7.5, 5))
lim = (0, max(res.actual_bp.max(), res.fundamentals_bp.max()) * 1.08)
ax.plot(lim, lim, color=GREY, lw=1, ls="--")
cmap = {"FRA": BLUE, "ITA": VIOLET, "ESP": AQUA, "BEL": YELLOW}
for c, g in res.groupby("country"):
    pre = g[g.year <= 2023]; post = g[g.year >= 2024]
    ax.scatter(pre.fundamentals_bp, pre.actual_bp, color=cmap[c], s=26, alpha=0.55, label=f"{NAMES[c]} 2017 to 2023")
    ax.scatter(post.fundamentals_bp, post.actual_bp, color=cmap[c], s=70, marker="D" if c == "FRA" else "o",
               edgecolor=INK if c == "FRA" else "none", label=f"{NAMES[c]} 2024 to 2026")
for _, r_ in res[(res.country == "FRA") & (res.year >= 2024)].iterrows():
    off = {2024: (8, -10), 2025: (8, 6), 2026: (-30, 6)}[int(r_.year)]
    ax.annotate(str(int(r_.year)), (r_.fundamentals_bp, r_.actual_bp), xytext=off, textcoords="offset points", fontsize=8)
ax.set_xlim(lim); ax.set_ylim(lim)
ax.set_xlabel("Spread explained by debt, deficit and normal standing (bp)"); ax.set_ylabel("Actual spread over Bunds (bp)")
ax.text(lim[1] * 0.55, lim[1] * 0.08, "below the line: cheaper than\nfundamentals (Italy now)", fontsize=8, color=INK2)
ax.text(lim[1] * 0.05, lim[1] * 0.85, "above the line: dearer than\nfundamentals (France now)", fontsize=8, color=INK2)
ax.legend(fontsize=7, loc="center right", ncol=1)
ax.set_title(f"Figure 6: Model 03, actual against fitted spreads (R squared {r2:.2f})")
source_note(fig, "Author's model 03: ECB yields, IMF WEO; country and year effects, fitted 2017 to 2023.")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(CHARTS / "figA3_model03_fit.png"); plt.close(fig)
