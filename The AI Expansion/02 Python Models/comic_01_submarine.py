"""
COMIC 01  Can a submarine swim?
An original two panel cartoon drawn in matplotlib for the line Edsger W. Dijkstra wrote in
1984: the question of whether machines can think is about as relevant as the question of
whether submarines can swim (EWD898, The Threats to Computing Science).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, FancyBboxPatch, Circle, Polygon, Wedge
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "04 Outputs" / "comics"
OUT.mkdir(parents=True, exist_ok=True)
INK, SEA, SEA2, SKY, SUB, SAND = "#1d1d1b", "#2f6fb3", "#1f4f86", "#e8f1fb", "#9aa7b2", "#e9d8a6"

def bubble(ax, x, y, w, h, text, tail, fs=11):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc="white", ec=INK, lw=1.8, zorder=10))
    ax.add_patch(Polygon(tail, closed=True, fc="white", ec=INK, lw=1.8, zorder=9))
    ax.add_patch(Polygon([tail[0], tail[1], ((tail[0][0]+tail[1][0])/2, tail[0][1]+0.01)], closed=True, fc="white", ec="white", lw=2.5, zorder=11))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=INK, zorder=12, family="DejaVu Sans", fontweight="bold", wrap=True)

def submarine(ax, cx, cy, s=1.0, periscope=True):
    ax.add_patch(Ellipse((cx, cy), 0.62 * s, 0.2 * s, fc=SUB, ec=INK, lw=2, zorder=5))
    ax.add_patch(FancyBboxPatch((cx - 0.08 * s, cy + 0.06 * s), 0.16 * s, 0.09 * s, boxstyle="round,pad=0.005", fc=SUB, ec=INK, lw=2, zorder=4))
    if periscope:
        ax.plot([cx + 0.03 * s, cx + 0.03 * s, cx + 0.07 * s], [cy + 0.15 * s, cy + 0.24 * s, cy + 0.24 * s], color=INK, lw=2.5, zorder=4)
    for dx in (-0.16, -0.06, 0.04, 0.14):
        ax.add_patch(Circle((cx + dx * s, cy), 0.028 * s, fc="#cfe8ff", ec=INK, lw=1.5, zorder=6))
    ax.add_patch(Polygon([(cx - 0.31 * s, cy), (cx - 0.38 * s, cy + 0.07 * s), (cx - 0.38 * s, cy - 0.07 * s)], fc=SUB, ec=INK, lw=2, zorder=4))

def person(ax, x, y, s=1.0, hat=True):
    ax.add_patch(Circle((x, y + 0.2 * s), 0.045 * s, fc="#f5d0b5", ec=INK, lw=1.8, zorder=7))
    ax.plot([x, x], [y + 0.155 * s, y + 0.05 * s], color=INK, lw=2.2, zorder=6)
    ax.plot([x, x - 0.04 * s], [y + 0.05 * s, y - 0.04 * s], color=INK, lw=2.2, zorder=6)
    ax.plot([x, x + 0.04 * s], [y + 0.05 * s, y - 0.04 * s], color=INK, lw=2.2, zorder=6)
    ax.plot([x, x + 0.06 * s], [y + 0.12 * s, y + 0.17 * s], color=INK, lw=2.2, zorder=6)
    ax.plot([x, x - 0.05 * s], [y + 0.12 * s, y + 0.08 * s], color=INK, lw=2.2, zorder=6)
    if hat:
        ax.add_patch(Rectangle((x - 0.05 * s, y + 0.235 * s), 0.1 * s, 0.012 * s, fc=INK, zorder=8))
        ax.add_patch(Rectangle((x - 0.03 * s, y + 0.245 * s), 0.06 * s, 0.05 * s, fc=INK, zorder=8))

def waves(ax, y, x0=0, x1=1, amp=0.012, n=9, color=SEA2):
    xs = np.linspace(x0, x1, 400)
    ax.plot(xs, y + amp * np.sin(xs * n * 2 * np.pi), color=color, lw=2, zorder=3)

fig, axes = plt.subplots(1, 2, figsize=(11, 5.4))
for ax in axes:
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_linewidth(3); sp.set_color(INK)

# Panel 1: the philosopher on the dock
ax = axes[0]
ax.add_patch(Rectangle((0, 0.45), 1, 0.55, fc=SKY, zorder=0))
ax.add_patch(Rectangle((0, 0), 1, 0.45, fc=SEA, zorder=1))
waves(ax, 0.45)
ax.add_patch(Rectangle((0, 0.4), 0.33, 0.08, fc="#8b5a2b", ec=INK, lw=2, zorder=4))
for px in (0.05, 0.16, 0.27):
    ax.add_patch(Rectangle((px, 0.0), 0.03, 0.4, fc="#6b4421", ec=INK, lw=1.5, zorder=2))
person(ax, 0.17, 0.5, s=1.0)
submarine(ax, 0.66, 0.36, s=1.0)
bubble(ax, 0.04, 0.83, 0.6, 0.13, "Impressive. But can it\nREALLY swim?", [(0.2, 0.83), (0.27, 0.83), (0.22, 0.79)])
bubble(ax, 0.55, 0.55, 0.42, 0.14, "...define swim?", [(0.64, 0.55), (0.72, 0.55), (0.69, 0.47)], fs=10)
ax.text(0.02, 0.03, "1.", fontsize=14, fontweight="bold", color="white", zorder=12)

# Panel 2: the submarine has crossed the ocean
ax = axes[1]
ax.add_patch(Rectangle((0, 0.45), 1, 0.55, fc=SKY, zorder=0))
ax.add_patch(Rectangle((0, 0), 1, 0.45, fc=SEA, zorder=1))
waves(ax, 0.45)
ax.add_patch(Polygon([(0.62, 0.45), (0.7, 0.62), (0.8, 0.58), (0.9, 0.7), (1, 0.66), (1, 0.45)], fc=SAND, ec=INK, lw=2, zorder=2))
ax.add_patch(Rectangle((0.83, 0.62), 0.012, 0.16, fc=INK, zorder=3))
ax.add_patch(Polygon([(0.842, 0.78), (0.842, 0.72), (0.92, 0.75)], fc="#e34948", ec=INK, lw=1.5, zorder=3))
ax.text(0.86, 0.52, "NEW\nWORLD", ha="center", fontsize=9, fontweight="bold", color=INK, zorder=4)
submarine(ax, 0.42, 0.32, s=1.0)
for i, xx in enumerate(np.linspace(0.05, 0.25, 5)):
    ax.add_patch(Circle((xx, 0.3 + 0.02 * np.sin(i)), 0.012 + 0.004 * i, fc="none", ec="white", lw=1.5, zorder=3))
bubble(ax, 0.05, 0.62, 0.55, 0.3, "Debate still running on\nthe dock. We arrived\nthree weeks ago.", [(0.38, 0.62), (0.46, 0.62), (0.44, 0.47)], fs=10.5)
ax.text(0.02, 0.03, "2.", fontsize=14, fontweight="bold", color="white", zorder=12)

fig.text(0.5, 0.035, "“The question of whether machines can think is about as relevant as the question of whether submarines can swim.”  Edsger W. Dijkstra, 1984",
         ha="center", fontsize=10.5, style="italic", color=INK)
fig.suptitle("Can it think? Can it swim?", fontsize=16, fontweight="bold", x=0.02, ha="left", y=0.97)
fig.tight_layout(rect=(0, 0.06, 1, 0.94))
fig.savefig(OUT / "comic_01_submarine.png", dpi=200)
print("saved", OUT / "comic_01_submarine.png")
