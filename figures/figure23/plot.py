"""Figure 23: temporal functions and distribution recovery.

Run from the repository root: python -m figures.figure23.plot
Input contracts and data provenance: README.md / README.en.md in this folder.
"""

from __future__ import annotations

import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from vizlib.common import clean, nums, subset


def _violin_panel(ax, rows, field, sizes, colors, title, ylabel=None, bounds=None, log=False):
    arrays = [nums(subset(rows, train_n=n), field) for n in sizes]
    parts = ax.violinplot(arrays, positions=np.arange(len(sizes)), widths=0.78,
                          showmeans=False, showmedians=True, showextrema=False,
                          bw_method=0.22)
    for body, color in zip(parts["bodies"], colors):
        body.set_facecolor(color)
        body.set_edgecolor("#333333")
        body.set_linewidth(0.8)
        body.set_alpha(0.88)
    parts["cmedians"].set_color("#222222")
    parts["cmedians"].set_linewidth(1.5)
    if bounds:
        for value in bounds:
            ax.axhline(value, color="#cf3e34", ls=(0, (4, 3)), lw=1.35, zorder=0)
    if log:
        ax.set_yscale("log")
    ax.set_title(title, fontsize=13, pad=7, fontweight="bold")
    ax.set_xticks(range(len(sizes)), [str(v) for v in sizes], rotation=35)
    ax.set_xlabel("Training functions, n", fontsize=10)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=10)
    clean(ax)
    ax.spines["left"].set_color("#777777")
    ax.spines["bottom"].set_color("#777777")
    ax.tick_params(labelsize=9, length=3)
    ax.grid(axis="y", color="#e8e8e8", lw=0.7, zorder=-5)


def draw(c, rows):
    """Draw worst-case curves above five distribution panels."""
    s = c.s
    sizes = [str(v) for v in s["training_sizes"]]
    curves = c.load("figure23_curves.csv")
    left, gap, panel_w = 70, 24, 282
    top_y, top_h = 105, 255
    bottom_y, bottom_h = 500, 300

    for index, (n, color) in enumerate(zip(sizes, s["colors"])):
        ax = c.ax([left + index * (panel_w + gap), top_y, panel_w, top_h])
        rr = subset(curves, train_n=n)
        x = nums(rr, "time")
        generated = nums(rr, "generated")
        reconstructed = nums(rr, "reconstructed")
        ax.scatter(x, generated, s=9, color=color, alpha=0.78, lw=0)
        ax.plot(x, reconstructed, color="#c83e35", lw=2.0, ls=(0, (5, 3)))
        ax.set_title(f"n = {n}", fontsize=14, fontweight="bold", pad=6)
        ax.set_xlim(0, 1)
        ax.set_ylim(s["curve_ylim"])
        ax.set_xticks([0, 0.5, 1.0])
        if index == 0:
            ax.set_ylabel("Function value", fontsize=11)
        else:
            ax.set_yticklabels([])
        if index == 2:
            ax.set_xlabel("Continuous coordinate / time", fontsize=11)
        clean(ax)
        ax.spines["left"].set_color("#777777")
        ax.spines["bottom"].set_color("#777777")
        ax.tick_params(labelsize=9, length=3)

    c.fig.legend(
        [Line2D([], [], marker="o", ls="none", ms=6, color=s["colors"][0]),
         Line2D([], [], color="#c83e35", lw=2, ls=(0, (5, 3)))],
        ["Generated function", "Parametric reconstruction"],
        loc="upper center", bbox_to_anchor=(0.5, 0.985), ncol=2,
        frameon=False, fontsize=12, handlelength=2.8,
    )

    fields = [
        ("amplitude", r"Amplitude, $A$", "Estimated value", s["target_bounds"]["amplitude"], False),
        ("damping", r"Damping, $\gamma$", None, s["target_bounds"]["damping"], False),
        ("frequency", r"Frequency, $\omega$", None, s["target_bounds"]["frequency"], False),
        ("shift", r"Vertical shift, $b$", None, s["target_bounds"]["shift"], False),
        ("mse", "Reconstruction MSE", "Mean squared error", None, True),
    ]
    for index, (field, title, ylabel, bounds, log) in enumerate(fields):
        ax = c.ax([left + index * (panel_w + gap), bottom_y, panel_w, bottom_h])
        _violin_panel(ax, rows, field, sizes, s["colors"], title, ylabel, bounds, log)

    c.text(30, 92, "a", fontsize=18, fontweight="bold", va="top")
    c.text(30, 485, "b", fontsize=18, fontweight="bold", va="top")
    c.text(70, 430, "Recovered distributions", fontsize=15, fontweight="bold", va="top")
    c.fig.legend(
        [Patch(fc=color, ec="#333333", lw=0.8) for color in s["colors"]]
        + [Line2D([], [], color="#cf3e34", ls=(0, (4, 3)), lw=1.5)],
        [f"n={n}" for n in sizes] + ["Target bounds"],
        loc="lower center", bbox_to_anchor=(0.5, 0.012), ncol=6,
        frameon=False, fontsize=10, handlelength=1.8,
    )


if __name__ == "__main__":
    from render import main
    main(default_figure=23)
