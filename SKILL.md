---
name: data-viz
description: Create reusable Python data visualizations from user datasets, choosing or adapting 19 chart templates or designing new charts with their restrained colors, layered data presentation, and compact layouts. Use for static charts, multi-panel figures, and editable PNG/SVG/PDF output across any domain.
---

# Data Viz

Turn the user's data and communication goal into an accurate, reusable visualization. This skill includes real plotting code, example data, style settings, and rendered previews for 19 templates. They are starting points, not a closed chart menu. Follow the user's requested chart, palette, language, and output requirements when supplied.

## Choose a route from the data

1. Inspect the available data locally: columns, observation unit, types, units, missing values, category counts, ranges, and any grouping/pairing. Establish what the viewer should compare, locate, or understand. Ask only for missing information that changes the interpretation; otherwise choose and state a reasonable mapping.
2. Read [template selection](docs/TEMPLATE_SELECTION.md), then the chosen `figures/figureNN/README.en.md` (or Chinese README), `style.json`, and `plot.py`. Inspect its `preview.png` when assessing visual fit. Load only relevant examples.
3. **Reuse** when the encoding and layout fit. **Adapt** when labels, group counts, panels, or encodings need changes. **Create** when no template fits: borrow the nearest drawing primitives and follow [the style guide](docs/STYLE_GUIDE.md). Do not force unrelated data into a biological story or an overcrowded template.

The biological field meanings and `raw_data_required` / `preprocessing` metadata describe source examples. Any domain is supported when data match the actual schema and mathematical constraints. Map concepts to required CSV column names, or modify the copied code and document the new schema. A column named `gene` can represent a product; a hierarchy need not be phylogenetic.

## Work in the user's project

Resolve `SKILL_ROOT` to the directory containing this file; commands below assume a POSIX shell. Use equivalent paths and commands on other platforms. Keep the installed templates intact and put modifications in a fresh project directory:

```bash
python3 "$SKILL_ROOT/scripts/prepare_workspace.py" --out ./visualization --figures 7
cd visualization
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

The helper copies a standalone runner, shared helpers, selected templates, and the new-figure scaffold. It refuses an existing destination. Omit `--figures` to start with shared helpers only. Use an existing suitable Python environment if available.

Prepare user-specific CSVs and style settings in this workspace. Store a reproducible preparation script when transforming source data. Use external data paths for sensitive or large inputs; do not commit or upload them merely to draw a chart. Bundled CSVs are clearly labeled demos, never substitutes for unavailable observations.

```bash
.venv/bin/python render.py --figure 7 --data-dir ./my_data --style ./my_style.json \
  --out ./output --format png svg pdf --annotations none --summary samples
```

Choose `--summary provided` only for intentional precomputed summaries; document whether error is SD, SEM, or CI. Existing grouped-bar schemas may still require `mean,error` columns; inspect the specific draw function and supply truthful summaries or adapt its input handling. Auxiliary tables must refer to the same observations and category keys. Change axis ranges, legends, titles, units, ordering, and any hardcoded labels in the copied code together with the data. Fixed layouts need edits for different panel/group counts.

For new charts, use a free ID and replace the starter with the requested design:

```bash
.venv/bin/python -m scripts.new_figure --id 20 --title "新的图表" --title-en "New chart"
.venv/bin/python -m figures.figure20.plot --format png svg pdf
```

Follow [the contributor guide](CONTRIBUTING.en.md) only when adding a reusable library example. User-specific charts do not require publishing a template or updating gallery fingerprints. New titles and documentation should describe the user's domain.

## Preserve meaning while borrowing style

Use the selected template's colors and density as an initial visual vocabulary. Retain interpretable encodings: quantitative bubble area, consistent scales across comparisons, clearly defined uncertainty, and legible labels. Add panels or enlarge the canvas when density exceeds readability. Density is useful comparisons per area, not arbitrary numbers of marks.

Do not transfer example P values, sample counts, correlations, fitted ellipses, significance stars, or biological labels into new results. For user data start with `--annotations none`; add statistics only when actually computed by a justified, recorded method. Example fingerprints are not a mechanism for validating new results. Log axes require positive values; trees require a valid hierarchy; missing values need an explicit treatment. The renderer does not perform domain analysis such as PCoA, PERMANOVA, sequencing, or flow-cytometry preprocessing.

## Render, inspect, and deliver

Render a PNG and inspect it at normal reading size; check labels, clipping, legend mapping, units, axis limits, overlap, density, and consistency with source values. Inspect at least representative extremes and recompute a displayed summary from input. Fix demonstrated problems and render again. Prefer vector SVG/PDF when the user wants editable or publication output; platform fonts can change appearance.

Deliver the requested image(s), runnable Python code, the data schema and mapping, a replay command, and necessary preparation steps. Include data only within the user's sharing scope. Explain estimated/simulated values or unperformed analysis when relevant. Summarize the chart choice and any meaningful adaptation. Never claim pixel identity with source images or original experimental data recovery.
