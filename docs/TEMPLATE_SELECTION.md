# Choose a starting template

Select by the user's variables and communication goal, not the biological titles of the source examples. Read only the selected figure's schema and implementation. The previews in [the gallery](GALLERY.en.md) show the existing composition; they do not limit the new chart's subject or design.

| IDs | Data / question | Reusable encoding | Adaptation to inspect |
|---|---|---|---|
| [01](../figures/figure01/README.en.md), [07](../figures/figure07/README.en.md), [08](../figures/figure08/README.en.md) | Compare grouped measurements | Bars, individual observations, error caps | Category/group counts, summary mode, jitter, old annotations |
| [06](../figures/figure06/README.en.md) | Groups with a large scale gap | Broken-axis bars with observations | Use a break only when justified and clearly labeled; consider log scale or panels |
| [02](../figures/figure02/README.en.md), [03](../figures/figure03/README.en.md) | Association between two numeric variables, across groups/cohorts | Scatter plus marginal summaries; repeated panels | Coordinates can be arbitrary variables; remove PCoA labels, variance percentages and irrelevant statistical text |
| [04](../figures/figure04/README.en.md) | Compare change along time or an ordered numeric axis | Lines, uncertainty, a summary inset | Sort time; avoid connecting unrelated categories; derive inset from the same data |
| [05](../figures/figure05/README.en.md), [17](../figures/figure17/README.en.md) | Compare distributions and their observations | Half-violin / raincloud / density + box + rug | Consistent bandwidth and scales; density, rug and summary must describe the same samples |
| [09](../figures/figure09/README.en.md) | Compare two metrics with different units | Nested bars and dual axes | Dual-axis association can mislead; prefer aligned panels when it clarifies comparisons |
| [10](../figures/figure10/README.en.md), [11](../figures/figure11/README.en.md) | Hierarchy with categorical or numeric annotations | Circular branches and annotation rings | Valid node/parent tables, meaningful branch lengths, matching leaf IDs; remap biological keys/legends |
| [12](../figures/figure12/README.en.md) | Two categorical dimensions and two metrics | Bubble matrix, color and area | Define size/color units and normalization; inspect size mapping and hardcoded panels |
| [13](../figures/figure13/README.en.md) | Positive variables spanning orders of magnitude | Log scatter and marginal histograms | Positive finite inputs; meaningful binning and tick labels |
| [14](../figures/figure14/README.en.md), [15](../figures/figure15/README.en.md), [16](../figures/figure16/README.en.md) | Many ordered group distributions | Ridgeline series / matrix | Accept density curves or grouped values; peak-normalized heights are not sample counts |
| [18](../figures/figure18/README.en.md) | Many grouped summaries across facets | Faceted boxes | Five-number ordering, group/panel labels and sample counts |
| [19](../figures/figure19/README.en.md) | Several linked measurements on common entities | Correlation, paired endpoints, bubbles and bars | Keep entity ordering consistent; use only panels supported by actual data; adapt fixed labels and correlations |

## Adapt or create

Use a direct template for matching encodings and manageable category counts. Modify the copied `plot.py` when fixed positions, hardcoded labels, group loops or axis choices no longer fit. `style.json` is not a universal layout engine.

For an unfamiliar chart, start from the nearest primitives in `vizlib/common.py` or one or two figure modules. A new slope chart can borrow paired endpoints from figure 19; an operational dashboard can combine figure 4's lines and figure 12's matrix without biological labels. Keep only encodings relevant to the user's question. A simpler single panel may communicate more than a dense composite.

Use [the style guide](STYLE_GUIDE.md) for palette, hierarchy and information density. For schemas, use the per-figure **Files and columns** sections. The **Source-study context** sections are background, not input requirements for other domains.
