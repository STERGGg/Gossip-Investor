"""
common.py
Shared helpers for the France Report Project models.

Every model reads data only from the folder 03 Data (downloaded public data or the
hand collected table with a source and URL on every row) and writes its
results to 04 Outputs. Nothing is typed in by hand inside the models apart
from clearly labelled scenario settings.

Requirements: python 3.9+, pandas, numpy, matplotlib
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "03 Data"
OUT = ROOT / "04 Outputs"
CHARTS = OUT / "charts"
TABLES = OUT / "tables"
for p in (CHARTS, TABLES):
    p.mkdir(parents=True, exist_ok=True)

# Chart colours (validated categorical palette, fixed order)
BLUE = "#2a78d6"     # France always takes slot 1
ORANGE = "#eb6834"   # Germany
AQUA = "#1baf7a"     # Spain
YELLOW = "#eda100"
MAGENTA = "#e87ba4"
GREEN = "#008300"
VIOLET = "#6250d6"   # Italy
RED = "#e34948"      # Greece
GREY = "#9a9893"
INK = "#0b0b0b"
INK2 = "#52514e"
COUNTRY_COL = {"FRA": BLUE, "DEU": ORANGE, "ESP": AQUA, "ITA": VIOLET, "GRC": RED,
               "FR": BLUE, "DE": ORANGE, "ES": AQUA, "IT": VIOLET, "GR": RED}
NAMES = {"FRA": "France", "DEU": "Germany", "ESP": "Spain", "ITA": "Italy", "GRC": "Greece",
         "BEL": "Belgium", "PRT": "Portugal", "AUT": "Austria", "NLD": "Netherlands",
         "IRL": "Ireland", "FIN": "Finland"}
ISO2_TO_3 = {"FR": "FRA", "DE": "DEU", "ES": "ESP", "IT": "ITA", "GR": "GRC", "BE": "BEL",
             "PT": "PRT", "AT": "AUT", "NL": "NLD", "IE": "IRL", "FI": "FIN"}


def style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": "#c9c7c1", "axes.labelcolor": INK2,
        "xtick.color": INK2, "ytick.color": INK2,
        "axes.grid": True, "grid.color": "#e8e6e1", "grid.linewidth": 0.6,
        "axes.titleweight": "bold", "axes.titlesize": 12, "axes.titlelocation": "left",
        "legend.frameon": False, "figure.dpi": 150, "savefig.dpi": 200,
        "lines.linewidth": 2, "axes.axisbelow": True,
    })


def source_note(fig, text):
    fig.text(0.01, 0.005, "Source: " + text, fontsize=7.5, color=INK2, ha="left", va="bottom")


def hand():
    """Hand collected figures: key -> value. Each row in the csv carries its source and URL."""
    df = pd.read_csv(DATA / "hand_collected_sources.csv")
    return dict(zip(df.key, df.value))


def weo():
    """IMF World Economic Outlook, long format -> dict of DataFrames (index year, columns ISO3)."""
    frames = []
    for f in ("imf_weo_tidy.csv", "imf_weo_tidy2.csv"):
        d = pd.read_csv(DATA / f)
        frames.append(d)
    d = pd.concat(frames)
    long = d.melt(id_vars=["ind", "country_code"], var_name="year", value_name="value")
    long["year"] = long.year.astype(int)
    out = {}
    for ind, g in long.groupby("ind"):
        out[ind] = g.pivot_table(index="year", columns="country_code", values="value")
    extra = pd.read_csv(DATA / "imf_weo_france_extra.csv", index_col=0).T
    extra.index = extra.index.astype(int)
    out["NGDP_FRA"] = extra["NGDP"] / 1e9          # EUR bn
    out["LUR_FRA"] = extra["LUR"]
    out["CPI_FRA"] = extra["PCPIPCH"]
    return out


def yields():
    """ECB long term interest rates for convergence purposes (10y), monthly, % ; columns ISO3."""
    y = pd.read_csv(DATA / "ecb_10y_yields_monthly.csv", index_col=0, parse_dates=True)
    y.columns = [ISO2_TO_3[c] for c in y.columns]
    return y


def spreads_bp():
    y = yields()
    return (y.sub(y["DEU"], axis=0).drop(columns="DEU") * 100)


def save_table(df, name):
    df.to_csv(TABLES / f"{name}.csv")
    return df
