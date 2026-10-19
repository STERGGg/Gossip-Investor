"""
MODEL 05  Private capital: why France cannot do what Greece did in 2012

In March 2012 Greece cut its debt through Private Sector Involvement (PSI):
private bondholders took a 53.5% haircut on EUR 198bn of bonds, wiping out EUR
106bn (figures from the ESM, as used in my EPQ). This model asks what the same
tool would mean for France, and how dependent France is on foreign private
buyers each year.

Calculations
    non resident holdings = negotiable debt (AFT, Jul 2026) x non resident share (BdF, Q1 2026)
    resident holdings     = negotiable debt - non resident holdings
    Greek style haircut   = 53.5% x holdings, expressed in EUR and % of 2026 GDP
    foreign demand needed = 2026 and 2027 programmes x non resident share
    Greece: EUR 106bn of relief, equal to about 54% of Greek GDP (ESM, as cited in the EPQ)
"""
from common import *

style()
h = hand(); w = weo()
gdp26 = w["NGDP_FRA"].loc[2026]
neg = h["negotiable_debt_jul2026"]; nr = h["nonresident_share"] / 100
hc = h["greece_psi_haircut"] / 100

nonres = neg * nr; res = neg - nonres
rows = {
    "Negotiable state debt (EUR bn)": neg,
    "Held by non residents (EUR bn)": nonres,
    "Held by residents: French banks, insurers, funds (EUR bn)": res,
    "Greek style 53.5% haircut on non resident holdings (EUR bn)": hc * nonres,
    "Haircut on non resident holdings, % of 2026 GDP": hc * nonres / gdp26 * 100,
    "Loss to French resident holders if applied to all bonds (EUR bn)": hc * res,
    "Loss to resident holders, % of 2026 GDP": hc * res / gdp26 * 100,
    "Foreign buying needed each year at 2026 programme (EUR bn)": h["aft_programme_2026"] * nr,
    "Foreign buying needed at 2027 programme (EUR bn)": h["aft_programme_2027"] * nr,
    "Greece 2012 PSI relief (EUR bn)": h["greece_psi_relief"],
}
t = pd.Series(rows).round(1)
save_table(t.to_frame("value"), "m05_psi_comparison")

fig, ax = plt.subplots(figsize=(7.5, 3.6))
labels = ["Greece 2012\nPSI relief", "France: haircut on\nforeign holders", "France: loss pushed onto\nFrench savers and banks"]
vals = [h["greece_psi_relief"], hc * nonres, hc * res]
ax.bar(labels, vals, color=[RED, BLUE, VIOLET], width=0.55)
for i, v in enumerate(vals):
    ax.text(i, v + 15, f"EUR {v:,.0f}bn", ha="center", fontsize=9)
ax.set_ylabel("EUR billion"); ax.set_ylim(0, max(vals) * 1.18)
ax.set_title("Figure 11: A Greek style PSI in France would be eight times larger")
source_note(fig, "Author's model 05: AFT Bulletin 435, Banque de France, ESM, IMF WEO.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig08_psi_comparison.png"); plt.close(fig)

with open(TABLES / "m05_summary.txt", "w") as fh:
    fh.write(t.to_string() + f"\nRatio France foreign haircut to Greek relief: {hc*nonres/h['greece_psi_relief']:.1f}x\n")
print(open(TABLES / "m05_summary.txt").read())

# ---------- Appendix figure A5: who owns French debt and who would lose ----------
fig, ax = plt.subplots(figsize=(9, 2.9))
ax.barh([1], [nonres], color=BLUE, height=0.5, label="Held by non residents")
ax.barh([1], [res], left=[nonres], color=VIOLET, height=0.5, label="Held by French residents")
ax.barh([0], [hc * nonres], color="#8db7ea", height=0.5, label="53.5% haircut, foreign holders")
ax.barh([0], [hc * res], left=[nonres], color="#b3abef", height=0.5, label="53.5% haircut, French holders")
ax.barh([-1], [h["greece_psi_relief"]], color=RED, height=0.5, label="Greek PSI 2012")
for y_, v, x0 in [(1, nonres, 0), (1, res, nonres), (0, hc * nonres, 0), (0, hc * res, nonres), (-1, h["greece_psi_relief"], 0)]:
    if v > 300:
        ax.text(x0 + v / 2, y_, f"EUR {v:,.0f}bn", ha="center", va="center", fontsize=8.5, color="white")
    else:
        ax.text(x0 + v + 25, y_, f"EUR {v:,.0f}bn", ha="left", va="center", fontsize=8.5, color=INK)
ax.set_yticks([1, 0, -1]); ax.set_yticklabels(["Negotiable debt", "Greek style loss", "Greece"])
ax.set_xlabel("EUR billion"); ax.legend(fontsize=7.5, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.32))
ax.grid(axis="y", visible=False)
ax.set_title("Figure 12: Model 05, who owns French debt and who would lose")
source_note(fig, "Author's model 05: AFT Bulletin 435, Banque de France (non resident share Q1 2026), ESM.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "figA5_model05_ownership.png"); plt.close(fig)
