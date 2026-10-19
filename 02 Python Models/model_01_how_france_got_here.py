"""
MODEL 01  How France got here
Fiscal history of France against its neighbours using the IMF World Economic Outlook.

What it calculates
1. Debt to GDP paths 1995 to 2031 for France, Germany, Italy, Spain and Greece.
2. The number of IMF years (1995 onwards) in which France ran a surplus.
3. A decomposition of the change in the deficit between two years into the part
   explained by revenue and the part explained by spending (both % of GDP).
       change in balance = change in revenue ratio - change in spending ratio
4. Interest paid as % of GDP, computed as primary balance minus overall balance,
   because overall balance = primary balance - interest.
5. The effective interest rate on the debt stock and nominal GDP growth, and from
   them the primary balance that would hold the debt ratio flat:
       pb* = d(t-1) x (r - g) / (1 + g)
   where d is debt/GDP, r the effective rate, g nominal growth.
"""
from common import *

style()
w = weo()
debt, bal, pb = w["GGXWDG_NGDP"], w["GGXCNL_NGDP"], w["GGXONLB_NGDP"]
rev, spend, growth = w["GGR_NGDP"], w["GGX_NGDP"], w["NGDP_RPCH"]
ngdp = w["NGDP_FRA"]

# 1 Debt paths chart
fig, ax = plt.subplots(figsize=(8, 4.4))
for c in ["GRC", "ITA", "FRA", "ESP", "DEU"]:
    s = debt[c].loc[1995:2031]
    hist = s.loc[:2025]; proj = s.loc[2025:]
    lw = 2.6 if c == "FRA" else 1.6
    ax.plot(hist.index, hist.values, color=COUNTRY_COL[c], lw=lw, label=NAMES[c])
    ax.plot(proj.index, proj.values, color=COUNTRY_COL[c], lw=lw, ls=(0, (3, 2)))
    ax.text(2031.4, s.loc[2031], NAMES[c], color=COUNTRY_COL[c], va="center", fontsize=9)
ax.axvspan(2025.5, 2031.5, color="#f1efe9", zorder=0)
ax.text(2026, 205, "IMF projection", fontsize=8, color=INK2)
ax.set_xlim(1995, 2034); ax.set_ylabel("General government gross debt, % of GDP")
ax.set_title("Figure 1: France has climbed into the high debt group")
ax.legend(loc="upper left", ncol=5, fontsize=8)
source_note(fig, "IMF World Economic Outlook database (retrieved 19 Oct 2026). Dashed = IMF projection.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig01_debt_paths.png"); plt.close(fig)

# 2 Surplus years
fr_bal = bal["FRA"].loc[1995:2025]
surplus_years = fr_bal[fr_bal >= 0].index.tolist()

# 3 Decomposition of the deficit change
def decompose(y0, y1):
    d_rev = rev.loc[y1, "FRA"] - rev.loc[y0, "FRA"]
    d_sp = spend.loc[y1, "FRA"] - spend.loc[y0, "FRA"]
    d_bal = bal.loc[y1, "FRA"] - bal.loc[y0, "FRA"]
    return {"from": y0, "to": y1, "balance_start": bal.loc[y0, "FRA"], "balance_end": bal.loc[y1, "FRA"],
            "change_in_balance_pp": d_bal, "revenue_change_pp": d_rev, "spending_change_pp": d_sp,
            "revenue_change_eur_bn_at_end_year_gdp": d_rev / 100 * ngdp.loc[y1]}
dec = pd.DataFrame([decompose(2017, 2024), decompose(2019, 2025), decompose(2007, 2025)])
save_table(dec.round(2), "m01_deficit_decomposition")

# 4 and 5 interest, effective rate, r minus g, debt stabilising primary balance
interest_pct = (pb - bal)  # % of GDP
rows = []
for yr in range(2000, 2032):
    d_prev = debt.loc[yr - 1, "FRA"] / 100
    i_pct = interest_pct.loc[yr, "FRA"] / 100
    g_nom = ngdp.loc[yr] / ngdp.loc[yr - 1] - 1
    # effective rate on last year's stock: interest(t) / debt(t-1), both in euros
    r_eff = (i_pct * ngdp.loc[yr]) / (d_prev * ngdp.loc[yr - 1])
    pb_star = d_prev * (r_eff - g_nom) / (1 + g_nom) * 100
    rows.append({"year": yr, "debt_pct": debt.loc[yr, "FRA"], "interest_pct_gdp": i_pct * 100,
                 "interest_eur_bn": i_pct * ngdp.loc[yr], "effective_rate_pct": r_eff * 100,
                 "nominal_growth_pct": g_nom * 100, "r_minus_g_pp": (r_eff - g_nom) * 100,
                 "primary_balance_pct": pb.loc[yr, "FRA"], "debt_stabilising_pb_pct": pb_star,
                 "gap_pb_vs_stabilising_pp": pb.loc[yr, "FRA"] - pb_star})
