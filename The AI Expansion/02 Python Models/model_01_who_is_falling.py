"""
MODEL 01  Is the whole AI trade falling, or only the borrowers?
Daily closes from Nasdaq (via OpenBB, retrieved 19 Oct 2026) for Oracle, CoreWeave, Nvidia,
the four cash rich hyperscalers (Microsoft, Alphabet, Amazon, Meta), the S&P 500 (SPY) and
the Nasdaq 100 (QQQ). Two measures:
1. Fall from each stock's own record close to the last close (16 Oct 2026).
2. Price rebased to 100 on 2 Jan 2025, so the paths can be compared.
"""
from pathlib import Path
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
px = pd.read_csv(ROOT / "03 Data" / "daily_close.csv", index_col=0, parse_dates=True)[["ORCL", "NVDA", "CRWV", "MSFT", "META", "GOOGL", "AMZN", "QQQ", "SPY", "COPX"]].loc["2016-10-17":]
names = {"ORCL": "Oracle", "CRWV": "CoreWeave", "NVDA": "Nvidia", "MSFT": "Microsoft", "GOOGL": "Alphabet",
         "AMZN": "Amazon", "META": "Meta", "QQQ": "Nasdaq 100", "SPY": "S&P 500"}
borrowers = {"ORCL", "CRWV"}
dd = pd.DataFrame({"record_close": px.max(), "record_date": px.idxmax().dt.date, "last_close": px.ffill().iloc[-1]})
dd["from_record_pct"] = (dd.last_close / dd.record_close - 1) * 100
dd = dd.drop(index="COPX").sort_values("from_record_pct")
(ROOT / "04 Outputs" / "tables").mkdir(parents=True, exist_ok=True)
dd.round(2).to_csv(ROOT / "04 Outputs" / "tables" / "m01_drawdowns.csv")

plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
                     "grid.color": "#e8e6e1", "axes.titlelocation": "left", "axes.titleweight": "bold"})
fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios": [1, 1.4]})
ax = axes[0]
cols = ["#e34948" if t in borrowers else ("#9a9893" if t in ("SPY", "QQQ") else "#2a78d6") for t in dd.index]
ax.barh([names[t] for t in dd.index][::-1], dd.from_record_pct[::-1], color=cols[::-1])
for i, v in enumerate(dd.from_record_pct[::-1]):
    ax.text(v - 1, i, f"{v:.0f}%", va="center", ha="right", fontsize=8.5)
ax.set_xlim(-80, 5); ax.set_xlabel("% below record close, 16 Oct 2026"); ax.grid(axis="y", visible=False)
ax.set_title("Fall from record close", fontsize=11)
ax = axes[1]
reb = px.loc["2025-01-02":].ffill()
for t in ["ORCL", "CRWV", "NVDA", "MSFT", "GOOGL", "SPY"]:
    s = reb[t].dropna(); s = s / s.iloc[0] * 100
    ax.plot(s.index, s, lw=2.2 if t in borrowers else 1.4, label=names[t],
            color={"ORCL": "#e34948", "CRWV": "#eb6834", "NVDA": "#1baf7a", "MSFT": "#2a78d6", "GOOGL": "#6250d6", "SPY": "#52514e"}[t])
ax.axhline(100, color="#9a9893", lw=0.8); ax.legend(fontsize=8, ncol=3, loc="upper left")
ax.set_ylabel("Rebased, first close in 2025 (CoreWeave: IPO) = 100"); ax.set_title("The borrowers rose fastest and fell hardest", fontsize=11)
fig.suptitle("Figure 1: The AI selloff is a credit story, not a technology story", x=0.01, ha="left", fontweight="bold")
fig.text(0.01, 0.01, "Source: author's model 01, Nasdaq daily closes via OpenBB to 16 Oct 2026. Red: companies funding AI capacity with debt.", fontsize=7.5, color="#52514e")
fig.tight_layout(rect=(0, 0.04, 1, 0.93)); fig.savefig(ROOT / "04 Outputs" / "charts" / "fig01_who_is_falling.png", dpi=200)
print(dd.round(1).to_string())
