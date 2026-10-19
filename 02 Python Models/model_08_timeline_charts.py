"""
MODEL 08  Timeline and market charts

Figure 4: timeline 2007 to 2026 of the French 10y spread over Germany (ECB
monthly averages) with the political and fiscal events that matter, and the
debt ratio underneath (IMF). Two panels share the time axis rather than using
two y axes on one chart.
Figure 5: 10 year yields of France, Italy, Spain and Greece since 2023.
"""
from common import *
import matplotlib.dates as mdates

style()
sp = spreads_bp(); y = yields(); w = weo(); h = hand()
fr = sp["FRA"].loc["2007":]

events = [
    ("2009-10-15", "Greek deficit revealed"),
    ("2011-11-15", "Euro crisis peak"),
    ("2012-01-15", "S&P removes AAA"),
    ("2012-03-09", "Greek PSI"),
    ("2017-02-15", "Le Pen surge in polls"),
    ("2017-05-15", "Macron elected"),
    ("2018-11-15", "Gilets jaunes"),
    ("2020-03-15", "Covid: whatever it costs"),
    ("2023-03-15", "Pension reform by 49.3"),
    ("2023-06-30", "Nanterre riots"),
    ("2024-06-15", "Assembly dissolved"),
    ("2024-12-04", "Barnier censured"),
    ("2025-09-08", "Bayrou falls, Fitch A+"),
    ("2025-10-10", "Lecornu out and back, S&P A+"),
    ("2026-06-11", "ECB hikes (energy shock)"),
    ("2026-09-25", "Lycee riots, 2027 budget"),
]

fig = plt.figure(figsize=(11, 7.2))
gs = fig.add_gridspec(2, 1, height_ratios=[3, 1.2], hspace=0.08)
ax = fig.add_subplot(gs[0]); ax2 = fig.add_subplot(gs[1], sharex=ax)
ax.plot(fr.index, fr.values, color=BLUE, lw=1.8)
peak = pd.Timestamp("2026-10-02")
ax.scatter([peak], [h["spread_peak_oct2026"]], color=RED, s=30, zorder=4)
ax.annotate("about 150bp on 2 Oct 2026", (peak, h["spread_peak_oct2026"]), xytext=(-170, 8),
            textcoords="offset points", fontsize=8, color=RED)
for i, (d, lab) in enumerate(events, start=1):
    dt = pd.Timestamp(d)
    v = fr.loc[:dt].iloc[-1]
    ax.scatter([dt], [v], color=INK, s=14, zorder=3)
    ax.annotate(str(i), (dt, v), xytext=(0, 9 if i % 2 else -15), textcoords="offset points",
                ha="center", fontsize=8, fontweight="bold", color=INK)
ax.set_ylabel("France minus Germany 10y yield, bp")
ax.set_title("Figure 4: Timeline of the French crisis, 2007 to 2026")
plt.setp(ax.get_xticklabels(), visible=False)
items = [f"{i}. {lab}".replace(" ", "\u00a0") for i, (d, lab) in enumerate(events, start=1)]
import textwrap
fig.text(0.01, 0.035, "\n".join(textwrap.wrap("   ".join(items), 175)), fontsize=7.6, color=INK, va="bottom")

debt = w["GGXWDG_NGDP"]["FRA"].loc[2007:2026]
ax2.bar([pd.Timestamp(f"{yr}-07-01") for yr in debt.index], debt.values, width=250,
        color=[BLUE if yr < 2026 else "#b9d2f0" for yr in debt.index])
for yr in (2007, 2012, 2019, 2020, 2026):
    ax2.text(pd.Timestamp(f"{yr}-07-01"), debt.loc[yr] + 3, f"{debt.loc[yr]:.0f}%", ha="center", fontsize=7.5)
ax2.set_ylabel("Debt, % GDP"); ax2.set_ylim(0, 140)
ax2.xaxis.set_major_locator(mdates.YearLocator(2)); ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
source_note(fig, "ECB long term interest rates (monthly), IMF WEO debt (2026 estimate shaded), EFG International for the Oct 2026 peak.")
fig.subplots_adjust(left=0.07, right=0.98, top=0.95, bottom=0.14)
fig.savefig(CHARTS / "fig03_timeline.png"); plt.close(fig)

# Figure 4
fig, ax = plt.subplots(figsize=(8.5, 4))
for c in ["GRC", "ITA", "ESP", "FRA", "DEU"]:
    s = y[c].loc["2023-01":]
    ax.plot(s.index, s.values, color=COUNTRY_COL[c], lw=2.6 if c == "FRA" else 1.5)
    off = {"FRA": 0.12, "ITA": 0.0, "GRC": -0.12, "ESP": 0.0, "DEU": 0.0}[c]
    ax.text(s.index[-1], s.dropna().iloc[-1] + off, f"  {NAMES[c]} {s.dropna().iloc[-1]:.2f}%", color=COUNTRY_COL[c], fontsize=8.5, va="center")
ax.set_ylabel("10 year government bond yield, %")
ax.set_xlim(pd.Timestamp("2023-01-01"), pd.Timestamp("2027-04-01"))
ax.set_title("Figure 5: France now borrows at the same price as Italy and above Greece")
source_note(fig, "ECB long term interest rates for convergence purposes, monthly averages to September 2026.")
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(CHARTS / "fig04_yields_peers.png"); plt.close(fig)

last = y.loc["2026-09"].iloc[0]
with open(TABLES / "m08_summary.txt", "w") as fh:
    fh.write("September 2026 10y yields (%):\n" + last.round(3).to_string() + "\n")
    fh.write(f"France minus Italy Sep 2026: {(last['FRA']-last['ITA'])*100:.1f}bp ; France minus Greece {(last['FRA']-last['GRC'])*100:.1f}bp\n")
    fh.write(f"Max monthly FR spread 2011-2012: {fr.loc['2011':'2012'].max():.1f}bp in {fr.loc['2011':'2012'].idxmax().date()}\n")
    fh.write(f"FR spread Jan 2024 to May 2024 avg {fr.loc['2024-01':'2024-05'].mean():.1f}; Jul 2024 {fr.loc['2024-07'].iloc[0]:.1f}; Sep 2026 {fr.loc['2026-09'].iloc[0]:.1f}\n")
    fh.write(f"FR minus IT history: 2012 avg {(y['FRA']-y['ITA']).loc['2012'].mean()*100:.0f}bp, 2019 avg {(y['FRA']-y['ITA']).loc['2019'].mean()*100:.0f}bp, 2023 avg {(y['FRA']-y['ITA']).loc['2023'].mean()*100:.0f}bp\n")
print(open(TABLES / "m08_summary.txt").read())
