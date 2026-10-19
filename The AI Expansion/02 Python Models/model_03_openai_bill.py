"""
MODEL 03  Can OpenAI pay its bills?
1. Annual value of OpenAI's commitments: 1.4tn over 8 years (Altman, Nov 2025) = 175bn a year
   on a straight line, against the Oracle contract alone (about 60bn a year from 2027).
2. Revenue: 2025 actual (13.1bn), the October 2026 run rate (50bn), and OpenAI's own internal
   plan (30bn 2026, 62bn 2027, 282.5bn 2030; 2028 and 2029 interpolated geometrically
   between 2027 and 2030, labelled as such).
3. Cash: OpenAI's own cash flow forecast 2024 to 2030 and the cumulative burn, against the
   122bn raised in March 2026.
4. Growth needed: compound annual growth to take the 50bn run rate to the 175bn yearly bill.
"""
from common import *

style(); h = hand()
yrs = list(range(2024, 2031))
cf = pd.Series({y: h[f"openai_cf_{y}"] for y in yrs})
cum = cf.cumsum()
plan = pd.Series({2025: h["openai_rev_2025"], 2026: h["openai_rev_2026_plan"], 2027: h["openai_rev_2027_plan"], 2030: h["openai_rev_2030_plan"]})
g = (plan[2030] / plan[2027]) ** (1 / 3)
plan[2028] = plan[2027] * g; plan[2029] = plan[2027] * g ** 2; plan = plan.sort_index()
annual_commit = h["openai_commitments"] / h["openai_commit_years"]
need_cagr = {n: (annual_commit / h["openai_run_rate_oct2026"]) ** (1 / n) - 1 for n in (2, 3, 4)}
save_table(pd.DataFrame({"revenue_plan": plan, "cash_flow": cf, "cumulative_cash_flow": cum}).round(1), "m03_openai")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
ax = axes[0]
ax.plot(plan.index, plan.values, marker="o", color=BLUE, label="OpenAI revenue: 2025 actual, then its own plan")
ax.scatter([2026.8], [h["openai_run_rate_oct2026"]], color=INK, zorder=5, label="Run rate told to investors, Oct 2026")
ax.axhline(annual_commit, color=RED, ls="--", lw=1.6); ax.text(2024.9, annual_commit + 6, f"Commitments: ${annual_commit:.0f}bn a year", color=RED, fontsize=8.5)
ax.axhline(h["oracle_openai_annual"], color=ORANGE, ls=":", lw=1.6); ax.text(2024.9, h["oracle_openai_annual"] + 6, "Oracle contract alone: about $60bn a year", color=ORANGE, fontsize=8.5)
ax.set_ylabel("USD bn"); ax.legend(fontsize=7.5, loc="upper left", bbox_to_anchor=(0, 0.85)); ax.set_title("Revenue against the yearly bill", fontsize=11)
ax.annotate("2028 and 2029\ninterpolated", (2028.5, plan[2028] * 1.1), fontsize=7.5, color=INK2)
ax = axes[1]
ax.bar(cf.index, cf.values, color=[RED if v < 0 else AQUA for v in cf.values])
ax.plot(cum.index, cum.values, color=INK, marker="o", label="Cumulative cash flow")
ax.axhline(-h["openai_raise_mar2026"], color=VIOLET, ls="--", lw=1.4); ax.text(2024, -h["openai_raise_mar2026"] - 14, "$122bn raised in March 2026", color=VIOLET, fontsize=8.5)
ax.set_ylabel("USD bn"); ax.legend(fontsize=8, loc="lower left"); ax.set_title("OpenAI's own cash flow forecast", fontsize=11)
finish(fig, "Figure 5: OpenAI's promises are bigger than its sales, and it says so itself",
       "author's model 03; Altman via TechCrunch (Nov 2025), OpenAI internal forecasts via The Information/The Decoder (Feb 2026), FT via TechCrunch (Oct 2026).",
       "fig03_openai_bill.png")
with open(TABLES / "m03_summary.txt", "w") as fh:
    fh.write(f"Annual commitments {annual_commit:.0f}bn vs run rate {h['openai_run_rate_oct2026']:.0f}bn ({annual_commit/h['openai_run_rate_oct2026']:.1f}x)\n")
    fh.write("Growth needed to reach 175bn: " + ", ".join(f"{n}y {v*100:.0f}% a year" for n, v in need_cagr.items()) + "\n")
    fh.write(f"Cumulative burn to 2029: {cum[2029]:.0f}bn; trough {cum.min():.0f}bn vs raised {h['openai_raise_mar2026']:.0f}bn\n")
    fh.write(f"Oracle 60bn vs run rate 50bn: {h['oracle_openai_annual']/h['openai_run_rate_oct2026']*100:.0f}%\n" + plan.round(1).to_string() + "\n")
print(open(TABLES / "m03_summary.txt").read())
