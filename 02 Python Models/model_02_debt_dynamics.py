"""
MODEL 02  Debt dynamics and the cost of the risk premium (2026 to 2031)

The question: how much of France's future interest bill comes from the extra
premium that markets now charge, and what happens to the debt ratio under
different political outcomes.

Mechanics (all in euros, then divided by nominal GDP)
    D(t)   = D(t-1) + interest(t) - primary balance(t)
    interest(t) = r_eff(t) x D(t-1)
The effective rate r_eff moves slowly because only part of the stock is
refinanced each year:
    r_eff(t) = [ (1 - f) x r_eff(t-1) x D(t-2)  +  f x m(t) x D(t-2)
                 + m(t-1) x (D(t-1) - D(t-2)) ] / D(t-1)
    f = share of negotiable debt that is repriced each year
      = (2026 medium and long term redemptions + stock of short term bills) / negotiable debt
      = (175.8 + 220) / 2,882 = 13.7%   (AFT figures; bills are rolled within the year)
    m = marginal borrowing rate = k x (Bund 10y + spread)
k is a curve factor because France borrows across the whole curve, not only at
10 years. It is NOT assumed: it is solved so that the model reproduces the IMF's
own 2026 interest bill from the 2025 starting point and the average 2026 OAT
yield actually observed (ECB data, January to September 2026).

Starting points (sourced, see data/hand_collected_sources.csv)
    Debt end 2025 = EUR 3,460.5bn (INSEE)
    Nominal GDP and primary balance path = IMF WEO
    Bund 10y held flat at its September 2026 level (ECB)

Scenario settings are the only numbers chosen here, and each is tied to an
observed level in the data rather than invented.
"""
from common import *

style()
h = hand(); w = weo(); y = yields(); sp = spreads_bp()
ngdp = w["NGDP_FRA"].copy()                   # EUR bn
pb_imf = w["GGXONLB_NGDP"]["FRA"]             # % GDP
bal_imf = w["GGXCNL_NGDP"]["FRA"]
spend = w["GGX_NGDP"]["FRA"]

f = (h["mlt_amortisation_2026"] + h["btf_stock_jul2026"]) / h["negotiable_debt_jul2026"]
bund = y["DEU"].loc["2026-09"].iloc[0]
oat_2026_avg = y["FRA"].loc["2026-01":"2026-09"].mean()
oat_2025_avg = y["FRA"].loc["2025"].mean()

# Observed spread levels used to anchor scenarios (bp)
spread_pre_dissolution = sp["FRA"].loc["2024-01":"2024-05"].mean()
spread_calm_2026 = sp["FRA"].loc["2026-01":"2026-06"].mean()
spread_sep_2026 = sp["FRA"].loc["2026-09"].iloc[0]
spread_peak = h["spread_peak_oct2026"]

# Starting stock and effective rate from IMF (interest = pb - overall balance)
D2025 = h["debt_2025_eur"]
D2024 = w["GGXWDG_NGDP"]["FRA"].loc[2024] / 100 * ngdp.loc[2024]
int_2025 = (pb_imf.loc[2025] - bal_imf.loc[2025]) / 100 * ngdp.loc[2025]
int_2026_imf = (pb_imf.loc[2026] - bal_imf.loc[2026]) / 100 * ngdp.loc[2026]
r2025 = int_2025 / D2024


def interest_2026(k):
    D2026_pre = D2025
    r = ((1 - f) * r2025 * D2024 + f * k * oat_2026_avg / 100 * D2024 + k * oat_2025_avg / 100 * (D2025 - D2024)) / D2025
    return r * D2025

# solve k by bisection so model 2026 interest = IMF 2026 interest
lo, hi = 0.3, 1.5
for _ in range(60):
    mid = (lo + hi) / 2
    if interest_2026(mid) > int_2026_imf:
        hi = mid
    else:
        lo = mid
k = (lo + hi) / 2


def run(spread_bp, growth_hit_pp=None, pb_path=None, label=""):
    """Simulate 2026 to 2031. spread_bp applies from 2027 (2026 is mostly fixed already)."""
    years = list(range(2026, 2032))
    gdp = ngdp.copy()
    if growth_hit_pp:
        for yr in years:
            hit = sum(growth_hit_pp.get(z, 0) for z in years if z <= yr) / 100
            gdp.loc[yr] = ngdp.loc[yr] * (1 + hit)
    D = {2024: D2024, 2025: D2025}; r = {2025: r2025}
    m = {2025: k * oat_2025_avg / 100, 2026: k * oat_2026_avg / 100}
    out = []
    for yr in years:
        if yr >= 2027:
            m[yr] = k * (bund + spread_bp / 100) / 100
        r[yr] = ((1 - f) * r[yr - 1] * D[yr - 2] + f * m[yr] * D[yr - 2] + m[yr - 1] * (D[yr - 1] - D[yr - 2])) / D[yr - 1]
        interest = r[yr] * D[yr - 1]
        pb_pct = pb_path[yr] if pb_path is not None else pb_imf.loc[yr]
        if growth_hit_pp:
            # revenue moves one for one with GDP, spending in euros does not:
            # a GDP shortfall of x% worsens the primary balance by spending ratio times x
            short = 1 - gdp.loc[yr] / ngdp.loc[yr]
            pb_pct = pb_pct - spend.loc[yr] * short
        pb_eur = pb_pct / 100 * gdp.loc[yr]
        D[yr] = D[yr - 1] + interest - pb_eur
        out.append({"scenario": label, "year": yr, "debt_eur_bn": D[yr], "debt_pct_gdp": D[yr] / gdp.loc[yr] * 100,
                    "interest_eur_bn": interest, "interest_pct_gdp": interest / gdp.loc[yr] * 100,
                    "effective_rate_pct": r[yr] * 100, "marginal_rate_pct": m[yr] * 100,
                    "primary_balance_pct": pb_pct, "overall_balance_pct": pb_pct - interest / gdp.loc[yr] * 100})
    return pd.DataFrame(out)

