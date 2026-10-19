"""
MODEL 09  What happens next? A probabilistic outlook to 2031

This model combines two kinds of uncertainty.

1. POLITICAL REGIME after the April and May 2027 elections (drawn once per path)
       P(RN president)                 = prediction market price for Le Pen (Polymarket, 29 Aug 2026)
       P(president wins a majority)    = average of the long base rate (4 of 5 legislative
                                         elections after a presidential vote, 2002 to 2022)
                                         and the recent record (0 of 2: 2022 and 2024)
   Four regimes follow:
     A  Centrist president with a majority   -> delivers the IMF primary balance path,
                                                spread returns to its calm H1 2026 average
     B  Centrist president, hung parliament  -> half of the IMF improvement (gridlock),
                                                spread stays at its September 2026 level,
                                                OFCE uncertainty growth penalty in 2028 and 2029
     C  RN president with a majority         -> the gridlock rate of consolidation (half of the IMF
                                                improvement, because the counter budget's largest
                                                savings are ones the government calls unconstitutional
                                                or dependent on the EU) minus the cost of repealing the
                                                2023 pension reform (Institut Montaigne / government
                                                estimate, EUR 8.2bn rising to 14.1bn by 2030),
                                                spread = September 2026 level plus the jump seen
                                                when an RN majority first looked possible
                                                (May to July 2024, ECB data)
     D  RN president, hung parliament        -> gridlock path as B, spread halfway between B and C,
                                                OFCE growth penalty
   2027 itself is run on the gridlock path for everyone, because the 2027 budget is
   being passed by the current parliament.

2. ECONOMIC SHOCKS each year (historical simulation)
   Each simulated year borrows a real year from 2008 to 2025, excluding 2020 and 2021 (the span where ECB, IMF
   and spread data all exist), in blocks of two years so that 2008 and 2009 or 2020 and
   2021 come together, and applies that year's shocks to nominal GDP growth (IMF), the
   Bund yield (ECB), the French spread (ECB) and the primary balance (IMF). How long a
   shock lasts is estimated from the data with an AR(1) for each series.
   Using whole historical years keeps the real correlations and fat tails (2009, 2011,
   2020) instead of assuming a normal distribution.

Debt engine: identical to model 02 (refinancing share 13.7% a year, calibrated curve
factor), so results are consistent with Chapter 4.

What counts as distress
   The primary balance needed to stabilise debt in 2031 is d x (r - g) / (1 + g).
   Eichengreen and Panizza (2016) find only 3 episodes in which any high or middle
   income country ran primary surpluses of 5% of GDP for ten years, and treat 3% as
   already demanding. A path is flagged "distress" if, in 2031, France would need a
   permanent primary surplus above 3% of GDP just to stop debt rising, or if the
   spread has gone above 300bp (roughly the Italian peak of 2018 to 2019 territory
   doubled, a level at which market access is in question).
   Gross financing need = deficit + 13.7% of negotiable debt (redemptions and bills),
   compared with the IMF's 15% of GDP high scrutiny line for advanced economies.

Market cross check: CDS implied default probability, with the standard 40% recovery
convention:  hazard = CDS / (1 - R);  P(default within 5y) = 1 - exp(-5 x hazard).
"""
import io, contextlib
from common import *

with contextlib.redirect_stdout(io.StringIO()):
    import model_02_debt_dynamics as m2

style()
rng = np.random.default_rng(2027)
N = 20000
h = hand(); w = weo(); y = yields(); sp = spreads_bp()
ngdp = w["NGDP_FRA"]; pb_imf = w["GGXONLB_NGDP"]["FRA"]; spend = w["GGX_NGDP"]["FRA"]
years = list(range(2027, 2032))

# ---------- political probabilities ----------
p_rn = h["p_lepen_market"] / 100
p_maj = (h["leg_majority_after_pres_2002_2022"] / 5 + 0 / 2) / 2
probs = {"A": (1 - p_rn) * p_maj, "B": (1 - p_rn) * (1 - p_maj), "C": p_rn * p_maj, "D": p_rn * (1 - p_maj)}
names = {"A": "Centrist president, majority", "B": "Centrist president, hung parliament",
         "C": "RN president, majority", "D": "RN president, hung parliament"}

