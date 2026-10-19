"""
MODEL 12  Why France and not Japan, the US or the UK? And could France have a Truss moment?

1. Fiscal comparison for 2025 and 2031 (IMF WEO, October 2026 vintage via OpenBB):
   gross debt, overall and primary balance, revenue, and the interest bill measured as
   primary balance minus overall balance. Interest as a share of revenue shows how
   much of each euro, dollar, pound or yen of tax already goes to creditors.
2. Who holds the debt: non resident share of French negotiable debt (Banque de France
   via AFT) against the foreign share of Japanese government bonds (Japan MoF).
3. Truss test: the 30 year gilt rose about 130bp in three trading days in September
   2022 (Bank of England). The same jump is added to the French spread from 2027 in
   the Model 02 debt engine, and the extra interest is compared with the September
   2026 path. First year cost is also shown on a simple basis: the jump times the 2027
   issuance programme plus the stock of short term bills, which reprice within a year.
"""
from common import *
import contextlib, io

style()
h = hand()
d = pd.read_csv(DATA / "imf_weo_international.csv")
long = d.melt(id_vars=["ind", "country_code"], var_name="year", value_name="v")
long["year"] = long.year.astype(int)
W = {i: g.pivot_table(index="year", columns="country_code", values="v") for i, g in long.groupby("ind")}
order = ["JPN", "ITA", "USA", "FRA", "GBR", "DEU"]
nm = {"JPN": "Japan", "ITA": "Italy", "USA": "United States", "FRA": "France", "GBR": "United Kingdom", "DEU": "Germany"}

rows = []
for c in order:
    for yr in (2025, 2031):
        intr = W["GGXONLB_NGDP"].loc[yr, c] - W["GGXCNL_NGDP"].loc[yr, c]
        rows.append({"country": nm[c], "year": yr, "debt_pct_gdp": W["GGXWDG_NGDP"].loc[yr, c],
                     "overall_balance": W["GGXCNL_NGDP"].loc[yr, c], "primary_balance": W["GGXONLB_NGDP"].loc[yr, c],
                     "interest_pct_gdp": intr, "revenue_pct_gdp": W["GGR_NGDP"].loc[yr, c],
                     "interest_pct_revenue": intr / W["GGR_NGDP"].loc[yr, c] * 100})
comp = save_table(pd.DataFrame(rows).round(2).set_index(["country", "year"]), "m12_international")
debt_change = (W["GGXWDG_NGDP"].loc[2031] - W["GGXWDG_NGDP"].loc[2025])[order].round(1)

# Truss test through the Model 02 engine
with contextlib.redirect_stdout(io.StringIO()):
    import model_02_debt_dynamics as m2
jump = h["truss_30y_move"]
base = m2.run(m2.spread_sep_2026).set_index("year")
truss = m2.run(m2.spread_sep_2026 + jump).set_index("year")
extra = (truss.interest_eur_bn - base.interest_eur_bn).loc[2027:2031]
simple_first_year = jump / 10000 * (h["aft_programme_2027"] + h["btf_stock_jul2026"])
truss_tab = save_table(pd.DataFrame({"extra_interest_eur_bn": extra.round(2),
                                     "debt_pct_gdp_truss": truss.debt_pct_gdp.loc[2027:2031].round(2),
                                     "debt_pct_gdp_base": base.debt_pct_gdp.loc[2027:2031].round(2)}), "m12_truss_test")

# Chart
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3), gridspec_kw={"width_ratios": [1.2, 1]})
ax = axes[0]
for c in order:
    x = W["GGXONLB_NGDP"].loc[2025, c]; yv = W["GGXWDG_NGDP"].loc[2025, c]
    col = BLUE if c == "FRA" else (VIOLET if c == "ITA" else (ORANGE if c == "DEU" else INK2))
    ax.scatter(x, yv, s=90, color=col, zorder=3)
    ax.annotate(nm[c], (x, yv), xytext=(6, 4), textcoords="offset points", fontsize=8.5)
ax.axvline(0, color=GREY, lw=1)
ax.set_xlabel("Primary balance 2025, % of GDP"); ax.set_ylabel("Gross debt 2025, % of GDP")
ax.set_title("Debt against the primary balance", fontsize=10.5)
ax = axes[1]
x = np.arange(len(order))
v25 = [comp.loc[(nm[c], 2025), "interest_pct_revenue"] for c in order]
v31 = [comp.loc[(nm[c], 2031), "interest_pct_revenue"] for c in order]
ax.bar(x - 0.2, v25, 0.4, color=GREY, label="2025")
ax.bar(x + 0.2, v31, 0.4, color=[BLUE if c == "FRA" else INK2 for c in order], label="2031 (IMF projection)")
ax.set_xticks(x); ax.set_xticklabels([nm[c].replace("United ", "U. ") for c in order], fontsize=8.5, rotation=20)
ax.set_ylabel("Interest as % of government revenue"); ax.legend(fontsize=8)
ax.set_title("Share of revenue paid as interest", fontsize=10.5)
fig.suptitle("Figure 25: France against Japan, the US and the UK", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 12: IMF World Economic Outlook (October 2026) via OpenBB; interest = primary minus overall balance.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "fig17_france_japan_us_uk.png"); plt.close(fig)

with open(TABLES / "m12_summary.txt", "w") as fh:
    fh.write(comp.to_string() + "\n\nDebt change 2025 to 2031 (pp):\n" + debt_change.to_string() + "\n\n")
    fh.write(f"Non resident share: France {h['nonresident_share']}% of negotiable debt; Japan foreign {h['jgb_foreign_share']}% and BoJ {h['jgb_boj_share']}% of JGBs\n")
    fh.write(f"Truss test (+{jump:.0f}bp from 2027): extra interest 2027 EUR {extra.loc[2027]:.1f}bn, 2031 EUR {extra.loc[2031]:.1f}bn, "
             f"cumulative EUR {extra.sum():.1f}bn; debt 2031 {truss.debt_pct_gdp.loc[2031]:.1f}% vs {base.debt_pct_gdp.loc[2031]:.1f}%\n")
    fh.write(f"Simple first year: {jump:.0f}bp x (EUR {h['aft_programme_2027']:.0f}bn programme + EUR {h['btf_stock_jul2026']:.0f}bn bills) = EUR {simple_first_year:.1f}bn\n")
print(open(TABLES / "m12_summary.txt").read())
