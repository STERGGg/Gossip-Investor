"""
MODEL 13  Am I exposed without knowing it?
1. Concentration: the top 10 companies' share of the S&P 500 in July 2026 (38%, JP Morgan)
   against the top 10's share of the MSCI USA index at the June 2000 peak (33.2%, Bloomberg).
   The indices differ slightly, so the comparison is indicative.
2. What 100 pounds or dollars in an S&P 500 tracker holds: 38 in ten companies, 62 in the
   other 490.
3. Simple stress test: the fall in the whole index if the top 10 fell by 25%, 50% or 83%
   (the Nasdaq 100's fall after March 2000, Model 05) and the other 490 did not move:
   index fall = top 10 weight x fall. This ignores knock on effects, which would make it worse.
"""
from common import *

style(); h = hand()
w = h["top10_sp500_jul2026"] / 100
falls = {"Top 10 fall 25%": 0.25, "Top 10 fall 50%": 0.5, "Top 10 fall 83%\n(Nasdaq 100 after 2000)": 0.83}
hit = pd.Series({k: -w * v * 100 for k, v in falls.items()})
save_table(hit.round(1).to_frame("index_change_pct"), "m13_stress")
fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ax = axes[0]
ax.bar(["Top 10, MSCI USA\nJune 2000", "Top 10, S&P 500\nJuly 2026"], [h["top10_msci_usa_2000"], h["top10_sp500_jul2026"]], color=[GREY, BLUE], width=0.55)
for i, v in enumerate([h["top10_msci_usa_2000"], h["top10_sp500_jul2026"]]):
    ax.text(i, v + 0.8, f"{v:.1f}%", ha="center", fontsize=10)
ax.set_ylabel("% of the index"); ax.set_ylim(0, 48); ax.grid(axis="x", visible=False)
ax.set_title("More concentrated than at the dot com peak", fontsize=11)
ax = axes[1]
ax.bar(range(3), hit.values, color=[YELLOW, ORANGE, RED], width=0.55)
ax.set_xticks(range(3)); ax.set_xticklabels(hit.index, fontsize=8.5)
for i, v in enumerate(hit.values):
    ax.text(i, v / 2, f"{v:.0f}%", ha="center", va="center", fontsize=11, fontweight="bold", color="white")
ax.axhline(0, color=INK2, lw=0.8); ax.set_ylabel("Change in the whole S&P 500, %"); ax.grid(axis="x", visible=False)
ax.set_title("If only the top 10 fell", fontsize=11)
finish(fig, "Figure 10: Your pension is already an AI bet",
       "author's model 13; JP Morgan via Landmark Wealth (Jul 2026); Bloomberg via Nasdaq/Benzinga (MSCI USA 2000).", "fig13_your_pension.png")
print(hit.round(1))
