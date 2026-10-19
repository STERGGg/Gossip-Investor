"""
COMICS 02 to 05  Original cartoons drawn in matplotlib for The AI Expansion.
02  The money merry go round (circular AI deals)
03  The IOU (Oracle and OpenAI)
04  The plug (power and the grid)
05  The robot intern (productivity)
Characters are generic shapes and labels; no real logos or likenesses are drawn.
"""
from common import *
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Polygon, FancyArrowPatch, Ellipse, Wedge

INKC = "#1d1d1b"

def panel(ax, bg="#f4f1ea"):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    ax.add_patch(Rectangle((0, 0), 1, 1, fc=bg, zorder=0))
    for sp in ax.spines.values():
        sp.set_linewidth(3); sp.set_color(INKC)

def bubble(ax, x, y, w, h, text, tip, fs=10.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.05", fc="white", ec=INKC, lw=1.8, zorder=10))
    bx = min(max(tip[0], x + 0.04), x + w - 0.04)
    ax.add_patch(Polygon([(bx - 0.025, y), (bx + 0.025, y), tip], fc="white", ec=INKC, lw=1.8, zorder=9))
    ax.plot([bx - 0.022, bx + 0.022], [y, y], color="white", lw=3, zorder=11)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, fontweight="bold", color=INKC, zorder=12)

def stick(ax, x, y, s=1.0, tie=None, arms="down", head="#f5d0b5"):
    fig = ax.figure; fig.canvas.draw(); bb = ax.get_window_extent(); r = bb.height / bb.width
    ax.add_patch(Ellipse((x, y + 0.2 * s), 0.09 * s * r, 0.09 * s, fc=head, ec=INKC, lw=1.8, zorder=7))
    ax.plot([x, x], [y + 0.155 * s, y + 0.04 * s], color=INKC, lw=2.2, zorder=6)
    ax.plot([x, x - 0.04 * s], [y + 0.04 * s, y - 0.05 * s], color=INKC, lw=2.2, zorder=6)
    ax.plot([x, x + 0.04 * s], [y + 0.04 * s, y - 0.05 * s], color=INKC, lw=2.2, zorder=6)
    if arms == "up":
        ax.plot([x - 0.06 * s, x, x + 0.06 * s], [y + 0.2 * s, y + 0.12 * s, y + 0.2 * s], color=INKC, lw=2.2, zorder=6)
    elif arms == "out":
        ax.plot([x - 0.07 * s, x, x + 0.07 * s], [y + 0.1 * s, y + 0.12 * s, y + 0.1 * s], color=INKC, lw=2.2, zorder=6)
    else:
        ax.plot([x - 0.05 * s, x, x + 0.05 * s], [y + 0.05 * s, y + 0.12 * s, y + 0.05 * s], color=INKC, lw=2.2, zorder=6)
    if tie:
        ax.add_patch(Polygon([(x, y + 0.15 * s), (x - 0.012 * s, y + 0.1 * s), (x, y + 0.08 * s), (x + 0.012 * s, y + 0.1 * s)], fc=tie, ec=INKC, lw=1, zorder=8))

def save(fig, name, title, caption):
    fig.suptitle(title, fontsize=15, fontweight="bold", x=0.02, ha="left", y=0.97)
    fig.text(0.5, 0.03, caption, ha="center", fontsize=10, style="italic", color=INKC)
    fig.tight_layout(rect=(0, 0.06, 1, 0.93)); fig.savefig(COMICS / name, dpi=200); plt.close(fig)

# ---------- 02 merry go round ----------
fig, ax = plt.subplots(figsize=(11, 5.6)); panel(ax, "#eef4fb")
ax.add_patch(Ellipse((0.5, 0.42), 0.62, 0.62 * 11 / 5.6 * 0.5, fc="#fde6c8", ec=INKC, lw=2.5, zorder=1))
pts = {"CHIP MAKER": (0.5, 0.80), "AI LAB": (0.82, 0.42), "CLOUD LANDLORD": (0.5, 0.08), "INVESTORS": (0.18, 0.42)}
cols = {"CHIP MAKER": "#1baf7a", "AI LAB": "#2a78d6", "CLOUD LANDLORD": "#e34948", "INVESTORS": "#6250d6"}
for name, (x, y) in pts.items():
    ax.add_patch(FancyBboxPatch((x - 0.1, y - 0.055), 0.2, 0.11, boxstyle="round,pad=0.01", fc=cols[name], ec=INKC, lw=2, zorder=5))
    ax.text(x, y, name, ha="center", va="center", color="white", fontweight="bold", fontsize=10.5, zorder=6)
arrows = [((0.62, 0.78), (0.8, 0.5), "invests $$$"), ((0.8, 0.34), (0.62, 0.12), "rents compute"), ((0.38, 0.12), (0.2, 0.34), "borrows to build"), ((0.2, 0.5), (0.38, 0.78), "buys chips")]
for (a, b, lab) in arrows:
    ax.add_patch(FancyArrowPatch(a, b, connectionstyle="arc3,rad=-0.35", arrowstyle="-|>", mutation_scale=22, lw=2.5, color=INKC, zorder=4))
