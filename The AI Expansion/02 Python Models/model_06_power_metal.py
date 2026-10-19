"""
MODEL 06  Is AI held back by power, copper and the grid?
1. Copper: monthly LME price in US dollars per tonne from the IMF Primary Commodity Prices
   database (PCPS, via OpenBB), with aluminium for comparison, rebased to January 2022.
2. Electricity: data centre use worldwide (IEA, 2024 and 2030) and in the US (LBNL for the
   Department of Energy, 2023 and the 2028 range). Total US use is backed out from LBNL's
   own share: 176 TWh / 4.4%.
3. OpenAI's 30 GW: the most it could use in a year if run flat out is 30 GW x 8,760 hours
   = 263 TWh. This is an upper bound, not a forecast, and is set against the numbers above.
"""
from common import *

style(); h = hand()
m = pd.read_csv(DATA / "imf_pcps_metals_monthly.csv", index_col=0, parse_dates=True)
cu = m["PCPS::PCOPP"]; al = m["PCPS::PALUM"]
us_total = h["lbnl_dc_2023_twh"] / 0.044
openai_twh = h["openai_gw"] * 8760 / 1000
bars = pd.Series({"US data centres 2023": h["lbnl_dc_2023_twh"], "US data centres 2028 (low)": h["lbnl_dc_2028_low"],
                  "US data centres 2028 (high)": h["lbnl_dc_2028_high"], "OpenAI 30 GW flat out": openai_twh,
                  "World data centres 2024": h["iea_dc_2024"], "World data centres 2030": h["iea_dc_2030"]})
save_table(bars.round(0).to_frame("TWh"), "m06_power")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
ax = axes[0]
ax.plot(cu.loc["2015":].index, cu.loc["2015":].values, color=ORANGE, label="Copper, $ per tonne")
ax.set_ylabel("Copper, USD per tonne"); ax.set_title(f"Copper: ${cu.iloc[-1]:,.0f} a tonne in {cu.index[-1]:%b %Y}", fontsize=11)
ax.legend(loc="upper left", fontsize=8)
ax = axes[1]
cols = [GREY, GREY, GREY, RED, BLUE, BLUE]
ax.barh(bars.index[::-1], bars.values[::-1], color=cols[::-1])
for i, v in enumerate(bars.values[::-1]):
    ax.text(v + 8, i, f"{v:,.0f} TWh", va="center", fontsize=8.5)
ax.set_xlim(0, bars.max() * 1.25); ax.grid(axis="y", visible=False); ax.set_xlabel("Terawatt hours a year")
ax.set_title("Electricity, terawatt hours a year", fontsize=11)
finish(fig, "Figure 11: The limits are physical: metal and megawatts",
       "author's model 06; IMF Primary Commodity Prices via OpenBB; IEA Energy and AI (2025); LBNL for US DOE (Dec 2024); OpenAI 30 GW (Reuters).",
       "fig06_power_metal.png")
with open(TABLES / "m06_summary.txt", "w") as fh:
    fh.write(bars.round(0).to_string() + f"\nUS total electricity implied {us_total:,.0f} TWh; OpenAI flat out = {openai_twh/us_total*100:.1f}% of US use, {openai_twh/h['lbnl_dc_2023_twh']:.2f}x all US data centres in 2023\n")
    fh.write(f"Copper latest {cu.iloc[-1]:,.0f} ({cu.index[-1].date()}), Jan 2022 {cu.loc['2022-01'].iloc[0]:,.0f}, change {(cu.iloc[-1]/cu.loc['2022-01'].iloc[0]-1)*100:.0f}%; 2015 low {cu.loc['2015':].min():,.0f}\n")
print(open(TABLES / "m06_summary.txt").read())
