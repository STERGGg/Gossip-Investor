"""
MODEL 02  The revenue gap: how one year of building compares with the money AI earns
1. 2026 capex of Amazon, Microsoft, Alphabet and Meta: sum of company guidance (midpoints).
2. What that one year of building costs each year in depreciation, at the longest server lives in use (6 years) and Meta's
   5.5 years, and at a stricter 3 years that critics argue
   matches how fast AI chips age. Depreciation = capex / useful life (straight line).
3. Revenue of the two leading model companies: OpenAI's run rate told to investors and
   Anthropic's Q3 2026 revenue times four. This is the money end customers pay for frontier
   models, much of which is then paid on to the clouds.
4. The gap: depreciation of 2026 capex alone divided by that revenue.
"""
from common import *

style(); h = hand()
capex = pd.Series({"Amazon": h["capex_2026_amzn"], "Alphabet": h["capex_2026_googl"],
                   "Microsoft": h["capex_2026_msft"], "Meta": h["capex_2026_meta"]})
C = capex.sum()
lives = {"6 years (longest in use)": 6, "5.5 years (Meta)": 5.5, "3 years (critics)": 3}
dep = pd.Series({k: C / v for k, v in lives.items()})
lab = pd.Series({"OpenAI run rate (Oct 2026)": h["openai_run_rate_oct2026"],
                 "Anthropic Q3 2026 x 4": h["anthropic_q3_revenue"] * 4})
L = lab.sum()
tab = pd.DataFrame({"eur": None}, index=[]).drop(columns="eur")
out = pd.concat([capex.rename("usd_bn"), pd.Series({"Total 2026 capex": C}, name="usd_bn"),
                 dep.rename("usd_bn"), lab.rename("usd_bn"), pd.Series({"Two labs combined": L}, name="usd_bn")])
save_table(out.round(1).to_frame(), "m02_revenue_gap")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios": [1, 1.25]})
ax = axes[0]
ax.bar(capex.index, capex.values, color=[ORANGE, VIOLET, BLUE, AQUA])
for i, v in enumerate(capex.values):
    ax.text(i, v + 4, f"${v:.0f}bn", ha="center", fontsize=9)
ax.set_ylabel("2026 capital spending, USD bn"); ax.grid(axis="x", visible=False)
ax.set_title(f"Four companies, one year: ${C:.0f}bn", fontsize=11)
ax = axes[1]
names = list(dep.index) + ["OpenAI + Anthropic revenue"]
vals = list(dep.values) + [L]
cols = [GREY, GREY, RED, BLUE]
ax.barh(names[::-1], vals[::-1], color=cols[::-1])
for i, v in enumerate(vals[::-1]):
    ax.text(v + 2, i, f"${v:.0f}bn", va="center", fontsize=9)
ax.set_xlabel("USD bn per year"); ax.grid(axis="y", visible=False); ax.set_xlim(0, max(vals) * 1.2)
ax.set_title("Yearly cost of 2026 capex vs lab revenue", fontsize=11)
finish(fig, "Figure 2: The bill for one year of building is bigger than the industry's sales",
       "author's model 02; company capex guidance (Yield Theory tracker), OpenAI (FT via TechCrunch), Anthropic (FT via Motley Fool).",
       "fig02_revenue_gap.png")
with open(TABLES / "m02_summary.txt", "w") as fh:
    fh.write(out.round(1).to_string() + f"\n\nCapex / lab revenue: {C/L:.1f}x; 6y depreciation / lab revenue: {dep.iloc[0]/L:.2f}x; 3y: {dep.iloc[2]/L:.2f}x\n")
print(open(TABLES / "m02_summary.txt").read())
