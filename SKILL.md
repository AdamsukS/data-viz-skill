---
name: data-viz
description: Visualize data by reusing and adapting bundled Python chart code wherever practical. Suggest useful missing inputs such as repeated measurements, and combine complementary information layers in one coherent figure when creative adaptation is needed. Use for static PNG/SVG/PDF figures across any domain.
---

# Data Viz

Reuse as much relevant plotting code as practical: start with an existing `plot.py`, `style.json`, and shared helpers, then adapt them to the user's data and communication goal. Preserve a suitable template's layout, palette and visual hierarchy when they work. For creative adaptations, a defining style is to show complementary perspectives together in one figure, often with overlaid marks sharing coordinates, supported by insets or margins when appropriate. Follow explicit user requests for a different chart or style.

## Choose a route from the data

1. Inspect the available data locally: columns, observation unit, types, units, missing values, category counts, ranges, and any grouping/pairing. Establish what the viewer should compare, locate, or understand. Identify whether additional available data would support a useful perspective, such as individual repeated measurements alongside a mean; make a concise, specific request when it would materially improve the figure.
2. Read [template selection](docs/TEMPLATE_SELECTION.md), then the chosen `figures/figureNN/README.en.md` (or Chinese README), `style.json`, and `plot.py`. Inspect its `preview.png` when assessing visual fit. Load only relevant examples.
3. Choose the valid template requiring the fewest changes, including a template whose unsupported layers or panels can simply be removed. A different domain, column naming, fewer groups, missing auxiliary data, or a few extra series is not a reason to design a new figure.
4. Apply this order: **replace data and labels → edit existing drawing code locally → add/remove elements within the composition → consider a new composition**. New composition is an exception for an explicit user request or substantial new variables/relationships that cannot be represented clearly by local changes. Explain the concrete mismatch before taking that route, and still reuse the nearest code. Never preserve an encoding that misrepresents the data just to retain a layout.

For natural-language data, read [text-data routing](docs/TEXT_DATA.en.md): reuse figure 20 for positioned words, 21 for word-group hierarchies, and 22 for document–word association flows. Use supplied coordinates/hierarchies/weights or derive them with a documented analysis; example positions and simulated links are not semantic evidence for a new corpus. Optional meshes and distribution panels can be disabled without rearranging the remaining layout.

The biological field meanings and `raw_data_required` / `preprocessing` metadata describe source examples. Any domain is supported when data match the actual schema and mathematical constraints. Map concepts to required CSV column names, or modify the copied code and document the new schema. A column named `gene` can represent a product; a hierarchy need not be phylogenetic.

## Work in the user's project

Resolve `SKILL_ROOT` to the directory containing this file; commands below assume a POSIX shell. Use equivalent paths and commands on other platforms. Keep the installed templates intact and put modifications in a fresh project directory:

```bash
python3 "$SKILL_ROOT/scripts/prepare_workspace.py" --out ./visualization --figures 7
cd visualization
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

The helper copies a standalone runner, shared helpers, selected templates, and the new-figure scaffold. It refuses an existing destination. Normally pass the selected template ID(s); omit `--figures` only after establishing that a new composition is necessary. Use an existing suitable Python environment if available.

Prepare user-specific CSVs and style settings in this workspace. Store a reproducible preparation script when transforming source data. Use external data paths for sensitive or large inputs; do not commit or upload them merely to draw a chart. Bundled CSVs are clearly labeled demos, never substitutes for unavailable observations.

```bash
.venv/bin/python render.py --figure 7 --data-dir ./my_data --style ./my_style.json \
  --out ./output --format png svg pdf --annotations none --summary samples
