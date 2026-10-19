"""
MODEL 07  Do immigrants explain France's fiscal problem? A statistical test

Four questions, each answered only from INSEE, OECD and CEPII figures.

Q1 How much of population growth came from immigration?
       share = change in immigrant stock / change in total population
   Measured 2006 to 2022 because INSEE changed its census method in 2024
   (2023 and 2024 are provisional and not comparable).

Q2 How much of the labour force are immigrants, and is the gap closing?
       labour force share (INSEE 2024) and the unemployment gap 2014 to 2024.

Q3 How large is their net fiscal effect against the deficit?
   OECD (2021) average 2006 to 2018: +1.02% of GDP excluding pure public goods,
   -0.85% including them. Pure public goods (defence, debt interest, etc.) are
   shared out per head, so on that measure ANY group is in deficit in a country
   that runs deficits. The fair test is therefore per head:
       immigrant share of the deficit  = 0.85 / average deficit 2006 to 2018
       immigrant share of population   = INSEE average 2006 to 2018
   If the first is roughly equal to the second, immigrants are no more
   responsible for the deficit than anyone else.

Q4 What if immigrants worked at the same rate as non immigrants?
       extra workers = (69.8% - 62.4%) x 5.3m immigrants aged 15 to 64
       extra output  = extra workers x output per worker x relative productivity
   Output per worker = 2025 GDP / employed persons, with employed persons =
   labour force x (1 - unemployment rate) (IMF). Relative productivity is the
   one parameter not observed directly; it is shown as a range of 0.6 to 1.0
   of the average so the reader can see how sensitive the answer is.
       extra tax = extra output x revenue ratio (IMF, 2025)
"""
from common import *

style()
h = hand(); w = weo()
pop = pd.read_csv(DATA / "insee_immigrant_population_1946_2024.csv", index_col=0)
un = pd.read_csv(DATA / "insee_immigrant_unemployment_2014_2024.csv", index_col=0)

# Q1
d_imm = pop.loc[2022, "immigrants_thousand"] - pop.loc[2006, "immigrants_thousand"]
d_pop = pop.loc[2022, "population_thousand"] - pop.loc[2006, "population_thousand"]
q1 = {"immigrant_increase_k": d_imm, "population_increase_k": d_pop, "share_of_growth_pct": d_imm / d_pop * 100}

# Q2
lf_share = h["immig_lf_2024"] / h["total_lf_2024"] * 100
gap = (un.immigrants - un.non_immigrants)
q2 = {"labour_force_share_pct": lf_share, "unemp_gap_2014_pp": gap.loc[2014], "unemp_gap_2024_pp": gap.loc[2024],
      "non_eu_unemp_2014": un.loc[2014, "immigrants_non_eu"], "non_eu_unemp_2024": un.loc[2024, "immigrants_non_eu"],
      "women_activity_gap_pp": h["native_act_women"] - h["immig_act_women"],
      "men_activity_gap_pp": h["native_act_men"] - h["immig_act_men"]}

# Q3
bal = w["GGXCNL_NGDP"]["FRA"]
avg_def = -bal.loc[2006:2018].mean()
avg_share = pop.loc[2006:2018, "immigrant_share_pct"].mean()
imm_share_def = -h["oecd_immig_fiscal_incl_pg"] / avg_def * 100
q3 = {"avg_deficit_2006_2018_pct_gdp": avg_def, "immigrant_net_incl_public_goods_pct_gdp": h["oecd_immig_fiscal_incl_pg"],
      "immigrant_net_excl_public_goods_pct_gdp": h["oecd_immig_fiscal_excl_pg"],
      "immigrant_share_of_deficit_pct": imm_share_def, "immigrant_share_of_population_pct": avg_share,
      "cepii_range_pct_gdp": f"{h['cepii_low']} to {h['cepii_high']}",
      "deficit_2025_pct": -bal.loc[2025]}

# Q4
lur = w["LUR_FRA"].loc[2025] / 100
lf_total = h["total_lf_2024"]  # thousands, 15 to 64
employed = lf_total * (1 - lur)
gdp25 = w["NGDP_FRA"].loc[2025] * 1e9
out_per_worker = gdp25 / (employed * 1e3)
extra_workers = (h["native_emp_rate_2024"] - h["immig_emp_rate_2024"]) / 100 * h["immig_pop_1564_2023"] * 1e3
rev25 = w["GGR_NGDP"]["FRA"].loc[2025] / 100
q4 = []
for rp in (0.6, 0.8, 1.0):
    extra_out = extra_workers * out_per_worker * rp
    q4.append({"relative_productivity": rp, "extra_workers": extra_workers, "extra_output_eur_bn": extra_out / 1e9,
               "extra_output_pct_gdp": extra_out / gdp25 * 100, "extra_tax_eur_bn": extra_out * rev25 / 1e9,
               "extra_tax_pct_gdp": extra_out * rev25 / gdp25 * 100})
q4 = pd.DataFrame(q4).set_index("relative_productivity")
save_table(q4.round(2), "m07_employment_gap_scenario")

summ = pd.Series({**{f"Q1 {k}": v for k, v in q1.items()}, **{f"Q2 {k}": v for k, v in q2.items()},
                  **{f"Q3 {k}": v for k, v in q3.items()}, "Q4 output per worker EUR": out_per_worker})
save_table(summ.to_frame("value"), "m07_summary_table")

