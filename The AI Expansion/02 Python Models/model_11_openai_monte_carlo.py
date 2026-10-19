"""
MODEL 11  Running the probabilities: can OpenAI pay?
A Monte Carlo simulation of OpenAI's revenue from 2026 to 2030, 20,000 paths.

1. Central path: OpenAI's own plan (2026 30bn, 2027 62bn, 2030 282.5bn, with 2028 and 2029
   interpolated geometrically as in Model 03).
2. Uncertainty: each year the log of revenue moves away from the plan by a random shock
   drawn from a normal distribution with mean m and standard deviation s, and the shocks
   accumulate (a miss in 2027 carries into 2028). Both are calibrated to OpenAI's own record:
   s is the average absolute size of the two big revisions to OpenAI's numbers in 2026, the
   October gap between the 70bn run rate investors had been told about and the 50bn OpenAI
   confirmed (ln(50/70)), and the February upgrade of its own revenue forecasts by about 27%
   (ln(1.27)). In the central case the plan is unbiased (m = 0). A pessimistic case gives the
   plan a downward drift equal to the October gap spread over three years.
3. Price deflation: a separate sensitivity cuts revenue growth by a further 10 percentage
   points a year from 2027, as a stand in for prices falling faster than usage grows.
4. Costs are taken from the same plan (cost = planned revenue minus planned cash flow) and
   treated as fixed, because most of them are compute contracts already signed.
5. Outputs: the chance that revenue in 2027 covers the Oracle contract (60bn), that revenue
   reaches the 175bn a year average commitment by 2029 and 2030, that the company turns
   cash positive by 2030, and the distribution of cumulative cash needed to 2030 against
   the 122bn raised in March 2026.
"""
from common import *

style(); h = hand()
rng = np.random.default_rng(2026)
N = 20000
yrs = list(range(2026, 2031))
plan = {2026: h["openai_rev_2026_plan"], 2027: h["openai_rev_2027_plan"], 2030: h["openai_rev_2030_plan"]}
g = (plan[2030] / plan[2027]) ** (1 / 3)
plan[2028] = plan[2027] * g; plan[2029] = plan[2027] * g ** 2
plan = pd.Series(plan).sort_index()
cf_plan = pd.Series({y: h[f"openai_cf_{y}"] for y in yrs})
cost = plan - cf_plan                      # planned costs, held fixed

miss = np.log(h["openai_run_rate_oct2026"] / 70.0)     # October 2026 revision
upg = np.log(1.27)                                       # February 2026 forecast upgrade
s = (abs(miss) + abs(upg)) / 2
m_base = miss / 3

def simulate(m, extra_drag=0.0):
    shocks = rng.normal(m, s, size=(N, len(yrs)))
    shocks[:, 0] = rng.normal(0, s / 4, size=N)          # 2026 is mostly known by October
    drag = np.array([0] + [np.log(1 - extra_drag)] * (len(yrs) - 1))
    dev = np.cumsum(shocks + drag, axis=1)
    rev = plan.values * np.exp(dev)
    cf = rev - cost.values
    cum = np.cumsum(cf, axis=1)
    return rev, cf, cum

def summarise(rev, cf, cum, label):
    r = pd.Series(dtype=float, name=label)
    r["P(2027 revenue >= Oracle 60bn)"] = (rev[:, 1] >= h["oracle_openai_annual"]).mean()
    r["P(2029 revenue >= 175bn)"] = (rev[:, 3] >= 175).mean()
    r["P(2030 revenue >= 175bn)"] = (rev[:, 4] >= 175).mean()
    r["P(cash positive in 2030)"] = (cf[:, 4] > 0).mean()
    r["P(cash needed > 2x the 122bn raised)"] = (-cum.min(axis=1) > 2 * h["openai_raise_mar2026"]).mean()
    r["Median 2030 revenue, bn"] = np.median(rev[:, 4])
    r["Median peak cash need, bn"] = np.median(-cum.min(axis=1))
    r["5th pct 2030 revenue, bn"] = np.percentile(rev[:, 4], 5)
    r["95th pct 2030 revenue, bn"] = np.percentile(rev[:, 4], 95)
    return r

base = simulate(0.0)
cases = pd.concat([summarise(*base, "Central: OpenAI's plan, with its own forecast errors"),
                   summarise(*simulate(m_base), "Pessimistic: plan drifts down by the October gap"),
                   summarise(*simulate(0.0, 0.10), "Central plus prices falling 10pp a year faster")], axis=1)
save_table(cases.round(3), "m11_openai_monte_carlo")
rev = base[0]
pct = pd.DataFrame({p: np.percentile(rev, p, axis=0) for p in (5, 25, 50, 75, 95)}, index=yrs)
save_table(pct.round(1), "m11_revenue_percentiles")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), gridspec_kw={"width_ratios": [1.4, 1]})
ax = axes[0]
ax.fill_between(yrs, pct[5], pct[95], color=BLUE, alpha=0.15, label="90% of paths")
ax.fill_between(yrs, pct[25], pct[75], color=BLUE, alpha=0.3, label="50% of paths")
ax.plot(yrs, pct[50], color=BLUE, lw=2, label="Median path")
ax.plot(plan.index, plan.values, color=INK, ls=":", lw=1.5, label="OpenAI's own plan")
ax.axhline(175, color=RED, ls="--", lw=1.4); ax.text(2026.05, 182, "Commitments: $175bn a year", color=RED, fontsize=8.5)
ax.axhline(h["oracle_openai_annual"], color=ORANGE, ls="--", lw=1.2); ax.text(2026.05, 66, "Oracle: $60bn a year", color=ORANGE, fontsize=8.5)
ax.set_xticks(yrs); ax.set_ylabel("Revenue, USD bn"); ax.legend(fontsize=7.5, loc="upper left", bbox_to_anchor=(0, 0.88))
ax.set_title("20,000 simulated revenue paths", fontsize=11)
ax = axes[1]
labels = ["Covers Oracle\nin 2027", "Reaches $175bn\nby 2029", "Reaches $175bn\nby 2030", "Cash positive\nin 2030"]
keys = ["P(2027 revenue >= Oracle 60bn)", "P(2029 revenue >= 175bn)", "P(2030 revenue >= 175bn)", "P(cash positive in 2030)"]
x = np.arange(4)
for j, (col, c) in enumerate(zip(cases.columns, [BLUE, GREY, RED])):
    ax.bar(x + (j - 1) * 0.26, [cases.loc[k, col] * 100 for k in keys], 0.26, color=c, label=col)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7.2); ax.set_ylabel("% of paths"); ax.set_ylim(0, 100)
ax.legend(fontsize=6.5, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=1); ax.grid(axis="x", visible=False); ax.set_title("How often does OpenAI make it?", fontsize=11)
finish(fig, "Figure 6: Running the probabilities on OpenAI",
       "author's model 11; OpenAI plan and cash flow forecast (The Information via The Decoder); revisions from FT via TechCrunch.",
       "fig11_openai_monte_carlo.png")
with open(TABLES / "m11_summary.txt", "w") as fh:
    fh.write(f"sigma {s:.3f}, drift {m_base:.3f}\nPlanned costs:\n{cost.round(1).to_string()}\n\n{cases.round(3).to_string()}\n\n{pct.round(1).to_string()}\n")
print(open(TABLES / "m11_summary.txt").read())