```

Choose `--summary provided` only for intentional precomputed summaries; document whether error is SD, SEM, or CI. Existing grouped-bar schemas may still require `mean,error` columns; inspect the specific draw function and supply truthful summaries or adapt its input handling. Auxiliary tables must refer to the same observations and category keys. Update labels, units, legends, ranges and hardcoded domain text to match the data. Keep existing axes rectangles, panel order, canvas proportions, typography and category colors by default. Different group counts alone do not require repositioning unaffected panels.

## Adapt incomplete or additional data in place

Map available inputs to the selected figure's layers/panels before editing. Before dropping a useful layer, explain what additional input would enable it and ask whether the user can provide it. For example: “Do you have the individual results from repeated experiments, with group and experiment/sample IDs? They would let us overlay observations and an appropriate variability summary on the existing bars.” Request existing data rather than prescribing new experiments just to fill a chart.

Ask for the minimum useful structure: individual values and units, group labels, independent experiment/batch or sample IDs, and pairing/time IDs if relevant. Distinguish independent experimental repeats from repeated readings of the same sample; do not treat technical repeats as independent observations. A supplied SD/SEM/CI needs its definition and relevant sample count; a mean alone cannot establish variability or a distribution.

For optional enhancements, continue rendering what the supplied data support while awaiting the answer; do not block a usable figure or repeatedly request unavailable data. If the input is essential to the requested interpretation, clarify before drawing that unsupported layer. Derive summaries only when observations and methods support them. If data remain unavailable, omit the layer with a brief explanation and remove its legend, labels and loading code.

- Means without replicate observations: keep bars or lines; remove fabricated sample dots. No uncertainty estimate: omit error bars, not replace missing errors with zero.
- Missing inset or auxiliary panel: skip its CSV load and drawing calls; remove its annotations. Keep the remaining panels in their original arrangement. Reclaim space locally only if the gap impairs readability or the user requests it.
- Fewer groups: update grouping loops, positions, ticks and legends locally; preserve colors of retained groups. A few additional groups/series: extend the same encoding and legend before adding a new panel or chart type.
- Missing individual values: use an explicit missing-data treatment (for example a line gap), not zero filling. Missing values in a bubble matrix are not zero-sized observations unless the data really mean zero.

The bundled renderer does not automatically handle absent columns or auxiliary files. Patch the copied `draw` function and relevant input checks/load calls so only retained elements require data; do not insert dummy CSV values to pass validation. If a missing variable is essential to the selected encoding, choose another valid bundled template or ask for that input. Do not infer pairings, uncertainty, hierarchy, or statistics from appearance.

## Exceptional new compositions

Use this route when the new-information threshold above is met, or the user explicitly asks for a new design. Reuse suitable code from one or more modules wherever practical. Plan the complementary perspectives first: what does each layer reveal about the same entities or observations, what data support it, and which coordinates or keys connect it to the others? Prefer combining compatible layers in one figure over defaulting to a collection of separate single-purpose charts.

Examples include raw points + a mean + justified uncertainty; distribution shape + a box summary + observations; or a scatter relationship + an appropriate fitted trend + marginal distributions. In text figures, position, category color, emphasis and association links can show different perspectives when each has a defined source. Share axes when units and scales are compatible; otherwise retain clear linked margins, insets or aligned panels within the figure. Do not force unrelated quantities onto one axis. See [the style guide](docs/STYLE_GUIDE.md) for concrete layering patterns and legibility checks.

Start by extending the nearest copied module; use the scaffold only when that is less suitable. For a separate new module, choose a free ID:

```bash
.venv/bin/python -m scripts.new_figure --id 24 --title "新的图表" --title-en "New chart"
.venv/bin/python -m figures.figure24.plot --format png svg pdf
```

Follow [the contributor guide](CONTRIBUTING.en.md) only when adding a reusable library example. User-specific charts do not require publishing a template or updating gallery fingerprints. New titles and documentation should describe the user's domain.

## Preserve meaning while borrowing style

Retain the selected template's colors, density and visual hierarchy. Layer complementary information deliberately: use draw order, transparency, restrained line weights and consistent category colors so observations, summaries and context remain distinguishable. Every added layer should answer a useful question and have data support. For a demonstrated overlap or clipping issue, adjust locally before reorganizing the composition. Keep interpretable encodings: quantitative bubble area, consistent scales, clearly defined uncertainty, and legible labels. Density is useful comparisons per area, not arbitrary numbers of marks.

Do not transfer example P values, sample counts, correlations, fitted ellipses, significance stars, or biological labels into new results. For user data start with `--annotations none`; add statistics only when actually computed by a justified, recorded method. Example fingerprints are not a mechanism for validating new results. Log axes require positive values; trees require a valid hierarchy; missing values need an explicit treatment. The renderer does not perform domain analysis such as PCoA, PERMANOVA, sequencing, or flow-cytometry preprocessing.

## Render, inspect, and deliver

Render a PNG and compare its composition with the selected template's preview. Check that layout changes are justified by data, readability or the user's request; undo incidental redesigns. Inspect at normal reading size for labels, clipping, legend mapping, units, axis limits, overlap, density, and consistency with source values. For removed layers, check that no stale legends, statistics or missing-file dependencies remain. Inspect representative extremes and recompute a displayed summary when applicable. Fix demonstrated problems and render again. Prefer vector SVG/PDF when the user wants editable or publication output; platform fonts can change appearance.

Deliver the requested image(s), runnable Python code, the data schema and mapping, a replay command, and necessary preparation steps. Name the reused modules and explain what each information layer shows; summarize added/removed elements and meaningful layout changes. Mention missing data that prevented a useful layer and the specific inputs that could enable it, without repeating requests the user has already declined. Include data only within the user's sharing scope. Explain estimated/simulated values or unperformed analysis when relevant. Never claim pixel identity with source images or original experimental data recovery.
