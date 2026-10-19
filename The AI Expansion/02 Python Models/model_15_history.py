"""
MODEL 15  How big is the boom compared with history, and how much does it add to growth?
1. Building booms as a share of US GDP, from published estimates collected by Justin Fox
   (Bloomberg): railroads at their late 1800s peak (Kedrosky) and on average in the 1870s and
   1880s (Ulmer), telecom at its 2000 peak (Kedrosky), all information processing equipment
   and software in Q4 2000 (BEA), and AI data centre capex in 2023 to 2025 (Exante Data).
2. The four hyperscalers' 2026 capex guidance (Model 02) divided by the IMF's estimate of US
   nominal GDP in 2026. This overstates the US share, because some of the spending is abroad,
   and includes some non AI spending, so it is an upper bound.
3. Contribution to growth: US real GDP grew 2.1% in the year to Q2 2026. Flossbach von Storch
   estimate that AI related investment added 0.45 to 0.94 percentage points before imports,
   but only 0.14 to 0.38 points once the imported hardware is subtracted.
"""
from common import *

style(); h = hand()
gdp = pd.read_csv(DATA / "imf_weo_us_gdp.csv", index_col=0)["us_nominal_gdp_usd_bn"]
capex26 = sum(h[f"capex_2026_{s}"] for s in ("amzn", "msft", "googl", "meta"))
ai26 = capex26 / gdp.loc[2026] * 100
booms = pd.Series({
    "Railroads,\nlate 1800s peak": h["boom_rail_peak_gdp"],
    "IT equipment and\nsoftware, 2000": h["boom_it_2000_gdp"],
    "Railroads,\n1870s to 1880s avg": h["boom_rail_avg_gdp"],
    "Hyperscaler capex\n2026 guidance": ai26,
    "AI data centres\n2025": h["boom_ai_dc_2025_gdp"],
    "Telecom,\n2000 peak": h["boom_telecom_peak_gdp"],
    "AI data centres\n2024": h["boom_ai_dc_2024_gdp"],
})
save_table(booms.round(2).to_frame("pct_of_gdp"), "m15_booms")
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), gridspec_kw={"width_ratios": [1.45, 1]})
ax = axes[0]
cols = [BLUE if ("AI" in k or "Hyperscaler" in k) else GREY for k in booms.index]
ax.barh(booms.index[::-1], booms.values[::-1], color=cols[::-1])
for i, v in enumerate(booms.values[::-1]):
    ax.text(v + 0.08, i, f"{v:.1f}%", va="center", fontsize=8.5)
ax.set_xlabel("Investment as % of US GDP"); ax.set_xlim(0, 7); ax.tick_params(axis="y", labelsize=8)
ax.grid(axis="y", visible=False); ax.set_title("Big, but not yet the biggest", fontsize=11)
ax = axes[1]
labels = ["US GDP growth,\nyear to Q2 2026", "AI investment,\nbefore imports", "AI investment,\nnet of imports"]
ax.bar(0, h["fvs_gdp_growth_q2_2026"], 0.55, color=GREY)
ax.bar(1, h["fvs_ai_contrib_high"] - h["fvs_ai_contrib_low"], 0.55, bottom=h["fvs_ai_contrib_low"], color=BLUE)
ax.bar(1, h["fvs_ai_contrib_low"], 0.55, color=BLUE, alpha=0.35)
ax.bar(2, h["fvs_ai_net_high"] - h["fvs_ai_net_low"], 0.55, bottom=h["fvs_ai_net_low"], color=ORANGE)
ax.bar(2, h["fvs_ai_net_low"], 0.55, color=ORANGE, alpha=0.35)
for i, txt, y in ((0, "2.1", 2.1), (1, "0.45 to 0.94", 0.94), (2, "0.14 to 0.38", 0.38)):
    ax.text(i, y + 0.06, txt, ha="center", fontsize=8.5)
ax.set_xticks(range(3)); ax.set_xticklabels(labels, fontsize=8); ax.set_ylabel("Percentage points")
ax.set_ylim(0, 2.5); ax.grid(axis="x", visible=False); ax.set_title("Less growth than it looks", fontsize=11)
finish(fig, "Figure 4: The AI build out against history and against growth",
       "author's model 15; Fox (Bloomberg) citing Kedrosky, Ulmer, BEA and Exante Data; IMF WEO; Flossbach von Storch (2026).",
       "fig15_history.png")
print(booms.round(2)); print("2026 capex share of GDP", round(ai26, 2))