# Scenario D primary balance: rises in equal steps from the 2026 IMF level so the
# overall deficit reaches the 3% EU ceiling by 2029 (solved below by iteration)
def pb_path_to_3pct():
    target_pb = pb_imf.loc[2026]
    for _ in range(200):
        steps = {yr: pb_imf.loc[2026] + (target_pb - pb_imf.loc[2026]) * min(1, (yr - 2026) / 3) for yr in range(2026, 2032)}
        res = run(spread_calm_2026, pb_path=steps)
        ob = res.set_index("year").loc[2029, "overall_balance_pct"]
        if abs(ob + 3) < 0.005:
            break
        target_pb += (-3 - ob) * 0.8
    return steps

ofce_hit = {2027: h["ofce_gdp_effect_2026"], 2028: h["ofce_gdp_effect_2026"]}
half_pb = {yr: pb_imf.loc[2026] + 0.5 * (pb_imf.loc[yr] - pb_imf.loc[2026]) for yr in range(2026, 2032)}

scen = pd.concat([
    run(spread_pre_dissolution, label="A  Spread back to pre dissolution level"),
    run(spread_sep_2026, label="B  IMF path at September 2026 spread"),
    run(spread_peak, growth_hit_pp=ofce_hit, pb_path=half_pb, label="C  Unrest persists"),
    run(spread_calm_2026, pb_path=pb_path_to_3pct(), label="D  Credible consolidation to 3%"),
])
save_table(scen.round(2).set_index(["scenario", "year"]), "m02_scenarios")

summary = scen[scen.year == 2031].set_index("scenario")[["debt_pct_gdp", "interest_eur_bn", "interest_pct_gdp", "effective_rate_pct"]]
summary["cumulative_interest_2027_2031"] = scen[scen.year >= 2027].groupby("scenario").interest_eur_bn.sum()
base = summary.loc["A  Spread back to pre dissolution level", "cumulative_interest_2027_2031"]
summary["extra_interest_vs_A"] = summary.cumulative_interest_2027_2031 - base
save_table(summary.round(1), "m02_summary_2031")

# Rule of thumb: first year cost of 10bp on the year's financing need
first_year_cost_per_10bp = h["aft_programme_2026"] * 0.001

# Chart
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
cols = [GREEN, BLUE, RED, YELLOW]
for (name, g), c in zip(scen.groupby("scenario"), cols):
    g = g.set_index("year")
    hist = pd.Series({2024: 112.6, 2025: 115.6})
    axes[0].plot(list(hist.index) + list(g.index), list(hist.values) + list(g.debt_pct_gdp), color=c, label=name)
    axes[1].plot(g.index, g.interest_eur_bn, color=c, label=name)
axes[0].set_title("Debt, % of GDP"); axes[1].set_title("Interest bill, EUR bn")
axes[1].legend(fontsize=7.5, loc="upper left")
fig.suptitle("Figure 18: Four fixed paths for French debt to 2031", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 02 using INSEE, IMF WEO, ECB yields and AFT maturity data.")
fig.tight_layout(rect=(0, 0.03, 1, 0.95)); fig.savefig(CHARTS / "fig12_debt_scenarios.png"); plt.close(fig)

with open(TABLES / "m02_summary.txt", "w") as fh:
    fh.write(f"Refinancing share f = {f:.4f}\nCurve factor k (calibrated) = {k:.3f}\n")
    fh.write(f"Bund 10y Sep 2026 = {bund:.3f}% ; OAT avg 2025 = {oat_2025_avg:.3f}% ; OAT avg Jan-Sep 2026 = {oat_2026_avg:.3f}%\n")
    fh.write(f"Spreads (bp): pre dissolution Jan-May 2024 {spread_pre_dissolution:.1f}; calm H1 2026 {spread_calm_2026:.1f}; Sep 2026 {spread_sep_2026:.1f}; Oct peak {spread_peak}\n")
    fh.write(f"Interest 2025 EUR {int_2025:.1f}bn, effective rate 2025 {r2025*100:.2f}% ; IMF interest 2026 EUR {int_2026_imf:.1f}bn\n")
    fh.write(f"First year cost of +10bp across the 2026 programme: EUR {first_year_cost_per_10bp:.2f}bn\n\n")
    fh.write(summary.round(2).to_string() + "\n\n")
    fh.write(scen.round(2).to_string())
print(open(TABLES / "m02_summary.txt").read()[:3500])

# ---------- Appendix figure A2: the refinancing mechanism ----------
fig, ax = plt.subplots(figsize=(8.5, 4))
for (name, g), c in zip(scen.groupby("scenario"), cols):
    g = g.set_index("year")
    ax.plot(g.index, g.marginal_rate_pct, color=c, ls=(0, (3, 2)), lw=1.4)
    ax.plot(g.index, g.effective_rate_pct, color=c, lw=2.2, label=name)
ax.text(2026.05, scen.marginal_rate_pct.max() + 0.08, "dashed = rate on new borrowing", fontsize=8, color=INK2)
ax.set_ylabel("%"); ax.legend(fontsize=7.5, loc="lower right")
ax.set_title("Figure 19: Model 02, the average rate slowly catches up with the new rate")
source_note(fig, f"Author's model 02. {f*100:.1f}% of negotiable debt repriced each year (AFT); curve factor {k:.2f} calibrated to the IMF 2026 interest bill.")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(CHARTS / "figA2_model02_refinancing.png"); plt.close(fig)
