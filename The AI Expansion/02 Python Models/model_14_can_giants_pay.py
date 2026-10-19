"""
MODEL 14  Can even the giants pay for it from cash?
1. Data: quarterly and annual cash flow statements from Nasdaq (via OpenBB) for Microsoft,
   Alphabet, Amazon, Meta and Oracle, stored in 03 Data/hyperscaler_cash_flows.csv (USD bn).
2. Capex coverage: capital expenditure as a share of operating cash flow, for the 2023
   financial year and for the latest four quarters (to June 2026, or August 2026 for Oracle).
   Above 100% means the company is spending more on building than its business brings in.
3. Borrowing: net debt issuance over the latest four quarters.
4. The four hyperscalers' 2026 capex guidance (Model 02) against their combined operating
   cash flow over the latest four quarters.
"""
from common import *

style(); h = hand()
cf = pd.read_csv(DATA / "hyperscaler_cash_flows.csv")
names = {"MSFT": "Microsoft", "GOOGL": "Alphabet", "AMZN": "Amazon", "META": "Meta", "ORCL": "Oracle"}
q = cf[cf.period == "quarter"].groupby("symbol")[["operating_cash_flow_bn", "capex_bn", "net_debt_issuance_bn"]].sum()
a23 = cf[(cf.period == "annual") & cf.period_ending.str.startswith("2023")].set_index("symbol")
t = pd.DataFrame({
    "capex_pct_ocf_2023": a23.capex_bn / a23.operating_cash_flow_bn * 100,
    "capex_pct_ocf_ttm": q.capex_bn / q.operating_cash_flow_bn * 100,
    "ocf_ttm_bn": q.operating_cash_flow_bn, "capex_ttm_bn": q.capex_bn,
    "net_debt_ttm_bn": q.net_debt_issuance_bn}).loc[list(names)]
big4 = ["MSFT", "GOOGL", "AMZN", "META"]
tot = {
    "big4_ocf_ttm": t.loc[big4, "ocf_ttm_bn"].sum(), "big4_capex_ttm": t.loc[big4, "capex_ttm_bn"].sum(),
    "big4_net_debt_ttm": t.loc[big4, "net_debt_ttm_bn"].sum(),
    "big4_capex_pct_2023": a23.loc[big4, "capex_bn"].sum() / a23.loc[big4, "operating_cash_flow_bn"].sum() * 100,
    "capex_2026_guidance": sum(h[f"capex_2026_{s.lower()}"] for s in big4)}
tot["big4_capex_pct_ttm"] = tot["big4_capex_ttm"] / tot["big4_ocf_ttm"] * 100
tot["guidance_pct_ocf"] = tot["capex_2026_guidance"] / tot["big4_ocf_ttm"] * 100
save_table(t.round(1), "m14_capex_coverage")
save_table(pd.Series(tot).round(1).to_frame("value"), "m14_totals")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axes[0]
x = np.arange(len(names))
ax.bar(x - 0.2, t.capex_pct_ocf_2023, 0.4, color=GREY, label="2023 financial year")
ax.bar(x + 0.2, t.capex_pct_ocf_ttm, 0.4, color=[RED if v > 100 else BLUE for v in t.capex_pct_ocf_ttm], label="Latest four quarters")
for i, v in enumerate(t.capex_pct_ocf_ttm):
    ax.text(i + 0.2, v + 3, f"{v:.0f}%", ha="center", fontsize=8.5)
ax.axhline(100, color=INK2, ls="--", lw=1); ax.text(-0.45, 104, "Spending all of its cash", fontsize=8, color=INK2)
ax.set_xticks(x); ax.set_xticklabels(names.values()); ax.set_ylabel("Capex as % of operating cash flow")
ax.set_ylim(0, 185); ax.grid(axis="x", visible=False); ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(0, 0.92))
ax.set_title("Capex is eating the cash", fontsize=11)
ax = axes[1]
vals = t.net_debt_ttm_bn
ax.barh(list(names.values())[::-1], vals.values[::-1], color=[RED if n == "ORCL" else ORANGE for n in vals.index[::-1]])
for i, v in enumerate(vals.values[::-1]):
    ax.text(max(v, 0) + 1.5, i, (f"${v:.0f}bn" if v >= 0 else f"repaid ${-v:.0f}bn"), va="center", fontsize=8.5)
ax.axvline(0, color=INK2, lw=0.8); ax.set_xlim(-10, 95); ax.set_xlabel("Net new debt, latest four quarters, USD bn")
ax.grid(axis="y", visible=False); ax.set_title("And they are borrowing", fontsize=11)
finish(fig, "Figure 3: Even the cash rich giants are now borrowing to build",
       "author's model 14; company cash flow statements from Nasdaq via OpenBB (four quarters to Jun 2026, Oracle to Aug 2026).",
       "fig14_can_giants_pay.png")
print(t.round(1)); print({k: round(v, 1) for k, v in tot.items()})
