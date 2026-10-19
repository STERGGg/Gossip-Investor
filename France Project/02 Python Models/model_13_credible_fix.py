"""
MODEL 13  What would a credible fix look like, and has anyone done it before?

1. Size of the job: scenario D in Model 02 (overall deficit at the EU's 3% by 2029)
   needs the primary balance to rise from its 2026 level to its 2029 level. In euros
   this is the change in percentage points times 2029 nominal GDP (IMF).
2. History: the largest three year improvements in the primary balance across the 20
   euro area members, 1995 to 2025 (IMF WEO). Windows starting in 2020 or 2021 are
   dropped because they are the pandemic rebound, and windows that start from a
   primary deficit worse than 10% of GDP are dropped because those are one off bank
   rescues (Ireland 2010). Each window is tagged if it overlaps an EU/IMF programme
   (Greece 2010 to 2018, Ireland 2010 to 2013, Portugal 2011 to 2014, Spain's bank
   programme 2012 to 2013, Cyprus 2013 to 2016). Only each country's best window is kept.
3. A menu: reported annual yields of measures that are already on the table or have
   been costed, set against the size of the job. The trim of tax expenditures by a
   quarter and the one point cut in the spending ratio are illustrations, labelled as such.
"""
from common import *
import contextlib, io

style()
h = hand(); w = weo()
with contextlib.redirect_stdout(io.StringIO()):
    import model_02_debt_dynamics as m2
D = m2.scen[m2.scen.scenario.str.startswith("D")].set_index("year")
pb26, pb29 = D.loc[2026, "primary_balance_pct"], D.loc[2029, "primary_balance_pct"]
need_pp = pb29 - pb26
need_eur = need_pp / 100 * m2.ngdp.loc[2029]

pb = pd.read_csv(DATA / "imf_weo_primary_balance_euro.csv", index_col=0)
pb.columns = pb.columns.astype(int)
for c in ("LVA", "LTU", "MLT"):          # early years reported as exact zeros are missing data
    pb.loc[c, pb.loc[c] == 0] = np.nan
programmes = {"GRC": range(2010, 2019), "IRL": range(2010, 2014), "PRT": range(2011, 2015),
              "ESP": range(2012, 2014), "CYP": range(2013, 2017)}
rows = []
for c in pb.index:
    s = pb.loc[c]
    for start in range(1995, 2023):
        end = start + 3
        if start in (2020, 2021) or pd.isna(s.get(start)) or pd.isna(s.get(end)) or s[start] < -10:
            continue
        rows.append({"country": c, "start": start, "end": end, "pb_start": s[start], "pb_end": s[end],
                     "improvement_pp": s[end] - s[start],
                     "programme": any(y in programmes.get(c, []) for y in range(start, end + 1))})
win = pd.DataFrame(rows)
best = win.sort_values("improvement_pp", ascending=False).groupby("country").head(1).head(12).reset_index(drop=True)
save_table(best.round(2), "m13_largest_consolidations")
n_bigger = (best.improvement_pp >= need_pp).sum()
n_bigger_noprog = ((best.improvement_pp >= need_pp) & ~best.programme).sum()
fr = win[win.country == "FRA"].sort_values("improvement_pp", ascending=False).head(1)

spend = w["GGX_NGDP"]
ngdp27 = m2.ngdp.loc[2027]
menu = pd.Series({
    "2027 budget: new measures": h["budget2027_new_measures"],
    "Keep the 2023 pension reform (yield by 2030)": h["pension_repeal_2030"],
    "Illustration: trim tax expenditures by a quarter": 0.25 * h["tax_expenditures_2026"],
    "Illustration: spending ratio one point lower": 0.01 * ngdp27,
})
save_table(menu.round(1).to_frame("eur_bn"), "m13_menu")

# Chart
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4), gridspec_kw={"width_ratios": [1.35, 1]})
ax = axes[0]
EXTRA = {"CYP": "Cyprus", "SVN": "Slovenia", "SVK": "Slovakia", "LVA": "Latvia", "LTU": "Lithuania", "MLT": "Malta", "HRV": "Croatia", "EST": "Estonia", "LUX": "Luxembourg"}
lab = [f"{NAMES.get(r.country, EXTRA.get(r.country, r.country))} {r.start} to {r.end}" for r in best.itertuples()]
cols = [RED if p else GREY for p in best.programme]
ax.barh(range(len(best))[::-1], best.improvement_pp, color=cols, height=0.65)
ax.axvline(need_pp, color=BLUE, lw=2, ls="--")
ax.text(need_pp + 0.2, len(best) - 0.6, f"France needs {need_pp:.1f}pp", color=BLUE, fontsize=8.5)
ax.set_yticks(range(len(best))[::-1]); ax.set_yticklabels(lab, fontsize=8)
ax.set_xlabel("Rise in primary balance over three years, pp of GDP"); ax.grid(axis="y", visible=False)
ax.set_title("Largest three year consolidations, euro area\n(red: under an EU/IMF programme)", fontsize=10)
ax = axes[1]
bottom = 0
for (k_, v), c in zip(menu.items(), [BLUE, AQUA, YELLOW, GREY]):
    ax.bar(0, v, bottom=bottom, color=c, width=0.5, label=f"{k_}: €{v:.0f}bn"); bottom += v
ax.bar(1, need_eur, color=INK2, width=0.5)
ax.text(1, need_eur + 2, f"€{need_eur:.0f}bn", ha="center", fontsize=9)
ax.set_xticks([0, 1]); ax.set_xticklabels(["Menu of measures", "Needed by 2029"])
ax.set_ylabel("EUR billion a year"); ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.12))
ax.set_title("Size of the job", fontsize=10)
fig.suptitle("Figure 26: Has anyone fixed a deficit this large, and with what?", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 13: IMF WEO primary balances 1995 to 2025; Model 02 scenario D; PLF 2027, IFRAP, Institut Montaigne.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "fig18_credible_fix.png"); plt.close(fig)

with open(TABLES / "m13_summary.txt", "w") as fh:
    fh.write(f"Primary balance 2026 {pb26:.2f}% -> 2029 {pb29:.2f}%: {need_pp:.2f}pp = EUR {need_eur:.1f}bn at 2029 GDP\n\n")
    fh.write(best.round(2).to_string() + f"\n\nCountries whose best window beats France's need: {n_bigger}; without a programme: {n_bigger_noprog}\n")
    fh.write("France's own best three year window:\n" + fr.round(2).to_string() + "\n\nMenu (EUR bn):\n" + menu.round(1).to_string() + f"\nTotal {menu.sum():.1f}\n")
print(open(TABLES / "m13_summary.txt").read())
