"""
MODEL 10  Who is winning: the picks and shovels of power
Nasdaq daily closes via OpenBB, rebased to 100 on the first trading day of 2025 (Nebius from
its first price in the data), for companies selling the physical inputs to AI: Vertiv (power
and cooling equipment for data centres), Constellation Energy (the largest US nuclear
operator), Freeport McMoRan (copper), AMD and Nvidia (chips), against the borrowers
(Oracle, CoreWeave) and the S&P 500. Total change to 16 October 2026 is reported for each.
"""
from common import *

style(); px = prices()
names = {"VRT": "Vertiv (power and cooling)", "CEG": "Constellation (nuclear power)", "FCX": "Freeport (copper)",
         "NVDA": "Nvidia (chips)", "AMD": "AMD (chips)", "NBIS": "Nebius (AI cloud)", "SPY": "S&P 500",
         "ORCL": "Oracle", "CRWV": "CoreWeave"}
start = "2025-01-02"
chg = {}
for t in names:
    s = px[t].dropna().loc[start:]
    chg[t] = (s.iloc[-1] / s.iloc[0] - 1) * 100
chg = pd.Series(chg).sort_values()
save_table(chg.round(1).to_frame("pct_change_since_2025"), "m10_picks_and_shovels")
fig, ax = plt.subplots(figsize=(10, 4.6))
cols = [RED if t in ("ORCL", "CRWV") else (GREY if t == "SPY" else (ORANGE if t in ("VRT", "CEG", "FCX") else BLUE)) for t in chg.index]
ax.barh([names[t] for t in chg.index], chg.values, color=cols)
for i, v in enumerate(chg.values):
    ax.text(v + (3 if v >= 0 else -3), i, f"{v:+.0f}%", va="center", ha="left" if v >= 0 else "right", fontsize=9)
ax.axvline(0, color=INK2, lw=0.8); ax.grid(axis="y", visible=False)
ax.set_xlim(min(chg.min() * 1.4, -80), chg.max() * 1.25); ax.set_xlabel("Share price change, 2 Jan 2025 to 16 Oct 2026 (CoreWeave and Nebius from first price in 2025)")
ax.set_title("Orange: power and metal. Blue: chips and clouds. Red: the borrowers", fontsize=10.5)
finish(fig, "Figure 12: The AI trade has split, with suppliers up and the borrowers down",
       "author's model 10; Nasdaq daily closes via OpenBB.", "fig10_picks_and_shovels.png")
print(chg.round(1))
