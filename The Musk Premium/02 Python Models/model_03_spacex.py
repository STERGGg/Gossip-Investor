"""
MODEL 03  SpaceX, the part that makes money
1. Revenue by business in the third quarter of 2026 against a year earlier, as reported by the
   Financial Times on 20 October 2026: AI cloud computing, Starlink and launch. The year
   earlier split for launch is backed out as total revenue minus AI and Starlink.
2. Capex against revenue in the quarter, and the fourth quarter capex guidance.
3. The share price since the June 2026 IPO against the $135 offer price, and the implied
   market value (offer value of $1,770bn scaled by price).
"""
from common import *

style(); h = hand()
px = prices()["SPCX"].dropna()
seg = pd.DataFrame({
    "Q3 2025": [h["spcx_q3_ai_ly"], h["spcx_q3_starlink_ly"], h["spcx_q3_rev_ly"] - h["spcx_q3_ai_ly"] - h["spcx_q3_starlink_ly"]],
    "Q3 2026": [h["spcx_q3_ai"], h["spcx_q3_starlink"], h["spcx_q3_launch"]]},
    index=["AI cloud computing", "Starlink", "Launch and other"])
mcap_now = h["spcx_ipo_value"] * px.iloc[-1] / h["spcx_ipo_price"]
res = pd.Series({"q3_revenue_bn": h["spcx_q3_rev"], "ai_share_pct": h["spcx_q3_ai"] / h["spcx_q3_rev"] * 100,
                 "ai_growth_x": h["spcx_q3_ai"] / h["spcx_q3_ai_ly"], "capex_to_revenue": h["spcx_q3_capex"] / h["spcx_q3_rev"],
                 "peak_close": px.max(), "last_close": px.iloc[-1], "from_peak_pct": (px.iloc[-1] / px.max() - 1) * 100,
                 "vs_ipo_pct": (px.iloc[-1] / h["spcx_ipo_price"] - 1) * 100, "implied_mcap_bn": mcap_now})
save_table(seg, "m03_spacex_segments"); save_table(res.round(2).to_frame("value"), "m03_spacex_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1, 1.2]})
ax = axes[0]
bottom = np.zeros(2)
for (name, row), c in zip(seg.iterrows(), [VIOLET, BLUE, GREY]):
    ax.bar(seg.columns, row.values, 0.55, bottom=bottom, color=c, label=name)
    for i, v in enumerate(row.values):
        if v > 0.9:
            ax.text(i, bottom[i] + v / 2, f"${v:.1f}bn", ha="center", va="center", fontsize=8.5, color="white", fontweight="bold")
    bottom += row.values
ax.bar(["Q3 2026"], [h["spcx_q3_capex"]], 0.18, color=RED, alpha=0.0)
ax.axhline(h["spcx_q3_capex"], color=RED, ls="--", lw=1.2); ax.text(1.3, h["spcx_q3_capex"] + 0.4, f"Capex in Q3 2026: ${h['spcx_q3_capex']:.1f}bn", color=RED, fontsize=8, ha="right")
ax.set_ylabel("Revenue in the quarter, USD bn"); ax.set_ylim(0, 23); ax.grid(axis="x", visible=False)
ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(0, 0.84)); ax.set_title("AI now earns more than rockets and Starlink", fontsize=10.5)
ax = axes[1]
ax.plot(px.index, px.values, color=BLUE, lw=1.8)
ax.axhline(h["spcx_ipo_price"], color=INK2, ls="--", lw=1); ax.text(px.index[2], h["spcx_ipo_price"] + 2, "IPO price $135", fontsize=8, color=INK2)
ax.annotate(f"Peak close ${px.max():.0f}", (px.idxmax(), px.max()), (px.idxmax() + pd.Timedelta(days=20), px.max() + 3), fontsize=8, color=INK2,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_ylabel("Share price, USD"); ax.set_ylim(100, 215)
import matplotlib.dates as mdates; ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")); ax.xaxis.set_major_locator(mdates.MonthLocator()); ax.set_title("SpaceX shares since the IPO", fontsize=10.5)
ax.tick_params(axis="x", labelsize=8)
finish(fig, "Figure 3: SpaceX makes real money, increasingly from AI rather than rockets",
       "author's model 03; Financial Times (20 Oct 2026); Nasdaq via OpenBB; Alphaspread (IPO price).", "fig03_spacex.png")
print(seg); print(res.round(2))
