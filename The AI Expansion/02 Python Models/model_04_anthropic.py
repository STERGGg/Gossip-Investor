"""
MODEL 04  How is Anthropic meant to make money if anyone can cancel?
1. Quarterly revenue 2026 rebuilt from the reported Q3 figure (16.8bn) and growth rates
   (Q1 to Q2 +140%, Q2 to Q3 +50%): Q2 = Q3 / 1.5, Q1 = Q2 / 2.4.
2. Annualised run rate = Q3 x 4, and the multiple implied by a reported 2tn IPO valuation.
3. Illustration of what the valuation asks for: years of growth needed for revenue to reach
   valuation / 10 (ten times sales, an illustrative mature software multiple) at constant
   valuation, for annual growth of 25%, 50% and 100%: years = ln(target / run rate) / ln(1 + g).
4. Who pays: estimated share of revenue from business and API customers against consumer
   subscriptions for Anthropic and OpenAI (author estimates from Arcade.dev, flagged as such).
"""
from common import *
import math

style(); h = hand()
q3 = h["anthropic_q3_revenue"]; q2 = q3 / (1 + 0.5); q1 = q2 / (1 + h["anthropic_q1q2_growth"] / 100)
q = pd.Series({"Q1 2026": q1, "Q2 2026": q2, "Q3 2026": q3})
run = q3 * 4; val = h["anthropic_ipo_val"]; mult = val / run
target = val / 10
yrs = {f"{int(g*100)}% a year": math.log(target / run) / math.log(1 + g) for g in (0.25, 0.5, 1.0)}
save_table(pd.DataFrame({"revenue_usd_bn": q.round(2)}), "m04_anthropic_quarters")
mix = pd.DataFrame({"Business and API": [h["anthropic_api_share_est"], 100 - h["openai_consumer_share_est"]],
                    "Consumer subscriptions": [100 - h["anthropic_api_share_est"], h["openai_consumer_share_est"]]}, index=["Anthropic", "OpenAI"])

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
ax.bar(q.index, q.values, color=[GREY, GREY, BLUE], width=0.6)
for i, v in enumerate(q.values):
    ax.text(i, v + 0.3, f"${v:.1f}bn", ha="center", fontsize=9)
ax.set_ylabel("Revenue per quarter, USD bn"); ax.grid(axis="x", visible=False)
ax.set_title(f"Quarterly revenue (run rate ${run:.0f}bn, IPO at {mult:.0f}x)", fontsize=10.5)
ax = axes[1]
left = np.zeros(2)
for col, c in zip(mix.columns, [BLUE, ORANGE]):
    ax.barh(mix.index, mix[col], left=left, color=c, label=col, height=0.5)
    for i, v in enumerate(mix[col]):
        ax.text(left[i] + v / 2, i, f"{v:.0f}%", ha="center", va="center", color="white", fontsize=10, fontweight="bold")
    left += mix[col].values
ax.set_xlim(0, 100); ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2); ax.grid(axis="y", visible=False)
ax.set_title("Who pays (estimated share of revenue)", fontsize=10.5)
finish(fig, "Figure 7: Anthropic sells mostly to businesses, which do not cancel on a whim",
       "author's model 04; FT via Motley Fool (Q3 2026 revenue and growth); revenue mix estimates from Arcade.dev (unsourced, indicative only).",
       "fig04_anthropic.png")
with open(TABLES / "m04_summary.txt", "w") as fh:
    fh.write(q.round(2).to_string() + f"\nRun rate {run:.1f}bn; valuation {val:.0f}bn = {mult:.1f}x run rate\n")
    fh.write(f"Target revenue at 10x: {target:.0f}bn. Years needed: " + ", ".join(f"{k}: {v:.1f}" for k, v in yrs.items()) + "\n")
print(open(TABLES / "m04_summary.txt").read())
