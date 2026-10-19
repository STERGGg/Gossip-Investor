"""
MODEL 04  What do the riots actually cost the state?

Thesis being tested: the riots are not the cause of France's fiscal problem; they
are an amplifier. If that is right, the direct damage should be small next to the
fiscal hole, while the indirect channels (a higher risk premium and weaker
investment) should be large.

Channel 1  Direct damage. Reported repair bills (2026 lycee protests, partial)
           and the June 2023 urban riots as a benchmark for a severe episode.
Channel 2  Risk premium. The unexplained part of the OAT spread from model 03,
           run through the debt engine of model 02:
              cost = interest(spread actually paid) - interest(spread fundamentals justify)
           A quick first year check: premium (bp) / 10,000 x EUR 310bn programme.
Channel 3  Growth and investment. OFCE estimates of how political uncertainty
           cut GDP growth (-0.1, -0.4, -0.3 points in 2024, 2025, 2026) and
           business investment growth (-0.2, -0.7, -1.5 points). Converted to euros:
              lost output in 2026 = 2026 GDP x (1 - product of (1 + effect))
              lost tax = lost output x revenue ratio (IMF, 2026)
              lost investment = 2025 NFC investment (INSEE) x cumulative effect
"""
import io, contextlib
from common import *

with contextlib.redirect_stdout(io.StringIO()):
    import model_02_debt_dynamics as m2
    import model_03_spread_fundamentals as m3

h = hand(); w = weo()
ngdp = w["NGDP_FRA"]; rev = w["GGR_NGDP"]["FRA"]

# Channel 1
direct = {
    "2026 lycee protests, Auvergne Rhone Alpes (up to)": h["riots2026_aura_high"],
    "2026 lycee protests, Ile de France": h["riots2026_idf"],
    "2026 lycee protests, Region Sud": h["riots2026_sud"],
    "2026 lycee protests, Hauts de France": h["riots2026_hdf"],
    "June 2023 riots, insured losses (France Assureurs)": h["riots2023_insured"],
    "June 2023 riots, total business damage (MEDEF)": h["riots2023_medef"],
}

# Channel 2
fund_2026 = m3.fr26_fund
paid = {"Jan to Sep 2026 average": m3.fr.loc[2026, "actual_bp"], "September 2026": m3.sep26,
        "October 2026 peak": h["spread_peak_oct2026"]}
base = m2.run(fund_2026, label="fundamentals only").set_index("year")
prem_rows = []
for name, s in paid.items():
    r = m2.run(s, label=name).set_index("year")
    extra = (r.interest_eur_bn - base.interest_eur_bn).loc[2027:2031]
    prem_rows.append({"spread_case": name, "spread_bp": s, "unexplained_bp": s - fund_2026,
                      "first_year_cost_eur_bn": (s - fund_2026) / 10000 * h["aft_programme_2026"],
                      "extra_interest_2027_eur_bn": extra.loc[2027], "extra_interest_2031_eur_bn": extra.loc[2031],
                      "cumulative_extra_2027_2031_eur_bn": extra.sum(),
                      "extra_debt_2031_pp": r.debt_pct_gdp.loc[2031] - base.debt_pct_gdp.loc[2031]})
prem = save_table(pd.DataFrame(prem_rows).set_index("spread_case").round(2), "m04_premium_cost")

# Channel 3
g_eff = [h["ofce_gdp_effect_2024"], h["ofce_gdp_effect_2025"], h["ofce_gdp_effect_2026"]]
i_eff = [h["ofce_inv_effect_2024"], h["ofce_inv_effect_2025"], h["ofce_inv_effect_2026"]]
level_gdp = 1 - np.prod([1 + e / 100 for e in g_eff])
level_inv = 1 - np.prod([1 + e / 100 for e in i_eff])
lost_output = level_gdp * ngdp.loc[2026]
lost_tax = lost_output * rev.loc[2026] / 100
lost_inv = level_inv * h["nfc_gfcf_2025"]

fdi = pd.Series({y: h[f"fdi_projects_{y}"] for y in range(2019, 2026)})
fdi_fall = fdi.loc[2025] / fdi.loc[2022] - 1

