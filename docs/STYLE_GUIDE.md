# Visual language for adapted and new charts

Use the user's requested style first. Otherwise borrow these concrete traits from the bundled Python figures, retaining legibility and the meaning of the data. This is a reusable design vocabulary inspired by the reconstructed examples, not a claim of an official Nature style standard.

## Color

Use a small, stable palette for categorical comparisons. Existing starting palettes are:

| Starting point | Colors | Typical role |
|---|---|---|
| Figure 07 | `#383838` · `#e8a625` · `#58a3ad` | Neutral control plus warm/cool contrasts |
| Figure 04 | `#7297d5` · `#e49386` · `#459b9e` · `#ece23e` | Four series; use dark outlines when pale colors have low contrast |
| Figure 05 | `#8aaa49` · `#b26462` · `#c8ac32` · `#8c8c8b` | Muted distributions with a neutral comparison |
| Figure 12 | `#edf4e7` → `#9ac87d` → `#4c9a48` → `#276335` | Ordered, low-to-high sequential values |
| Figure 19 | `#81b2c4` · `#8cbbb0` | Soft fills with dark text and structural lines |

Retain category-to-color mapping across panels. Use a sequential palette for magnitude, a diverging palette only for a meaningful midpoint, and discrete colors for categories. Do not cycle colors ambiguously when groups outgrow a palette; add direct labels or facets. Distinguish groups by marker/line shape as needed. Read the selected `style.json` and `plot.py`: some encodings and colormaps live in code.

## Structure and density

Start with a white background, restrained spines, sparse purposeful ticks, and dark labels. The examples combine observations with a summary (points + bars, distributions + boxes) and align complementary panels to save repeated labels. Keep shared category order and scales wherever comparisons require them.

Use the selected template's typography and line widths as the initial values, then assess at final display size. Canvas coordinates in `context.ax([left, top, width, height])` are pixels; Matplotlib text and line sizes are point-based. Enlarging or rearranging a canvas needs coordinated spacing and typography changes, not just copying positions.

Maintain enough space for labels, units, legends and colorbars. For dense figures, prefer aligned facets and shared legends over shrinking text. If too many observations overlap, consider transparency, smaller markers, binning or aggregation with a stated rule. Do not silently drop observations to mimic a reference density.

## Quantitative encodings

- Bars normally start at zero. Any break or truncated range must be visually explicit and appropriate.
- Bubble **area** should encode the size metric; Matplotlib scatter `s` is already an area in points squared. Explain units and show a meaningful size legend.
- Show SD, SEM or CI only with an explicit definition and appropriate calculation. Do not invent independent replicates.
- Density bandwidth and normalization affect comparison; document both. The bundled ridge defaults normalize peaks, so height is not sample count.
- Use paired lines only for actual pairings; use a common scale when comparing panels quantitatively.
- Show statistical annotations only from the current analysis, with enough method context to interpret them.

## Final inspection

Inspect the rendered PNG at the intended reading size, then zoom to investigate clipping or overlaps. Check the smallest labels, longest category names, extreme values, both ends of color/size legends, and the relationship between data and any inset. Verify export dimensions; inspect the SVG/PDF when vector editing or print use matters. Deliver executable code and a documented data mapping so style changes remain reproducible.
