"""
MODEL 02  What are investors actually paying for?
1. Tesla's market value today: the 21 July 2026 market cap from FactSet ($1,423bn) gives the
   share count, which is multiplied by the 19 October close.
2. Price to earnings: market value divided by net income over the latest four quarters.
   Toyota's P/E of 10 and net income of $25.45bn (year to March 2026) are from 24/7 Wall St.
3. The profit Tesla would need to justify today's price at a P/E of 25 (a generous multiple for
   a large mature company) and at Toyota's 10, as a multiple of its current profit.
4. The 2025 pay award: the first market value tranche ($2tn) and the final one ($8.5tn)
   against today's value.
"""
from common import *

style(); h = hand()
px = prices()["TSLA"].dropna()
fin = pd.read_csv(DATA / "tesla_financials.csv"); q = fin[fin.period == "quarter"]
shares = h["tsla_mcap_jul21"] / px.loc["2026-07-21"]
mcap = shares * px.iloc[-1]
ni = q.net_income_bn.sum()
pe = mcap / ni
need = {pe_: mcap / pe_ for pe_ in (25, 10)}
toy_mcap = h["toyota_ni_fy26"] * h["toyota_pe"]
res = pd.Series({"tesla_mcap_bn": mcap, "tesla_ttm_net_income_bn": ni, "tesla_pe": pe,
                 "toyota_mcap_bn_approx": toy_mcap, "toyota_net_income_bn": h["toyota_ni_fy26"],
                 "profit_needed_pe25_bn": need[25], "multiple_of_today_pe25": need[25] / ni,
                 "profit_needed_pe10_bn": need[10], "multiple_of_today_pe10": need[10] / ni,
                 "pay_first_tranche_vs_today": h["pay_first_tranche"] / mcap, "pay_final_tranche_vs_today": h["pay_final_tranche"] / mcap})
save_table(res.round(2).to_frame("value"), "m02_valuation")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
x = np.arange(2)
ax.bar(x - 0.2, [mcap, toy_mcap], 0.4, color=[BLUE, GREY], label="Market value")
ax2 = ax.twinx()
ax2.bar(x + 0.2, [ni, h["toyota_ni_fy26"]], 0.4, color=[ORANGE, ORANGE], alpha=0.85, label="Yearly profit")
for i, (m, p) in enumerate(zip([mcap, toy_mcap], [ni, h["toyota_ni_fy26"]])):
    ax.text(i - 0.2, m + 25, f"${m:,.0f}bn", ha="center", fontsize=8.5)
    ax2.text(i + 0.2, p + 0.5, f"${p:.1f}bn", ha="center", fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels([f"Tesla\n(P/E {pe:.0f})", f"Toyota\n(P/E {h['toyota_pe']:.0f})"])
ax.set_ylabel("Market value, USD bn"); ax2.set_ylabel("Net income, last year, USD bn", color=ORANGE)
ax.set_ylim(0, 1700); ax2.set_ylim(0, 34); ax2.spines["right"].set_visible(True); ax2.grid(False); ax.grid(axis="x", visible=False)
ax.set_title("Five times Toyota's value, a seventh of its profit", fontsize=10.5)
ax = axes[1]
lab = ["Profit today", "Needed at\nP/E of 25", "Needed at\nToyota's P/E", "Top profit goal\nin Musk's pay"]
vals = [ni, need[25], need[10], h["pay_profit_top"]]
ax.bar(range(4), vals, color=[ORANGE, BLUE, GREY, VIOLET], width=0.6)
for i, v in enumerate(vals):
    ax.text(i, v + 5, f"${v:,.0f}bn", ha="center", fontsize=8.5)
ax.set_xticks(range(4)); ax.set_xticklabels(lab, fontsize=8); ax.set_ylabel("Yearly profit, USD bn")
ax.set_ylim(0, 460); ax.grid(axis="x", visible=False); ax.set_title("The profit the price assumes", fontsize=10.5)
finish(fig, "Figure 2: Investors are paying for the future, not for the car company",
       "author's model 02; Nasdaq via OpenBB; FactSet via WSJ and 24/7 Wall St (Jul 2026); CBT News (Nov 2025).", "fig02_valuation.png")
print(res.round(2))
