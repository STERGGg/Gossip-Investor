"""
MODEL 05  The promise tracker
For five of Musk's best documented promises, the year he made it, the year he promised and
the year it was delivered (or is now expected), from 03 Data/promise_tracker.csv, where each
row carries its source. Delay = delivery year minus promised year. For the Roadster the
delivery year is the planned 2028 start of production; for humans on Mars the bar runs to
2031, the earliest year implied by Musk's February 2026 statement of a Mars city in five to
seven years, and is shown as open ended. The uncrewed Mars bar runs to 2029, the next Mars launch window after late 2026.
"""
from common import *

style()
d = pd.read_csv(DATA / "promise_tracker.csv")
d["end"] = d.year_delivered
d.loc[d.promise == "Humans on Mars", "end"] = 2031
d.loc[d.promise == "Uncrewed Starship to Mars", "end"] = 2029
d["delay_years"] = d.end - d.year_promised
save_table(d[["promise", "year_made", "year_promised", "year_delivered", "delay_years", "status"]], "m05_promises")
fig, ax = plt.subplots(figsize=(11, 4.2))
y = np.arange(len(d))[::-1]
for yi, (_, r) in zip(y, d.iterrows()):
    ax.plot([r.year_made, r.year_promised], [yi, yi], color=GREY, lw=6, solid_capstyle="butt")
    open_end = pd.isna(r.year_delivered) or r.promise == "New Roadster"
    ax.plot([r.year_promised, r.end], [yi, yi], color=RED if open_end else ORANGE, lw=6, solid_capstyle="butt", alpha=0.55 if open_end else 1)
    ax.scatter([r.year_promised], [yi], color=INK, zorder=3, s=25)
    if not pd.isna(r.year_delivered) and r.promise != "New Roadster":
        ax.scatter([r.end], [yi], color=GREEN, zorder=3, s=45, marker="D")
    ax.text(r.end + 0.4, yi, f"{r.status} ({r.delay_years:.0f}+ yrs late)" if open_end else f"{r.status} ({r.delay_years:.0f} yrs late)", va="center", fontsize=8)
ax.set_yticks(y); ax.set_yticklabels(d.promise, fontsize=9)
ax.set_xlim(2016, 2042); ax.set_xticks(range(2016, 2034, 2)); ax.grid(axis="y", visible=False)
ax.axvline(2026.8, color=INK2, ls=":", lw=1); ax.text(2026.9, y.max() + 0.45, "Today", fontsize=8, color=INK2)
ax.set_xlabel("Grey: from promise to deadline. Orange: late but delivered (green diamond). Faded red: still waiting.", fontsize=8)
finish(fig, "Figure 5: Musk's promises usually arrive, just years late",
       "author's model 05; CNN (2019), The Drive (2023), TechCrunch, Fortune, NBC News and TIKR (2026).", "fig05_promise_tracker.png")
print(d[["promise", "year_promised", "end", "delay_years"]])
