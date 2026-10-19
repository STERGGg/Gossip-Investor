"""
MODEL 05  Is it 1999 again? The Nasdaq 100 now against the dot-com boom
1. Nasdaq 100 index (Nasdaq daily closes via OpenBB). The dot-com run is measured from June
   1996 (first date in the data) and the AI run from 30 November 2022, the launch of ChatGPT.
   Both are rebased to 100 at their start and plotted by months since the start.
2. Peak gain and the fall after the peak: dot-com peak to trough, and the AI run to date.
3. Leaders: Cisco then (data from Oct 2016 only, so the 2000 crash is quoted from the
   Nasdaq 100 instead) and Nvidia now, rebased to the ChatGPT launch.
"""
from common import *
import matplotlib.dates

style(); px = prices()
ndx = px["NDX"].dropna()
dc = ndx.loc["1996-06-01":"2003-12-31"]; ai = ndx.loc["2022-11-30":]
def months(s):
    return (s.index - s.index[0]).days / 30.44
dcr = dc / dc.iloc[0] * 100; air = ai / ai.iloc[0] * 100
dc_peak = dcr.max(); dc_peak_d = dcr.idxmax(); dc_trough = dcr.loc[dc_peak_d:].min()
ai_peak = air.max(); ai_now = air.iloc[-1]
nv = px["NVDA"].dropna().loc["2022-11-30":]; nvr = nv / nv.iloc[0] * 100
res = pd.Series({"dotcom_peak_multiple": dc_peak / 100, "dotcom_months_to_peak": months(dcr.loc[:dc_peak_d]).max(),
                 "dotcom_fall_from_peak_pct": (dc_trough / dc_peak - 1) * 100, "ai_peak_multiple": ai_peak / 100,
                 "ai_months_so_far": months(air).max(), "ai_now_multiple": ai_now / 100, "ai_from_peak_pct": (ai_now / ai_peak - 1) * 100,
                 "nvidia_multiple_since_chatgpt": nvr.iloc[-1] / 100})
save_table(res.round(2).to_frame("value"), "m05_bubble_test")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axes[0]
ax.plot(months(dcr), dcr.values, color=GREY, label="Dot-com: Nasdaq 100 from June 1996")
ax.plot(months(air), air.values, color=BLUE, label="AI: Nasdaq 100 from ChatGPT launch (Nov 2022)")
ax.annotate(f"March 2000 peak: {dc_peak/100:.1f}x", (months(dcr.loc[:dc_peak_d]).max(), dc_peak), xytext=(8, -4), textcoords="offset points", ha="left", fontsize=8.5)
ax.annotate(f"then {res.dotcom_fall_from_peak_pct:.0f}% from the peak", (60, 330), fontsize=8.5, color=INK2)
ax.annotate(f"Today: {ai_now/100:.1f}x", (months(air).max(), ai_now), xytext=(5, -15), textcoords="offset points", fontsize=8.5, color=BLUE)
ax.set_xlabel("Months since the start of the boom"); ax.set_ylabel("Rebased to 100"); ax.legend(fontsize=8, loc="upper left"); ax.set_ylim(0, 820)
ax.set_title("The AI rally is big, but nowhere near 1999", fontsize=11)
ax = axes[1]
ax.plot(nvr.index, nvr.values, color=AQUA, label="Nvidia")
ax.plot(air.index, air.values, color=BLUE, label="Nasdaq 100")
ax.set_ylabel("Rebased, 30 Nov 2022 = 100"); ax.legend(fontsize=8); ax.xaxis.set_major_locator(matplotlib.dates.YearLocator()); ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y")); ax.set_title("The leader has done the heavy lifting", fontsize=11)
finish(fig, "Figure 9: Is it 1999 again?", "author's model 05; Nasdaq daily closes via OpenBB (Nasdaq 100 from June 1996; Nvidia).", "fig05_bubble_test.png")
print(res.round(2).to_string())
