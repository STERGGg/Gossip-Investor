"""
MODEL 07  Is anyone actually more productive, and what about jobs?
1. US labour productivity, nonfarm business, change on a year earlier (BLS via OpenBB),
   quarterly. Averages for the years before Covid (2016 to 2019) and since ChatGPT (2023 Q1
   to the latest quarter).
2. The range of academic estimates of AI's total effect on productivity over a decade
   (compiled by Apollo), against the time saving workers report (St Louis Fed via Apollo).
3. Young workers: employment change of 22 to 25 year olds in the most and least AI exposed
   jobs, November 2022 to June 2026 (Brynjolfsson, Chandar and Chen, Stanford, ADP payroll data).
"""
from common import *

style(); h = hand()
p = pd.read_csv(DATA / "bls_productivity_nonfarm.csv", parse_dates=["date"]).set_index("date")["change_from_year_ago"]
pre = p.loc["2016":"2019"].mean(); post = p.loc["2023":].mean()
save_table(pd.Series({"avg_2016_2019": pre, "avg_2023_latest": post, "latest": p.iloc[-1]}).round(2).to_frame("pct"), "m07_productivity")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axes[0]
ax.bar(p.index, p.values, width=60, color=[BLUE if d >= pd.Timestamp("2023-01-01") else GREY for d in p.index])
ax.hlines(pre, pd.Timestamp("2016-01-01"), pd.Timestamp("2019-12-31"), color=INK, lw=2); ax.text(pd.Timestamp("2016-02-01"), pre + 0.4, f"2016 to 2019: {pre:.1f}%", fontsize=8.5)
ax.hlines(post, pd.Timestamp("2023-01-01"), p.index[-1], color=BLUE, lw=2); ax.text(pd.Timestamp("2022-10-01"), 5.2, f"Since 2023: {post:.1f}%", fontsize=8.5, color=BLUE)
ax.axhline(0, color=GREY, lw=0.8); ax.set_ylabel("% change on a year earlier"); ax.set_title("US labour productivity", fontsize=11)
ax = axes[1]
v = pd.Series({"Least exposed jobs": h["canaries_least_change"], "Most exposed jobs": h["canaries_exposed_change"]})
ax.bar(v.index, v.values, color=[AQUA, RED], width=0.55)
for i, x in enumerate(v.values):
    ax.text(i, x / 2, f"{x:+.0f}%", ha="center", va="center", fontsize=11, fontweight="bold", color="white")
ax.axhline(0, color=GREY, lw=0.8); ax.set_ylabel("Employment change, Nov 2022 to Jun 2026"); ax.grid(axis="x", visible=False)
ax.set_title("Workers aged 22 to 25", fontsize=11)
finish(fig, "Figure 13: Productivity is up a little; young workers in exposed jobs are down a lot",
       "author's model 07; BLS Productivity and Costs via OpenBB; Brynjolfsson, Chandar and Chen (Stanford, Aug 2026), ADP data.",
       "fig07_productivity_jobs.png")
print(f"pre {pre:.2f} post {post:.2f} latest {p.iloc[-1]} ({p.index[-1].date()}) first {p.index[0].date()}")