for (a, b, lab), off in zip(arrows, [(0.06, 0.03), (0.05, -0.03), (-0.06, -0.03), (-0.06, 0.03)]):
    ax.text((a[0] + b[0]) / 2 + off[0], (a[1] + b[1]) / 2 + off[1], lab, ha="center", va="center", fontsize=9.5, style="italic", zorder=6,
            bbox=dict(fc="white", ec="none", alpha=0.85, pad=1.5))
stick(ax, 0.5, 0.33, s=0.75, tie="#eda100", arms="up")
bubble(ax, 0.39, 0.6, 0.22, 0.08, "Revenue is up again!", (0.5, 0.53), fs=9.5)
stick(ax, 0.05, 0.03, s=0.45, arms="out")
bubble(ax, 0.015, 0.19, 0.15, 0.11, "Whose revenue,\nexactly?", (0.05, 0.14), fs=8.5)
save(fig, "comic_02_merry_go_round.png", "The money merry go round", "When the same dollar is counted as an investment, a sale and a backlog, the ride looks faster than it is.")

# ---------- 03 the IOU ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))
ax = axes[0]; panel(ax, "#fbf3e6")
ax.add_patch(Rectangle((0.08, 0.3), 0.84, 0.05, fc="#8b5a2b", ec=INKC, lw=2, zorder=3))
ax.add_patch(Rectangle((0.14, 0.0), 0.04, 0.3, fc="#6b4421", ec=INKC, lw=1.5, zorder=2)); ax.add_patch(Rectangle((0.82, 0.0), 0.04, 0.3, fc="#6b4421", ec=INKC, lw=1.5, zorder=2))
for i in range(6):
    ax.add_patch(FancyBboxPatch((0.2 + i * 0.1, 0.36), 0.08, 0.12, boxstyle="round,pad=0.005", fc="#3a3a3a", ec=INKC, lw=1.5, zorder=4))
    ax.add_patch(Rectangle((0.215 + i * 0.1, 0.4), 0.05, 0.01, fc="#1baf7a", zorder=5))
ax.text(0.5, 0.52, "$300bn of computing", ha="center", fontsize=10, fontweight="bold")
stick(ax, 0.12, 0.55, s=0.9, tie="#2a78d6", arms="out"); ax.text(0.12, 0.47, "AI LAB", ha="center", fontsize=8.5, fontweight="bold")
stick(ax, 0.88, 0.55, s=0.9, tie="#e34948"); ax.text(0.88, 0.47, "WAITER", ha="center", fontsize=8.5, fontweight="bold")
bubble(ax, 0.03, 0.82, 0.45, 0.13, "We'll take everything.\nAnd another kitchen.", (0.14, 0.78), fs=9.5)
bubble(ax, 0.52, 0.84, 0.45, 0.1, "Excellent choice, sir!", (0.86, 0.78), fs=9.5)
ax.text(0.03, 0.03, "1.", fontsize=13, fontweight="bold")
ax = axes[1]; panel(ax, "#fbf3e6")
ax.add_patch(Rectangle((0.08, 0.3), 0.84, 0.05, fc="#8b5a2b", ec=INKC, lw=2, zorder=3))
ax.add_patch(Rectangle((0.14, 0.0), 0.04, 0.3, fc="#6b4421", ec=INKC, lw=1.5, zorder=2)); ax.add_patch(Rectangle((0.82, 0.0), 0.04, 0.3, fc="#6b4421", ec=INKC, lw=1.5, zorder=2))
ax.add_patch(Polygon([(0.42, 0.36), (0.6, 0.36), (0.62, 0.62), (0.44, 0.62)], fc="white", ec=INKC, lw=2, zorder=5))
ax.text(0.53, 0.55, "I.O.U.", ha="center", fontsize=13, fontweight="bold", zorder=6)
ax.text(0.53, 0.46, "$60bn a year\nfrom 2027", ha="center", fontsize=9, zorder=6)
stick(ax, 0.12, 0.55, s=0.9, tie="#2a78d6"); stick(ax, 0.88, 0.55, s=0.9, tie="#e34948", arms="up")
bubble(ax, 0.04, 0.8, 0.44, 0.14, "Of course we can pay.\n800 million users!", (0.14, 0.78), fs=9.5)
bubble(ax, 0.55, 0.8, 0.42, 0.14, "...who mostly\ndon't pay?", (0.86, 0.78), fs=10)
ax.text(0.03, 0.03, "2.", fontsize=13, fontweight="bold")
save(fig, "comic_03_iou.png", "The I.O.U.", "Oracle borrowed to build the kitchen. The customer pays from 2027, out of revenue it has not earned yet.")

