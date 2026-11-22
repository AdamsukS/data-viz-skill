# Visual language for adapted and new charts

Use the user's requested style first and reuse existing plotting code wherever practical. Preserve suitable template layouts and visual settings. When creative changes are needed, emphasize complementary information layered into one coherent figure. This is a reusable visual language, not an official Nature style standard.

## Compact canvas, statistical content, external explanation

Keep adapted/new figures moderately compact. Trim unused outer margins, reduce oversized gutters, align related plotting regions and share redundant legends or axis labels. Reclaim space left by removed titles or unavailable layers. Preserve readable type, uncropped ticks and enough separation between marks; a fixed shrink percentage is not a quality criterion.

The figure's information density should come from measured dimensions and statistical encodings, such as individual observations, distributions, estimates, uncertainty, associations and group comparisons. Do not fill space with analysis, conclusions, prose descriptions, caption blocks, chart titles, panel subtitles or explanatory callouts. Place them in the response or a separate `figure_caption.md` alongside the export. Textual statistical tests and significance explanations also belong there by default.

Retain essential axis names and units, ticks, concise legend/colorbar keys, short category/data identifiers and panel markers. Words that identify actual observations in a language-data chart can remain, but paragraphs and descriptive topic summaries should not replace statistical encodings. Add text annotations beyond these essentials only when the user explicitly requests them.

Reference previews preserve their source compositions; they do not override these defaults for user outputs. Inspect the copied `set_title`, `suptitle`, `text`, `annotate` and figure-level text calls, plus style fields such as `heading` and `panel_label`. Remove narrative text selectively while retaining essential labels. `--annotations none` alone is insufficient to strip hardcoded text. Do not remove every text artist indiscriminately.

## Multi-panel markers

Label distinct main panels `(a)`, `(b)`, `(c)`, … from left to right and top to bottom. Keep marker size, weight and placement consistent, near the upper-left edge of each panel in a small reserved gutter. Markers must not overlap observations, ticks or legends. Use the parenthesized form instead of bare letters or descriptive subtitles. Explain the marker-to-panel mapping in the external caption.

Treat a scatter plot with its marginal axes as one panel unless the user requests otherwise. Colorbars and supporting insets do not automatically receive separate letters. After deleting, adding or reordering panels, update the marker sequence and external caption together. A single standalone chart needs no panel marker by default.

## Multiple perspectives in one figure

Identify a main question, then combine supported perspectives on the same observations or entities. Shared-coordinate overlays are preferred when scales and units are compatible. A compact inset, marginal distribution or aligned panel can carry a perspective that needs its own scale while remaining part of the same figure.

| Composition | Perspectives brought together | Required inputs / nearby code |
|---|---|---|
| Raw points over bars with error caps | Individual outcomes, group mean and variability | Repeated observations with group/sample IDs, or separately justified summaries; figures 01/07/08 |
| Half-violin + box + points/rug | Distribution shape, quantiles and individual observations | Observations from the same population; figures 05/17 |
| Scatter + trend/interval + marginals | Association, estimated trend/uncertainty and one-variable distributions | Paired x/y observations and a justified fit when used; reuse figures 02/03/13 and add only supported layers |
| Word positions + color/emphasis + links | Spatial or semantic placement, categories and relationships | Defined coordinates, label/category metadata and actual links; figures 20/22 |
| Bubble matrix with color and area | Two metrics for the same category pairs | Documented metrics and separate legends; figure 12 |

Check which inputs exist before designing the layers. If repeated experiment results would enable points and variability, ask for individual values with group, experiment/sample IDs and units. If only means exist and no additional data are available, keep the mean layer; do not invent a distribution. Do not request unnecessary new measurements solely to fill a template.

Make layers readable through draw order, restrained opacity, marker size and line weight: for example, a pale distribution behind a narrow summary and visible observations. Keep category colors consistent across layers. Avoid hiding extreme observations under fills, implying pairing without IDs, or using arbitrary dual-axis scaling to make unrelated trends overlap. Add a layer for a distinct useful perspective, not merely to make the image denser.

## Color

Keep the selected template's palette and retained categories' color assignments by default. Extend it only for added categories or a necessary encoding change. Available palettes are:

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

Retain suitable typography, line widths, panel order and proportions. Adjust axes rectangles locally to tighten excess whitespace and remove space previously reserved for titles or prose. Keep the remaining arrangement when reclaiming a missing panel's space. Canvas coordinates in `context.ax([left, top, width, height])` are pixels; Matplotlib text and line sizes are point-based.

Maintain enough space for labels, units, legends and colorbars. Resolve overlap locally with spacing, label wrapping or marker adjustments before enlarging the canvas or creating facets. Aggregation or binning needs a stated rule. Do not silently drop observations or fill missing data to mimic a reference density. Change the layout only for a demonstrated readability/encoding problem, substantial new information, or a user request.

## Quantitative encodings

- Bars normally start at zero. Any break or truncated range must be visually explicit and appropriate.
- Bubble **area** should encode the size metric; Matplotlib scatter `s` is already an area in points squared. Explain units and show a meaningful size legend.
- Show SD, SEM or CI only with an explicit definition and appropriate calculation. Do not invent independent replicates.
- Density bandwidth and normalization affect comparison; document both. The bundled ridge defaults normalize peaks, so height is not sample count.
- Use paired lines only for actual pairings; use a common scale when comparing panels quantitatively.
- Statistical layers must come from the current data. Put method context, test results and interpretive annotations in the external caption by default; include extra statistical text in the image only when explicitly requested.

## Final inspection

Compare the rendered composition against the selected preview and account for meaningful layout changes. Verify a compact but readable canvas, no embedded titles/captions/analysis, and a complete consistent `(a)`, `(b)`, … sequence for main panels. Check that each overlaid perspective has supporting data and can be distinguished from the others; verify shared units, populations and entity keys. Inspect the smallest labels, longest category names, extreme values, legends and insets at the intended reading size. Removed layers must leave no stale legend entries or statistical text. Verify export dimensions and inspect the actual PNG/SVG/PDF. Deliver code and data mapping, with panel descriptions and analysis outside the image.
