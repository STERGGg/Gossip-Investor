"""
MODEL 14  What does it mean for people living in France?

1. Mortgage rates: ECB MFI interest rate statistics (MIR), new loans for house
   purchase to households, France against Germany, Italy and Spain, monthly.
2. The monthly payment on an illustrative EUR 200,000 loan over 20 years, using the
   standard annuity formula  P = L r / (1 - (1 + r)^-n)  with r the monthly rate,
   at the December 2021 low and at the latest French rate.
3. Savings: the real return on the Livret A (rate minus IMF 2026 French inflation
   forecast) and the size of assurance vie, the main channel through which French
   households hold their own government's debt.
"""
from common import *

style()
h = hand(); w = weo()
m = pd.read_csv(DATA / "ecb_mir_mort_monthly.csv", index_col=0, parse_dates=True)
m.columns = [c.split(".")[1] for c in m.columns]
m.columns = [ISO2_TO_3[c] for c in m.columns]

def payment(rate_pct, loan=200_000, years=20):
    r = rate_pct / 100 / 12; n = years * 12
    return loan * r / (1 - (1 + r) ** -n)

low_date = m["FRA"].loc["2021":"2022"].idxmin()
low, last = m["FRA"].loc[low_date], m["FRA"].iloc[-1]
p_low, p_last = payment(low), payment(last)
gap = (m["FRA"] - m["DEU"]).loc["2026"].mean()
cpi26 = w["CPI_FRA"].loc[2026]
real_livret = h["livret_a_rate_aug2026"] - cpi26
save_table(pd.DataFrame({"rate_pct": [low, last], "monthly_payment_eur": [p_low, p_last]},
                        index=[str(low_date.date()), str(m.index[-1].date())]).round(2), "m14_mortgage_payment")

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": [1.6, 1]})
ax = axes[0]
for c in ["FRA", "DEU", "ITA", "ESP"]:
    ax.plot(m.index, m[c], color=COUNTRY_COL[c], lw=2.2 if c == "FRA" else 1.4, label=NAMES[c])
ax.set_ylabel("% a year, new house purchase loans"); ax.legend(fontsize=8, ncol=4, loc="upper left")
ax.set_title("Mortgage rates on new loans", fontsize=10.5)
ax = axes[1]
ax.bar([0, 1], [p_low, p_last], color=[GREY, BLUE], width=0.55)
for i, (v, r) in enumerate([(p_low, low), (p_last, last)]):
    ax.text(i, v + 15, f"€{v:,.0f}\nat {r:.2f}%", ha="center", fontsize=9)
ax.set_xticks([0, 1]); ax.set_xticklabels([low_date.strftime("%b %Y"), m.index[-1].strftime("%b %Y")])
ax.set_ylim(0, p_last * 1.3); ax.set_ylabel("EUR per month"); ax.grid(axis="x", visible=False)
ax.set_title("€200,000 over 20 years", fontsize=10.5)
fig.suptitle("Figure 27: What the crisis means for a French mortgage", x=0.01, ha="left", fontweight="bold")
source_note(fig, "Author's model 14: ECB MFI interest rate statistics (MIR), new business, households, house purchase.")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(CHARTS / "fig19_households.png"); plt.close(fig)

with open(TABLES / "m14_summary.txt", "w") as fh:
    fh.write(f"French mortgage low {low:.2f}% ({low_date.date()}), latest {last:.2f}% ({m.index[-1].date()})\n")
    fh.write(f"Monthly payment on EUR 200k over 20y: EUR {p_low:.0f} -> EUR {p_last:.0f} (+EUR {p_last-p_low:.0f}, +{(p_last/p_low-1)*100:.0f}%)\n")
    fh.write(f"France minus Germany mortgage rate, 2026 average: {gap*100:.0f}bp\n")
    fh.write("Latest rates: " + m.iloc[-1].round(2).to_string().replace("\n", "; ") + "\n")
    fh.write(f"Livret A {h['livret_a_rate_aug2026']}% vs IMF 2026 inflation {cpi26:.2f}% -> real {real_livret:.2f}%\n")
    fh.write(f"Assurance vie EUR {h['assurance_vie_aug2026']}bn = {h['assurance_vie_aug2026']/w['NGDP_FRA'].loc[2026]*100:.0f}% of 2026 GDP\n")
print(open(TABLES / "m14_summary.txt").read())
