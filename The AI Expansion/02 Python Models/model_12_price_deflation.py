"""
MODEL 12  The price treadmill: falling prices and cheap Chinese models
1. Price gap today: price per million input tokens of OpenAI's GPT-5.5 against DeepSeek V4
   Flash (June 2026, reported by CNBC).
2. Chinese models' share of enterprise token volume on OpenRouter: first half 2025, the
   prior twelve month average and the mid 2026 weekly peak (CNBC / OpenRouter).
3. The treadmill: OpenAI's own plan needs revenue to grow 9.4 times from 2026 (30bn) to 2030
   (282.5bn). Revenue = usage x price, so usage must grow by 9.4 times the cumulative price
   fall. Shown for prices flat, halving each year, falling 4x a year and falling 10x a year
   (a16z's estimate for the cost of equivalent performance). Epoch AI's range of 9x to 900x
   a year applies to a fixed level of capability, so frontier prices fall more slowly.
"""
from common import *

style(); h = hand()
rev_mult = h["openai_rev_2030_plan"] / h["openai_rev_2026_plan"]
falls = {"Prices flat": 1, "Prices halve\neach year": 2, "Prices fall\n4x a year": 4, "Prices fall\n10x a year": 10}
need = pd.Series({k: rev_mult * v ** 4 for k, v in falls.items()})
save_table(need.round(1).to_frame("usage_growth_needed_2026_2030"), "m12_treadmill")
share = pd.Series({"H1 2025": h["cn_share_h1_2025"], "Prior 12 months\n(avg to mid 2026)": h["cn_share_12m_avg"], "Mid 2026\n(weekly peak)": h["cn_share_peak_2026"]})

fig, axes = plt.subplots(1, 3, figsize=(12, 4.3), gridspec_kw={"width_ratios": [0.8, 1, 1.25]})
ax = axes[0]
pr = pd.Series({"OpenAI\nGPT-5.5": h["gpt55_price"], "DeepSeek\nV4 Flash": h["deepseek_v4_flash"]})
ax.bar(pr.index, pr.values, color=[BLUE, RED], width=0.55)
for i, v in enumerate(pr.values):
    ax.text(i, v + 0.1, f"${v:.2f}", ha="center", fontsize=9.5)
ax.set_ylabel("USD per million input tokens"); ax.grid(axis="x", visible=False)
ax.set_title(f"{pr.iloc[0]/pr.iloc[1]:.0f}x cheaper", fontsize=11)
ax = axes[1]
ax.bar(share.index, share.values, color=[GREY, GREY, RED], width=0.55)
for i, v in enumerate(share.values):
    ax.text(i, v + 1, f"{v:.0f}%", ha="center", fontsize=9.5)
ax.set_ylabel("% of enterprise tokens on OpenRouter"); ax.set_ylim(0, 55); ax.grid(axis="x", visible=False); ax.tick_params(axis="x", labelsize=8)
ax.set_title("Chinese models' share", fontsize=11)
ax = axes[2]
ax.bar(need.index, need.values, color=[GREY, BLUE, ORANGE, RED], width=0.6); ax.set_yscale("log")
for i, v in enumerate(need.values):
    ax.text(i, v * 1.3, f"{v:,.0f}x", ha="center", fontsize=9)
ax.set_ylabel("Usage growth needed, 2026 to 2030 (log)"); ax.tick_params(axis="x", labelsize=8); ax.grid(axis="x", visible=False)
ax.set_ylim(1, need.max() * 8); ax.set_title(f"Usage needed for OpenAI's {rev_mult:.1f}x revenue plan", fontsize=10.5)
finish(fig, "Figure 8: The price treadmill",
       "author's model 12; CNBC/OpenRouter via Yahoo Finance (Jul 2026); a16z (Nov 2024); Epoch AI (Mar 2025); OpenAI plan via The Information.",
       "fig12_price_deflation.png")
print(need.round(0), rev_mult)