# ---------- regime settings, all from data ----------
s_calm = sp["FRA"].loc["2026-01":"2026-06"].mean()
s_sep = sp["FRA"].loc["2026-09"].iloc[0]
rn_jump = sp["FRA"].loc["2024-07"].iloc[0] - sp["FRA"].loc["2024-05"].iloc[0]
spread_target = {"A": s_calm, "B": s_sep, "C": s_sep + rn_jump, "D": s_sep + rn_jump / 2}
pension_cost = {2027: h["pension_repeal_2027"], 2030: h["pension_repeal_2030"]}
pens = pd.Series({yr: np.interp(yr, [2027, 2030], [pension_cost[2027], pension_cost[2030]]) for yr in years})
pens = pens.clip(upper=h["pension_repeal_2030"])
pb_full = {yr: pb_imf.loc[yr] for yr in years}
pb_half = {yr: pb_imf.loc[2026] + 0.5 * (pb_imf.loc[yr] - pb_imf.loc[2026]) for yr in years}
pb_path = {"A": pb_full, "B": pb_half,
           "C": {yr: pb_half[yr] - (pens.loc[yr] / ngdp.loc[yr] * 100 if yr >= 2028 else 0) for yr in years},
           "D": pb_half}
growth_pen = {"A": 0, "B": h["ofce_gdp_effect_2026"], "C": 0, "D": h["ofce_gdp_effect_2026"]}

# ---------- historical shocks ----------
# Persistence is estimated, not assumed: AR(1) on annual levels
#   x(t) - mean = rho x (x(t-1) - mean) + e(t)
# for the Bund yield, the French spread and the primary balance. Growth shocks are
# deviations from mean nominal growth. The residuals e(t) of the same calendar year are
# kept together so that their real correlation is preserved.
bund_ann = y["DEU"].groupby(y.index.year).mean().loc[2007:2025]
fra_spread_ann = sp["FRA"].groupby(sp.index.year).mean().loc[2007:2025]
pb_ann = pb_imf.loc[1995:2025]

def ar1(x):
    x = x.dropna(); z = x - x.mean()
    rho = (z.shift(1) * z).sum() / (z.shift(1) ** 2).sum()
    e = (z - rho * z.shift(1)).dropna()
    return rho, e

rho_b, e_b = ar1(bund_ann)
rho_s, e_s = ar1(fra_spread_ann)
rho_p, e_p = ar1(pb_ann)
g_nom = (ngdp / ngdp.shift(1) - 1) * 100
e_g = (g_nom - g_nom.loc[2008:2025].mean()).loc[2008:2025]
H = pd.DataFrame({"g": e_g, "e_bund": e_b, "e_spread": e_s, "e_pb": e_p}).dropna()
# 2020 and 2021 are excluded: with only 18 years to sample, keeping the pandemic would make a
# once in a century collapse appear in roughly half of all five year paths. The 2008 to 2009
# crash, the 2011 to 2012 euro crisis and the 2022 inflation shock remain as tail events.
H = H.drop(index=[2020, 2021])
hist_idx = list(H.index)
H_dm = H - H.mean()
save_table(pd.concat([H.round(2), H.describe().round(2)]), "m09_historical_shocks")
# ---------- simulation ----------
f = m2.f; k = m2.k
D2024, D2025, r2025 = m2.D2024, m2.D2025, m2.r2025
bund0 = m2.bund
neg_share = h["negotiable_debt_jul2026"] / h["debt_q2_2026_eur"]

block_starts = [j for j in range(len(hist_idx) - 1) if hist_idx[j + 1] == hist_idx[j] + 1]
regime_draw = rng.choice(list(probs), size=N, p=list(probs.values()))
out = {k_: np.zeros((N, len(years))) for k_ in ["debt", "interest_pct", "spread", "gfn", "pb", "overall"]}
stab_need = np.zeros(N)

# The deterministic 2026 step is shared (common to every path)
base26 = m2.run(s_sep).set_index("year").loc[2026]
D2026 = base26.debt_eur_bn
r2026 = base26.effective_rate_pct / 100
m2026 = m2.k * m2.oat_2026_avg / 100

