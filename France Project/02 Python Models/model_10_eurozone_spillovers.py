"""
MODEL 10  France and the euro area: size and spillovers

1. Weight: France's share of euro area GDP and of euro area public debt in 2025
       debt in USD = debt % GDP x GDP in USD   (IMF WEO, all 21 members)
2. Spillovers: does the French spread now drag other countries' spreads with it?
   For each country the monthly change in its spread over Bunds is regressed on
   the monthly change in the French spread, in two windows:
       calm window:   January 2015 to May 2024
       French crisis: June 2024 (dissolution) to September 2026
       d spread(i,t) = a + beta x d spread(France,t) + e
   A higher beta in the second window means a basis point of French stress now
   carries more of itself into that country than it used to. ECB monthly data.
3. Stress transmission in basis points: beta multiplied by the rise in the French
   spread from its pre dissolution average to the October 2026 peak.
"""
from common import *

style()
w = weo(); sp = spreads_bp(); h = hand()
ea = pd.read_csv(DATA / "imf_weo_euro_area_2025.csv").set_index("iso3")
debt = w["GGXWDG_NGDP"].loc[2025]
ea["debt_pct"] = ea.debt_pct_gdp_2025.fillna(debt.reindex(ea.index))
ea["debt_usd_bn"] = ea.debt_pct / 100 * ea.ngdpd_2025_usd_bn
share = pd.DataFrame({"gdp_share_pct": ea.ngdpd_2025_usd_bn / ea.ngdpd_2025_usd_bn.sum() * 100,
                      "debt_share_pct": ea.debt_usd_bn / ea.debt_usd_bn.sum() * 100}).sort_values("gdp_share_pct", ascending=False)
save_table(share.round(1), "m10_euro_area_shares")

d = sp.diff().dropna(how="all")
windows = {"calm 2015 to May 2024": ("2015-01", "2024-05"), "crisis Jun 2024 to Sep 2026": ("2024-06", "2026-09")}
rows = []
for c in ["ITA", "ESP", "BEL", "PRT", "GRC", "AUT", "FIN", "NLD", "IRL"]:
    row = {"country": NAMES[c]}
    for wname, (a, b) in windows.items():
        x = d.loc[a:b, "FRA"]; y_ = d.loc[a:b, c]
        m = x.notna() & y_.notna()
        X = np.column_stack([np.ones(m.sum()), x[m]])
        beta = np.linalg.lstsq(X, y_[m].values, rcond=None)[0][1]
        row[f"beta {wname}"] = beta
        row[f"corr {wname}"] = np.corrcoef(x[m], y_[m])[0, 1]
    rows.append(row)
spill = save_table(pd.DataFrame(rows).set_index("country").round(2), "m10_spillover_betas")
rise = h["spread_peak_oct2026"] - sp["FRA"].loc["2024-01":"2024-05"].mean()
spill["implied_bp_from_French_rise"] = spill["beta crisis Jun 2024 to Sep 2026"] * rise
save_table(spill.round(2), "m10_spillover_betas")

# Chart
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": [1, 1.5]})
ax = axes[0]
top = share.head(6)
ax.barh(range(len(top))[::-1], top.gdp_share_pct, height=0.38, color=[BLUE if i == "FRA" else GREY for i in top.index], label="Share of euro area GDP")
ax.barh([i - 0.4 for i in range(len(top))[::-1]], top.debt_share_pct, height=0.38,
        color=["#8db7ea" if i == "FRA" else "#cfccc5" for i in top.index], label="Share of euro area public debt")
ax.set_yticks([i - 0.2 for i in range(len(top))[::-1]]); ax.set_yticklabels([NAMES.get(i, i) for i in top.index])
for i, (g, dd) in enumerate(zip(top.gdp_share_pct, top.debt_share_pct)):
    yy = len(top) - 1 - i
    ax.text(g + 0.5, yy, f"{g:.0f}%", va="center", fontsize=8); ax.text(dd + 0.5, yy - 0.4, f"{dd:.0f}%", va="center", fontsize=8)
ax.set_xlabel("% of euro area, 2025"); ax.legend(fontsize=7.5, loc="lower right"); ax.grid(axis="y", visible=False)
ax.set_title("Weight in the euro area", fontsize=10.5)
ax = axes[1]
order = spill.sort_values("beta crisis Jun 2024 to Sep 2026", ascending=False)
xpos = np.arange(len(order))
ax.bar(xpos - 0.2, order["beta calm 2015 to May 2024"], width=0.4, color=GREY, label="2015 to May 2024: France followed others' crises")
ax.bar(xpos + 0.2, order["beta crisis Jun 2024 to Sep 2026"], width=0.4, color=RED, label="Jun 2024 to Sep 2026: crises start in France")
ax.set_xticks(xpos); ax.set_xticklabels(order.index, rotation=35, ha="right", fontsize=8.5)
ax.set_ylabel("bp move per 1bp move in France"); ax.legend(fontsize=8)
ax.set_title("Basis points other spreads move per 1bp French move", fontsize=10.5)
fig.suptitle("Figure 23: France's weight in the euro area and the spillover of its stress", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 10: IMF WEO 2025 (USD), ECB monthly 10y yields; OLS of monthly spread changes on the French spread change.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "fig15_eurozone_spillovers.png"); plt.close(fig)

with open(TABLES / "m10_summary.txt", "w") as fh:
    fh.write(share.round(1).to_string() + "\n\n" + spill.round(2).to_string() + f"\n\nRise in French spread used: {rise:.1f}bp\n")
print(open(TABLES / "m10_summary.txt").read())