# Chart A: unemployment
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
ax = axes[0]
ax.plot(un.index, un.immigrants_non_eu, color=RED, label="Immigrants from outside the EU")
ax.plot(un.index, un.immigrants, color=VIOLET, label="All immigrants")
ax.plot(un.index, un.non_immigrants, color=BLUE, label="Non immigrants")
ax.set_ylabel("unemployment rate, %, ages 15 to 64"); ax.set_title("Unemployment is falling fastest for immigrants")
ax.legend(fontsize=8)
ax = axes[1]
labels = ["Share of\npopulation\n(2006 to 18 avg)", "Share of the\ndeficit\n(OECD, incl.\npublic goods)", "Share of\nlabour force\n(2024)"]
vals = [avg_share, imm_share_def, lf_share]
ax.bar(labels, vals, color=[GREY, RED, BLUE], width=0.55)
for i, v in enumerate(vals):
    ax.text(i, v + 0.4, f"{v:.1f}%", ha="center", fontsize=9)
ax.set_title("Immigrants' share, by measure"); ax.set_ylim(0, max(vals) * 1.3); ax.set_ylabel("%")
fig.suptitle("Figure 16: The statistics on immigration and the public finances", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 07: INSEE Enquete Emploi (via DGEF), INSEE Premiere Oct 2025, OECD International Migration Outlook 2021, IMF WEO.")
fig.tight_layout(rect=(0, 0.03, 1, 0.94)); fig.savefig(CHARTS / "fig10_immigration.png"); plt.close(fig)

with open(TABLES / "m07_summary.txt", "w") as fh:
    fh.write(summ.to_string() + "\n\n" + q4.round(2).to_string() + "\n")
print(open(TABLES / "m07_summary.txt").read())

# ---------- Appendix figure A7: what closing the employment gap is worth ----------
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
ax = axes[0]
ax.bar([f"{int(r*100)}%" for r in q4.index], q4.extra_tax_eur_bn, color=[YELLOW, AQUA, BLUE], width=0.55)
for i, v in enumerate(q4.extra_tax_eur_bn):
    ax.text(i, v + 0.4, f"EUR {v:.0f}bn", ha="center", fontsize=9)
ax.set_xlabel("Output of the extra workers relative to the average worker"); ax.set_ylabel("Extra tax per year, EUR bn")
ax.set_title(f"{q4.extra_workers.iloc[0]/1000:.0f}k more people in work", fontsize=10.5)
ax = axes[1]
labels2 = ["2025 deficit", "OECD immigrant\nnet cost", "Deficit without\nthat cost", "EU ceiling"]
vals2 = [q3["deficit_2025_pct"], -h["oecd_immig_fiscal_incl_pg"], q3["deficit_2025_pct"] + h["oecd_immig_fiscal_incl_pg"], 3.0]
ax.bar(labels2, vals2, color=[RED, VIOLET, "#f0a5a4", GREY], width=0.55)
for i, v in enumerate(vals2):
    ax.text(i, v + 0.08, f"{v:.1f}%", ha="center", fontsize=9)
ax.set_ylabel("% of GDP"); ax.set_title("Removing the whole immigrant net cost", fontsize=10.5)
fig.suptitle("Figure 15: Model 07, the employment gap matters more than the headline cost", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 07: INSEE, OECD (2021) net cost including pure public goods applied to the 2025 deficit, IMF WEO.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "figA7_model07_employment_gap.png"); plt.close(fig)


# ---------- Figure 23: France against Europe ----------
eu = pd.read_csv(DATA / "eurostat_migration_europe.csv").set_index("geo")
eu["foreign_born_share"] = eu.foreign_born_1jan2025 / eu.population_1jan2025 * 100
eu["employment_gap_pp"] = eu.emp_rate_native_2024 - eu.emp_rate_foreign_born_2024
save_table(eu.round(2), "m07_europe_comparison")
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
ax = axes[0]
e1 = eu.dropna(subset=["foreign_born_share"]).sort_values("foreign_born_share")
ax.barh(e1.name, e1.foreign_born_share, color=[BLUE if g == "FR" else (INK2 if g == "EU27_2020" else GREY) for g in e1.index], height=0.6)
for i, v in enumerate(e1.foreign_born_share):
    ax.text(v + 0.3, i, f"{v:.1f}%", va="center", fontsize=8)
ax.set_xlabel("Foreign born, % of population, 1 Jan 2025"); ax.grid(axis="y", visible=False)
ax.set_title("France is in the middle on numbers", fontsize=10.5)
ax = axes[1]
e2 = eu.sort_values("employment_gap_pp")
ax.barh(e2.name, e2.employment_gap_pp, color=[BLUE if g == "FR" else (INK2 if g == "EU27_2020" else GREY) for g in e2.index], height=0.6)
for i, v in enumerate(e2.employment_gap_pp):
    ax.text(v + (0.2 if v >= 0 else -0.2), i, f"{v:+.1f}", va="center", ha="left" if v >= 0 else "right", fontsize=8)
ax.axvline(0, color=INK2, lw=0.8)
ax.set_xlabel("Employment rate gap, native minus foreign born, points (2024)"); ax.grid(axis="y", visible=False)
ax.set_title("but near the top on the employment gap", fontsize=10.5)
fig.suptitle("Figure 17: Immigration in France compared with Europe", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Eurostat lfsa_ergacob (ages 20 to 64, 2024), migr_pop3ctb and tps00001 (1 Jan 2025). Portugal has no foreign born count published.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "fig11_immigration_europe.png"); plt.close(fig)
with open(TABLES / "m07_europe_summary.txt", "w") as fh:
    fh.write(eu[["foreign_born_share", "emp_rate_native_2024", "emp_rate_foreign_born_2024", "employment_gap_pp"]].round(1).to_string())
print(open(TABLES / "m07_europe_summary.txt").read())