for i in range(N):
    reg = regime_draw[i]
    # block bootstrap of historical years, blocks of 2
    seq = []
    while len(seq) < len(years):
        j = rng.choice(block_starts)
        seq += [hist_idx[j], hist_idx[j + 1]]
    seq = seq[:len(years)]
    D = {2025: D2025, 2026: D2026}; r = {2026: r2026}; m = {2026: m2026}
    gdp = {2026: ngdp.loc[2026]}
    bund = bund0; spr_dev = 0.0; pb_eps = 0.0
    for t, yr in enumerate(years):
        shock = H_dm.loc[seq[t]]
        reg_t = "B" if yr == 2027 else reg            # 2027 budget passed by current parliament
        g_base = (ngdp.loc[yr] / ngdp.loc[yr - 1] - 1) * 100
        pen = growth_pen[reg_t] if yr in (2028, 2029) else (h["ofce_gdp_effect_2026"] if yr == 2027 else 0)
        g = g_base + pen + shock.g
        gdp[yr] = gdp[yr - 1] * (1 + g / 100)
        bund = max(bund0 + rho_b * (bund - bund0) + shock.e_bund, 0.0)
        spr_dev = rho_s * spr_dev + shock.e_spread
        spread = max(spread_target[reg_t] + spr_dev, 0.0)
        m[yr] = k * (bund + spread / 100) / 100
        r[yr] = ((1 - f) * r[yr - 1] * D[yr - 2] + f * m[yr] * D[yr - 2] + m[yr - 1] * (D[yr - 1] - D[yr - 2])) / D[yr - 1]
        interest = r[yr] * D[yr - 1]
        pb_eps = rho_p * pb_eps + shock.e_pb
        pb = pb_path[reg_t][yr] + pb_eps
        D[yr] = D[yr - 1] + interest - pb / 100 * gdp[yr]
        overall = pb - interest / gdp[yr] * 100
        out["debt"][i, t] = D[yr] / gdp[yr] * 100
        out["interest_pct"][i, t] = interest / gdp[yr] * 100
        out["spread"][i, t] = spread
        out["pb"][i, t] = pb
        out["overall"][i, t] = overall
        out["gfn"][i, t] = -overall + f * neg_share * D[yr - 1] / gdp[yr] * 100
    # debt stabilising primary balance in 2031, using the 2031 marginal rate and trend nominal growth
    g_trend = (ngdp.loc[2031] / ngdp.loc[2030] - 1)
    d = D[2031] / gdp[2031]
    stab_need[i] = d * (m[2031] - g_trend) / (1 + g_trend) * 100

debt31 = out["debt"][:, -1]
rising31 = out["debt"][:, -1] > out["debt"][:, -2]
distress = (stab_need > 3) | (out["spread"].max(axis=1) > 300)

# ---------- results ----------
def summarise(mask):
    return {"probability": mask.mean(),
            "debt_2031_median": np.median(debt31[mask]), "debt_2031_p5": np.percentile(debt31[mask], 5),
            "debt_2031_p95": np.percentile(debt31[mask], 95),
            "P_debt_above_130": (debt31[mask] > 130).mean(), "P_debt_above_140": (debt31[mask] > 140).mean(),
            "P_debt_still_rising_2031": rising31[mask].mean(),
            "interest_pct_2031_median": np.median(out["interest_pct"][mask, -1]),
            "stabilising_pb_2031_median": np.median(stab_need[mask]),
            "P_distress": distress[mask].mean()}

rows = {names[r_]: summarise(regime_draw == r_) for r_ in probs}
rows["All paths"] = summarise(np.ones(N, bool))
res = save_table(pd.DataFrame(rows).T.round(3), "m09_outlook_by_regime")

pct = pd.DataFrame({p: np.percentile(out["debt"], p, axis=0) for p in (5, 25, 50, 75, 95)}, index=years)
save_table(pct.round(1), "m09_debt_fan_percentiles")
gfn_pct = pd.DataFrame({p: np.percentile(out["gfn"], p, axis=0) for p in (5, 50, 95)}, index=years)
save_table(gfn_pct.round(1), "m09_gfn_percentiles")

