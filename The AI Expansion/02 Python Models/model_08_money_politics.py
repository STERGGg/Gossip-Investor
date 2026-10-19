"""
MODEL 08  Where the money goes: politics and the rest of the world
1. AI industry political spending in the 2026 US midterms by group (reported figures).
2. Scale: the four hyperscalers' 2026 capex against the US federal interest bill
   (about 1tn a year, Bloomberg) and OpenAI's 1.4tn of commitments.
"""
from common import *

style(); h = hand()
pol = pd.Series({"Leading the Future\n(a16z, Greg Brockman)": h["ltf_raised"], "Innovation Council Action": h["innovation_council"],
                 "Public First Action\n(Anthropic seeded $20m)": h["public_first"], "Meta": h["meta_politics"]}).sort_values()
capex = h["capex_2026_amzn"] + h["capex_2026_msft"] + h["capex_2026_googl"] + h["capex_2026_meta"]
scale = pd.Series({"Hyperscaler capex, 2026": capex, "US federal interest bill, a year": h["us_interest_bill"], "OpenAI commitments, 8 years": h["openai_commitments"]})
save_table(pol.to_frame("usd_m"), "m08_politics"); save_table(scale.to_frame("usd_bn"), "m08_scale")
fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ax = axes[0]
ax.barh(pol.index, pol.values, color=[BLUE, VIOLET, ORANGE, RED])
for i, v in enumerate(pol.values):
    ax.text(v + 2, i, f"${v:.0f}m+", va="center", fontsize=9)
ax.set_xlim(0, pol.max() * 1.3); ax.set_xlabel("USD million"); ax.grid(axis="y", visible=False)
ax.set_title(f"AI money in the 2026 midterms: over ${h['ai_politics_total']:.0f}m", fontsize=11)
ax = axes[1]
ax.bar(range(3), scale.values, color=[BLUE, GREY, RED], width=0.6)
ax.set_xticks(range(3)); ax.set_xticklabels([s.replace(", ", "\n") for s in scale.index], fontsize=8.5)
for i, v in enumerate(scale.values):
    ax.text(i, v + 20, f"${v:,.0f}bn", ha="center", fontsize=9)
ax.set_ylabel("USD bn"); ax.grid(axis="x", visible=False); ax.set_title("The scale of the bet", fontsize=11)
finish(fig, "Figure 15: The money is now big enough to move elections and bond markets",
       "author's model 08; Tech Times (9 Oct 2026); Bloomberg Originals (Oct 2026); company guidance; TechCrunch.", "fig08_money_politics.png")
print(pol, scale)