summary = pd.DataFrame([
    ["Direct damage, 2026 protests (reported so far)", (h["riots2026_sud"] + h["riots2026_idf"] + h["riots2026_aura_high"] + h["riots2026_hdf"]) / 1000, "one off"],
    ["Direct damage, 2023 riots (MEDEF, severe benchmark)", h["riots2023_medef"] / 1000, "one off"],
    ["Political premium, first year at Sep 2026 spread", prem.loc["September 2026", "first_year_cost_eur_bn"], "per year, rising"],
    ["Political premium, 2027 to 2031 at Sep 2026 spread", prem.loc["September 2026", "cumulative_extra_2027_2031_eur_bn"], "five years"],
    ["Political premium, 2027 to 2031 at Oct 2026 peak", prem.loc["October 2026 peak", "cumulative_extra_2027_2031_eur_bn"], "five years"],
    ["Lost tax revenue from uncertainty (OFCE), 2026", lost_tax, "per year"],
    ["Lost business investment from uncertainty (OFCE), 2026", lost_inv, "per year"],
    ["For scale: 2027 budget savings package", h["savings_2027"], "one year"],
], columns=["item", "eur_bn", "nature"]).set_index("item")
save_table(summary.round(2), "m04_bill_for_disorder")

# Chart: horizontal bars, log scale would hide nothing here so keep linear and label
fig, ax = plt.subplots(figsize=(8.5, 4.2))
s = summary.eur_bn.iloc[::-1]
colors = [GREY if "For scale" in i else (RED if "premium" in i else (YELLOW if "Lost" in i else BLUE)) for i in s.index]
ax.barh(range(len(s)), s.values, color=colors, height=0.6)
ax.set_yticks(range(len(s))); ax.set_yticklabels(s.index, fontsize=8.5)
for i, v in enumerate(s.values):
    ax.text(v + 0.8, i, f"EUR {v:,.2f}bn" if v < 1 else f"EUR {v:,.1f}bn", va="center", fontsize=8.5)
ax.set_xlabel("EUR billion"); ax.set_xlim(0, s.max() * 1.25)
fig.suptitle("Figure 8: The broken windows are the smallest part of the bill", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 04: INSEE, IMF WEO, ECB, AFT, OFCE (Oct 2025), France Assureurs, MEDEF, Region Sud.")
fig.tight_layout(rect=(0, 0.03, 1, 0.95)); fig.savefig(CHARTS / "fig06_bill_for_disorder.png"); plt.close(fig)

# Chart FDI
fig, ax = plt.subplots(figsize=(7, 3.4))
ax.bar(fdi.index, fdi.values, color=[BLUE if y != 2025 else RED for y in fdi.index], width=0.6)
for yv, v in fdi.items():
    ax.text(yv, v + 15, f"{int(v):,}", ha="center", fontsize=8.5)
ax.set_ylabel("foreign investment projects"); ax.set_ylim(0, 1450)
ax.set_title("Figure 10: Foreign investment projects in France")
source_note(fig, "EY Attractiveness Barometers 2020 to 2026.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig07_fdi_projects.png"); plt.close(fig)

with open(TABLES / "m04_summary.txt", "w") as fh:
    fh.write(prem.round(2).to_string() + "\n\n" + summary.round(2).to_string() + "\n\n")
    fh.write(f"Cumulative GDP level loss {level_gdp*100:.2f}% -> EUR {lost_output:.1f}bn output, EUR {lost_tax:.1f}bn tax (revenue ratio {rev.loc[2026]:.1f}%)\n")
    fh.write(f"Cumulative investment level loss {level_inv*100:.2f}% -> EUR {lost_inv:.1f}bn\n")
    fh.write(f"FDI projects 2022 to 2025 change {fdi_fall*100:.1f}%\n")
print(open(TABLES / "m04_summary.txt").read())

# ---------- Appendix figure A4: how the premium compounds ----------
fig, ax = plt.subplots(figsize=(8.5, 4))
yrs = list(range(2027, 2032)); width = 0.26
for i, (name, s) in enumerate(paid.items()):
    r = m2.run(s, label=name).set_index("year")
    extra = (r.interest_eur_bn - base.interest_eur_bn).loc[2027:2031]
    ax.bar([y_ + (i - 1) * width for y_ in yrs], extra.values, width=width, color=[AQUA, BLUE, RED][i],
           label=f"{name} ({s:.0f}bp, {s - fund_2026:.0f}bp unexplained)")
ax.set_ylabel("Extra interest per year, EUR bn"); ax.set_xticks(yrs)
ax.legend(fontsize=8, loc="upper left")
ax.set_title("Figure 9: Model 04, the political premium compounds as debt is refinanced")
source_note(fig, f"Author's model 04: interest at the spread paid minus interest at the {fund_2026:.0f}bp that fundamentals justify (model 03), run through model 02.")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(CHARTS / "figA4_model04_premium.png"); plt.close(fig)
