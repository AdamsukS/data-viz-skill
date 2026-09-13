# 16 · Cell-population expression ridgelines

[中文](README.md) | **English**

[← Gallery index](../../README.en.md)

![Preview](preview.png)

## Data provenance

**synthetic_fitted_curve** — Gaussian-mixture demonstration curves approximating visible modes; not original cell measurements.

Original experimental data were not supplied, and a paper/DOI has not been verified. These values demonstrate a reusable chart layout; they are not original research measurements or a pixel-identical reproduction.

## Original data you need

- Per-cell/event CD161, NKG2A, CD31, CD8, CD57 and CD28 expression, with sample IDs and c1–c8 labels.
- Vγ9Vδ2/Vδ1 definitions, preprocessing transformation, gating/clustering and composition of All cells.
- Sample weights and the median convention; peak height does not identify the number of cells.

## From raw data to plotting inputs

Define populations and expression transformation upstream; supply marker/group/value or x/density. Replacement-data median lines are estimated from input distributions rather than reused from the screenshot.

## Files and columns

`plot.py` contains the actual drawing code; `style.json` controls canvas, labels, colors and ordering; `data/` holds replaceable CSVs. `provenance.json` records per-file provenance, row count, SHA-256, columns and units.

### [figure16.csv](data/figure16.csv)

`synthetic_fitted_curve` · 11880 rows. Missing/NaN/Inf numeric values are unsupported; use UTF-8.

| Column | Type | Unit | Meaning |
|---|---|---|---|
| `marker` | string | identifier | Marker corresponding to the measurement channel |
| `group` | string | label | Experimental group or cell population; match style |
| `x` | number | transformed expression | Transformed x coordinate, not a raw feature matrix |
| `density` | number ≥ 0 | row spacing | Display height of a distribution, not sample count |

```csv
marker,group,x,density
CD161,c1,-1.0,0.0
CD161,c1,-0.9635,0.0
```

## Run and replace data

```bash
python -m figures.figure16.plot --format png svg
cp -R figures/figure16/data my_data
# Edit the relevant CSVs in my_data, then run:
python render.py --figure 16 --data-dir my_data --out my_output --format png svg pdf
```

Run commands from the repository root. Changing groups, genes, panel counts, sample-count labels or units also requires updating style.json and, where necessary, plot.py layout. A fixed canvas does not adapt to arbitrary group counts. Original statistical annotations are disabled by default when CSVs change. See the [main README](../../README.en.md) for summary modes.
