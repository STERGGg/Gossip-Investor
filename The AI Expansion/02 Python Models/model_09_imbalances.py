"""
MODEL 09  The rest of the world: who is selling the shovels?
Current account balances as % of GDP, 2000 to 2031 (IMF World Economic Outlook, October
2026, via OpenBB; 2026 onwards are IMF projections) for the US and the economies that make
the chips and memory (Taiwan, South Korea), plus China, Japan and Germany for scale.
A surplus means a country earns more from the world than it spends and so has savings to
lend or invest abroad, much of it back into US assets.
"""
from common import *

style()
ca = pd.read_csv(DATA / "imf_weo_current_account_pct_gdp.csv", index_col=0)
ca.index = ca.index.astype(int)
names = {"TWN": "Taiwan", "KOR": "South Korea", "CHN": "China", "JPN": "Japan", "DEU": "Germany", "USA": "United States"}
cols = {"TWN": RED, "KOR": ORANGE, "CHN": YELLOW, "JPN": VIOLET, "DEU": GREY, "USA": BLUE}
save_table(ca.round(1), "m09_current_accounts")
fig, ax = plt.subplots(figsize=(10, 4.6))
for c in ["TWN", "KOR", "CHN", "JPN", "DEU", "USA"]:
    s = ca[c].loc[2000:2031]
    ax.plot(s.loc[:2025].index, s.loc[:2025].values, color=cols[c], lw=2.4 if c in ("TWN", "KOR", "USA") else 1.4, label=names[c])
    ax.plot(s.loc[2025:].index, s.loc[2025:].values, color=cols[c], lw=2.4 if c in ("TWN", "KOR", "USA") else 1.4, ls="--")
    if c in ("TWN", "KOR", "USA"):
        ax.text(2031.3, s.loc[2031], f"{names[c]}\n2026: {s.loc[2026]:.0f}%", color=cols[c], fontsize=8, va="center")
ax.axvspan(2025.5, 2031.5, color="#f2f0eb", zorder=0); ax.text(2026, ca.max().max() * 0.95, "IMF projections", fontsize=8, color=INK2)
ax.axhline(0, color=INK2, lw=0.8); ax.set_xlim(2000, 2035); ax.set_ylabel("Current account balance, % of GDP")
ax.set_title("The chip makers are running the biggest surpluses in their history", fontsize=11)
ax.legend([plt.Line2D([], [], color=cols[c]) for c in ["CHN", "JPN", "DEU"]], [names[c] for c in ["CHN", "JPN", "DEU"]], fontsize=8, loc="upper left")
finish(fig, "Figure 14: The AI boom is building huge savings in Asia, and they flow back to the US",
       "author's model 09; IMF World Economic Outlook (October 2026) via OpenBB.", "fig09_imbalances.png")
print(ca.loc[[2007, 2019, 2025, 2026, 2031]].round(1))
