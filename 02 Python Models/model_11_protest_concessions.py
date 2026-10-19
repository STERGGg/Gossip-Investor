"""
MODEL 11  Does the street win? The cost of concessions against the cost of damage

Question: when protests have moved French budgets in the past, was the cost the
damage done in the streets or the concessions governments made to end them?

1. Episode table: every large protest movement since 1995, what happened to the
   policy it targeted and the reported annual budget cost of the concession.
   Costs are reported figures (hand_collected_sources.csv), converted to % of GDP
   with IMF WEO nominal GDP for the year the cost first applied.
2. Scale: the gilets jaunes concessions as a share of the 2019 deficit, and in
   years of the 2027 savings package, against the reported direct damage of the
   2026 lycee protests and the 2023 riots.
3. Chart (Figure 16): reported damage against concessions and the political
   premium from Model 04, on a log scale because they differ by a factor of a thousand.
"""
from common import *
import contextlib, io

style()
h = hand(); w = weo()
ngdp = w["NGDP_FRA"]; bal = w["GGXCNL_NGDP"]["FRA"]
with contextlib.redirect_stdout(io.StringIO()):
    import model_04_cost_of_unrest as m4

damage_2026 = (h["riots2026_aura_high"] + h["riots2026_idf"] + h["riots2026_sud"] + h["riots2026_hdf"]) / 1000
episodes = pd.DataFrame([
    ["1995", "Juppe plan (pensions, social security)", "Pension part withdrawn after three weeks of strikes", np.nan, None],
    ["2006", "First employment contract (CPE)", "Law withdrawn after student protests", np.nan, None],
    ["2018 to 2019", "Gilets jaunes", "Fuel tax rise cancelled; tax cuts and income top ups", h["gj_total"], 2019],
    ["2023", "Pension reform (age 62 to 64)", "Passed with Article 49.3 despite protests", 0.0, 2023],
    ["2025", "Pension reform suspension", "Suspended to survive a censure vote (cost in 2027)", h["pension_suspension_2027"], 2027],
    ["2026", "Lycee protests", "Five working groups; first decisions due end October", np.nan, None],
], columns=["year", "movement", "outcome", "annual_cost_eur_bn", "gdp_year"])
episodes["cost_pct_gdp"] = [c / ngdp.loc[int(y)] * 100 if pd.notna(y) else np.nan for c, y in zip(episodes.annual_cost_eur_bn, episodes.gdp_year)]
save_table(episodes.drop(columns="gdp_year").round(2).set_index("year"), "m11_concessions")

deficit_2019 = -bal.loc[2019] / 100 * ngdp.loc[2019]
gj_share_def = h["gj_total"] / deficit_2019 * 100
gj_vs_package = h["gj_total"] / h["savings_2027"] * 100
gj_vs_damage = h["gj_total"] / damage_2026
premium5 = m4.prem.loc["September 2026", "cumulative_extra_2027_2031_eur_bn"]

bars = pd.Series({
    "2026 lycee protests: reported damage": damage_2026,
    "2023 riots: business damage (MEDEF)": h["riots2023_medef"] / 1000,
    "2025 pension suspension: cost in 2027": h["pension_suspension_2027"],
    "Gilets jaunes concessions: cost per year": h["gj_total"],
    "2027 savings package": h["savings_2027"],
    "Political premium 2027 to 2031 (Model 04)": premium5,
})
save_table(bars.round(2).to_frame("eur_bn"), "m11_scale")

fig, ax = plt.subplots(figsize=(9, 4.4))
cols = [RED, RED, YELLOW, YELLOW, GREY, BLUE]
ax.barh(range(len(bars))[::-1], bars.values, color=cols, height=0.6)
ax.set_xscale("log"); ax.set_yticks(range(len(bars))[::-1]); ax.set_yticklabels(bars.index, fontsize=9)
for i, v in enumerate(bars.values):
    ax.text(v * 1.15, len(bars) - 1 - i, f"€{v:,.2f}bn" if v < 1 else f"€{v:,.1f}bn", va="center", fontsize=8.5)
ax.set_xlim(0.01, 400); ax.set_xlabel("EUR billion, log scale"); ax.grid(axis="y", visible=False)
ax.set_title("Damage in red, concessions in yellow", fontsize=10.5)
fig.suptitle("Figure 24: What protests cost the French state", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 11: Public Senat, Sud Radio, MEDEF, AFP (Le Maire 2019), IFRAP, Euronews; Model 04 premium.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "fig16_protest_concessions.png"); plt.close(fig)

with open(TABLES / "m11_summary.txt", "w") as fh:
    fh.write(episodes.drop(columns="gdp_year").round(2).to_string() + "\n\n")
    fh.write(f"Reported direct damage of 2026 protests (up to): EUR {damage_2026*1000:.0f}m\n")
    fh.write(f"Gilets jaunes EUR {h['gj_total']}bn = {h['gj_total']/ngdp.loc[2019]*100:.2f}% of 2019 GDP, "
             f"{gj_share_def:.1f}% of the 2019 deficit (EUR {deficit_2019:.1f}bn), {gj_vs_package:.0f}% of the 2027 package, "
             f"{gj_vs_damage:.0f} times the 2026 reported damage\n")
    fh.write(f"Political premium 2027 to 2031 at Sep 2026 spread: EUR {premium5:.1f}bn\n")
print(open(TABLES / "m11_summary.txt").read())