rg = save_table(pd.DataFrame(rows).set_index("year").round(2), "m01_interest_r_minus_g")

# Peers primary balance 2025 and 2026
peers = pd.DataFrame({y: pb.loc[y, ["FRA", "ITA", "ESP", "GRC", "DEU"]] for y in (2024, 2025, 2026)})
save_table(peers.round(2), "m01_primary_balance_peers")

# Chart: revenue vs spending France
fig, ax = plt.subplots(figsize=(8, 4))
r_ = rev["FRA"].loc[1995:2026]; s_ = spend["FRA"].loc[1995:2026]
ax.plot(s_.index, s_.values, color=RED, label="Spending")
ax.plot(r_.index, r_.values, color=BLUE, label="Revenue")
ax.fill_between(r_.index, r_.values, s_.values, color="#f6d3d2", alpha=0.6, label="Deficit")
ax.set_ylabel("% of GDP"); ax.set_title("Figure 3: France has not covered its spending since before 1995")
ax.legend(loc="upper left", ncol=3)
source_note(fig, "IMF World Economic Outlook (retrieved 19 Oct 2026); 2026 is an IMF estimate.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig02_revenue_spending.png"); plt.close(fig)

with open(TABLES / "m01_summary.txt", "w") as f:
    f.write(f"Surplus years for France in IMF data 1995 to 2025: {surplus_years}\n")
    f.write(dec.round(2).to_string() + "\n\n")
    f.write(rg.loc[[2007, 2019, 2023, 2024, 2025, 2026, 2027, 2030]].to_string() + "\n\n")
    f.write(peers.round(2).to_string() + "\n")
    f.write(f"Debt 2007 {debt.loc[2007,'FRA']:.1f}%, 2019 {debt.loc[2019,'FRA']:.1f}%, 2025 {debt.loc[2025,'FRA']:.1f}%, 2031 {debt.loc[2031,'FRA']:.1f}%\n")
    f.write(f"Spending 2025 {spend.loc[2025,'FRA']:.1f}% vs Germany {spend.loc[2025,'DEU']:.1f}%, Italy {spend.loc[2025,'ITA']:.1f}%, Spain {spend.loc[2025,'ESP']:.1f}%\n")
print(open(TABLES / "m01_summary.txt").read())

# ---------- Appendix figure A1: how the model works ----------
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4))
ax = axes[0]
d = dec.iloc[0]
steps = [("2017 balance", d.balance_start, None), ("Revenue change", d.revenue_change_pp, None),
         ("Spending change", -d.spending_change_pp, None), ("2024 balance", d.balance_end, None)]
x = range(len(steps)); run_ = 0
for i, (lab, v, _) in enumerate(steps):
    if i in (0, 3):
        ax.bar(i, v, color=GREY, width=0.55); ax.text(i, v - 0.4, f"{v:.1f}", ha="center", fontsize=9)
        run_ = v
    else:
        ax.bar(i, v, bottom=run_, color=RED if v < 0 else GREEN, width=0.55)
        ax.text(i, run_ + v - 0.4 if v < 0 else run_ + v + 0.12, f"{v:+.1f}", ha="center", fontsize=9)
        run_ += v
ax.set_xticks(list(x)); ax.set_xticklabels([s[0] for s in steps], fontsize=8.5)
ax.axhline(0, color=INK2, lw=0.8); ax.set_ylabel("% of GDP"); ax.set_ylim(-7.2, 0.6)
ax.set_title("Deficit change 2017 to 2024, split by cause", fontsize=10.5)
ax = axes[1]
ax.plot(rg.index, rg.effective_rate_pct, color=RED, label="Effective interest rate (r)")
ax.plot(rg.index, rg.nominal_growth_pct, color=BLUE, label="Nominal GDP growth (g)")
ax.axvspan(2025.5, 2031.5, color="#f1efe9", zorder=0)
ax.set_ylabel("%"); ax.set_title("r against g, 2000 to 2031", fontsize=10.5); ax.legend(fontsize=8)
fig.suptitle("Figure 2: Model 01, where the deficit came from and why growth no longer helps", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 01, IMF WEO. Shaded = IMF projection. Positive bars improve the balance, negative bars worsen it.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "figA1_model01_decomposition.png"); plt.close(fig)