# CDS implied
R = h["cds_recovery_convention"] / 100
cds_rows = []
for key in ("cds5y_2oct2026",):
    s = h[key] / 10000
    lam = s / (1 - R)
    cds_rows.append({"date": key, "cds_bp": h[key], "annual_hazard_pct": lam * 100,
                     "P_default_5y_pct": (1 - np.exp(-5 * lam)) * 100})
cds = save_table(pd.DataFrame(cds_rows).set_index("date").round(2), "m09_cds_implied")

# Sensitivity of the headline probabilities to the political inputs
sens = []
for prn in (0.35, h["p_lepen_market"] / 100, 0.65):
    for pm in (0.2, p_maj, 0.6):
        pr = {"A": (1 - prn) * pm, "B": (1 - prn) * (1 - pm), "C": prn * pm, "D": prn * (1 - pm)}
        wts = np.array([pr[r_] / probs[r_] for r_ in regime_draw]); wts /= wts.sum()
        sens.append({"P_RN": prn, "P_majority": pm, "P_debt_above_130": (wts * (debt31 > 130)).sum(),
                     "P_distress": (wts * distress).sum(), "median_debt_2031": np.median(np.repeat(debt31, 1)[np.argsort(debt31)][np.searchsorted(np.cumsum(wts[np.argsort(debt31)]), 0.5)])})
sens = save_table(pd.DataFrame(sens).round(3), "m09_sensitivity")

# ---------- charts ----------
hist_debt = w["GGXWDG_NGDP"]["FRA"].loc[2019:2025]
fig, ax = plt.subplots(figsize=(8.5, 4.3))
ax.plot(hist_debt.index, hist_debt.values, color=INK, lw=2)
xs = [2026] + years
d26 = base26.debt_pct_gdp
ax.fill_between(xs, [d26] + list(pct[5]), [d26] + list(pct[95]), color="#cfe0f5", label="5th to 95th percentile")
ax.fill_between(xs, [d26] + list(pct[25]), [d26] + list(pct[75]), color="#8db7ea", label="25th to 75th percentile")
ax.plot(xs, [d26] + list(pct[50]), color=BLUE, lw=2.4, label="Median")
ax.plot([2025, 2026], [hist_debt.loc[2025], d26], color=INK, lw=2)
for p_ in (5, 50, 95):
    ax.text(2031.15, pct.loc[2031, p_], f"{pct.loc[2031, p_]:.0f}%", va="center", fontsize=8.5, color=INK2)
ax.set_xlim(2019, 2032); ax.set_ylabel("Debt, % of GDP")
ax.set_title("Figure 20: Fan chart for French debt, 20,000 simulated paths")
ax.legend(loc="upper left", fontsize=8.5)
source_note(fig, "Author's model 09: IMF WEO, ECB, INSEE, AFT, OFCE, Institut Montaigne, Polymarket. Historical block bootstrap 2008 to 2025 excl. 2020 to 2021.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig13_debt_fan.png"); plt.close(fig)

fig, ax = plt.subplots(figsize=(8.5, 4.2))
bins = np.arange(105, 165, 1.5)
cols = {"A": GREEN, "B": BLUE, "C": RED, "D": YELLOW}
bottom = np.zeros(len(bins) - 1)
for r_ in ["A", "B", "D", "C"]:
    hcount, _ = np.histogram(debt31[regime_draw == r_], bins=bins)
    share = hcount / N * 100
    ax.bar(bins[:-1], share, width=1.4, bottom=bottom, color=cols[r_], align="edge",
           label=f"{names[r_]} ({probs[r_]*100:.0f}%)", edgecolor="white", linewidth=0.4)
    bottom += share
ax.axvline(130, color=INK2, lw=1, ls="--"); ax.text(130.5, bottom.max() * 0.95, "130%", fontsize=8, color=INK2)
ax.set_xlabel("Debt in 2031, % of GDP"); ax.set_ylabel("% of simulated paths")
ax.set_title("Figure 22: Where debt ends up in 2031, by political outcome")
ax.legend(fontsize=8, loc="upper right")
source_note(fig, "Author's model 09. Regime probabilities from Polymarket and the 2002 to 2024 legislative record.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig14_debt_2031_by_regime.png"); plt.close(fig)