# ---------- 04 the plug ----------
fig, ax = plt.subplots(figsize=(11, 5.4)); panel(ax, "#f2f2f2")
ax.add_patch(Rectangle((0.05, 0.12), 0.48, 0.55, fc="#cfd8e3", ec=INKC, lw=2.5, zorder=2))
for r in range(4):
    for c in range(6):
        ax.add_patch(Rectangle((0.08 + c * 0.075, 0.18 + r * 0.115), 0.055, 0.08, fc="#3a3a3a", ec=INKC, lw=1, zorder=3))
        ax.add_patch(Circle((0.095 + c * 0.075, 0.24 + r * 0.115), 0.006, fc="#1baf7a", zorder=4))
ax.text(0.29, 0.71, "GIGA DATA CENTRE (30 GW)", ha="center", fontsize=11, fontweight="bold")
xs = np.linspace(0.53, 0.86, 50); ax.plot(xs, 0.25 + 0.05 * np.sin((xs - 0.53) * 18), color=INKC, lw=6, zorder=2)
ax.add_patch(Rectangle((0.86, 0.2), 0.05, 0.1, fc="#555", ec=INKC, lw=2, zorder=3))
ax.add_patch(FancyBboxPatch((0.9, 0.18), 0.06, 0.14, boxstyle="round,pad=0.005", fc="white", ec=INKC, lw=2, zorder=2))
ax.add_patch(Circle((0.93, 0.27), 0.007, fc=INKC, zorder=3)); ax.add_patch(Circle((0.93, 0.23), 0.007, fc=INKC, zorder=3))
ax.text(0.93, 0.13, "the grid", ha="center", fontsize=9, style="italic")
stick(ax, 0.72, 0.42, s=0.9, tie="#2a78d6", arms="up")
bubble(ax, 0.58, 0.72, 0.38, 0.17, "Just plug it in.\nHow hard can it be?", (0.72, 0.64), fs=11)
ax.text(0.75, 0.05, "Transformers: 2 year wait.  New lines: 4 to 8 years.", ha="center", fontsize=9, color="#e34948", fontweight="bold")
save(fig, "comic_04_plug.png", "Just plug it in", "You can raise a hundred billion dollars in a week. You cannot build a power line in one.")

# ---------- 05 robot intern ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))
for i, ax in enumerate(axes):
    panel(ax, "#eef6f1")
    ax.add_patch(Rectangle((0.15, 0.25), 0.7, 0.05, fc="#8b5a2b", ec=INKC, lw=2, zorder=3))
    ax.add_patch(Rectangle((0.55, 0.3), 0.22, 0.17, fc="#2b2b2b", ec=INKC, lw=2, zorder=4))
    ax.add_patch(Rectangle((0.57, 0.32), 0.18, 0.13, fc="#9fd3ff" if i == 0 else "#ffd6d6", zorder=5))
    ax.add_patch(FancyBboxPatch((0.3, 0.3), 0.14, 0.18, boxstyle="round,pad=0.01", fc="#b8c4cf", ec=INKC, lw=2, zorder=4))
    ax.add_patch(FancyBboxPatch((0.32, 0.5), 0.1, 0.09, boxstyle="round,pad=0.01", fc="#b8c4cf", ec=INKC, lw=2, zorder=4))
    ax.add_patch(Circle((0.35, 0.55), 0.012, fc="#e34948", zorder=5)); ax.add_patch(Circle((0.39, 0.55), 0.012, fc="#e34948", zorder=5))
    ax.plot([0.37, 0.37], [0.59, 0.63], color=INKC, lw=2); ax.add_patch(Circle((0.37, 0.64), 0.01, fc="#eda100", ec=INKC, zorder=5))
    ax.text(0.37, 0.37, "INTERN\nv4", ha="center", fontsize=7.5, fontweight="bold", zorder=6)
stick(axes[0], 0.82, 0.55, s=0.9, tie="#6250d6")
bubble(axes[0], 0.05, 0.76, 0.6, 0.17, "I wrote 400 pages of\nstrategy in 9 seconds.", (0.37, 0.66), fs=10)
axes[0].text(0.66, 0.38, "400 pp", ha="center", fontsize=9, fontweight="bold", zorder=6); axes[0].text(0.03, 0.03, "1.", fontsize=13, fontweight="bold")
stick(axes[1], 0.85, 0.5, s=0.9, tie="#6250d6", arms="up")
bubble(axes[1], 0.32, 0.8, 0.46, 0.15, "Great. Now who has\ntime to read it?", (0.78, 0.8), fs=10)
axes[1].text(0.66, 0.38, "Productivity\n+1%", ha="center", fontsize=8.5, fontweight="bold", zorder=6); axes[1].text(0.03, 0.03, "2.", fontsize=13, fontweight="bold")
save(fig, "comic_05_robot_intern.png", "The robot intern", "Producing more is easy. Turning it into output the economy can measure is the slow part.")
print("done")