with open(TABLES / "m09_summary.txt", "w") as fh:
    fh.write(f"P(RN) {p_rn:.3f}  P(majority) {p_maj:.3f}\nRegime probabilities: " + str({k_: round(v, 3) for k_, v in probs.items()}) + "\n")
    fh.write(f"Spread targets (bp): {({k_: round(v,1) for k_, v in spread_target.items()})}; RN jump May to Jul 2024 = {rn_jump:.1f}bp\n")
    fh.write(f"Pension repeal cost path (EUR bn): {pens.round(1).to_dict()}\n")
    fh.write(f"Historical shock years used: {hist_idx}\n")
    fh.write(f"AR(1) persistence: bund {rho_b:.3f}, spread {rho_s:.3f}, primary balance {rho_p:.3f}\n\n")
    fh.write(res.round(3).to_string() + "\n\nDebt fan percentiles\n" + pct.round(1).to_string())
    fh.write("\n\nGross financing need percentiles (% GDP)\n" + gfn_pct.round(1).to_string())
    fh.write("\n\nCDS implied\n" + cds.to_string() + "\n\nSensitivity\n" + sens.to_string() + "\n")
    fh.write(f"\nShare of paths where the 2031 stabilising primary balance exceeds 3%: {(stab_need>3).mean():.3f}; spread ever above 300bp: {(out['spread'].max(axis=1)>300).mean():.3f}\n")
    gfn27_eur = np.median(out["gfn"][:, 0]) / 100 * ngdp.loc[2027]
    fh.write(f"Median 2027 gross financing need EUR {gfn27_eur:.0f}bn vs ESM available capacity EUR {h['esm_available_capacity']:.0f}bn\n")
    fh.write(f"Share of paths with GFN above the IMF 15% line in every year: {(out['gfn'] > h['imf_gfn_benchmark_ae']).all(axis=1).mean():.3f}\n")
    fh.write(f"Median 2031 stabilising primary balance: {np.median(stab_need):.2f}% ; median 2031 primary balance achieved: {np.median(out['pb'][:,-1]):.2f}%\n")
print(open(TABLES / "m09_summary.txt").read())

# ---------- Appendix figure A8: distress by regime and sensitivity ----------
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4))
ax = axes[0]
order = ["A", "B", "C", "D"]
dvals = [res.loc[names[r_], "P_distress"] * 100 for r_ in order]
ax.bar([names[r_].replace(", ", ",\n") for r_ in order], dvals, color=[cols[r_] for r_ in order], width=0.55)
ax.axhline(res.loc["All paths", "P_distress"] * 100, color=INK2, ls="--", lw=1)
ax.text(-0.45, res.loc["All paths", "P_distress"] * 100 + 0.4, "all paths", fontsize=8, color=INK2, ha="left")
for i, v in enumerate(dvals):
    ax.text(i, v + 0.4, f"{v:.0f}%", ha="center", fontsize=9)
ax.tick_params(axis="x", labelsize=7.5); ax.set_ylabel("% of paths in distress by 2031")
ax.set_title("Chance of distress by political outcome", fontsize=10.5)
ax = axes[1]
piv = sens.pivot(index="P_majority", columns="P_RN", values="P_debt_above_130") * 100
im = ax.imshow(piv.values, cmap="Blues", vmin=35, vmax=50, origin="lower", aspect="auto")
ax.set_xticks(range(piv.shape[1])); ax.set_xticklabels([f"{v*100:.0f}%" for v in piv.columns])
ax.set_yticks(range(piv.shape[0])); ax.set_yticklabels([f"{v*100:.0f}%" for v in piv.index])
for i in range(piv.shape[0]):
    for j in range(piv.shape[1]):
        ax.text(j, i, f"{piv.values[i, j]:.0f}%", ha="center", va="center", fontsize=9, color="white" if piv.values[i, j] > 45 else INK)
ax.set_xlabel("Probability of an RN president"); ax.set_ylabel("Probability of a majority")
ax.grid(False); ax.set_title("Chance debt ends above 130%, by input", fontsize=10.5)
fig.suptitle("Figure 21: Model 09, the result barely moves when the political inputs change", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 09: 20,000 simulated paths. Distress = 2031 debt stabilising primary surplus above 3% of GDP (Eichengreen and Panizza).")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "figA8_model09_distress.png"); plt.close(fig)
