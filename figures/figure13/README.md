# 13 · 双对数散点与边缘直方图

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**synthetic** — 模拟相关散点；样本量沿用截图标签，不代表获得了原始样本

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 每个 genome 的 ID、SAG/MAG/WGS 类别、总长度 bp 和 CDS 数量。
- 原始长度/计数，以及 corrected 的校正方法和质量筛选规则。
- 真实样本量、拟合方法、残差尺度，以及用于组间残差检验的设计。

## 从原始数据到绘图输入

先完成 corrected 校正并输入严格正值。程序在 log10 空间拟合直线和计算残差；不运行残差组间显著性检验。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure13.csv](data/figure13.csv)

`synthetic` · 5678 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `group` | string | label | 实验组或细胞群；与样式一致 |
| `genome_bp` | number > 0 | bp | 已按原方法校正的基因组总长度 |
| `cds` | number > 0 | count | 已校正的预测 CDS 数量 |

```csv
group,genome_bp,cds
MHQ SAG (N=226),1312058.88,1175.16
MHQ SAG (N=226),3615231.72,3191.64
```

## 运行与替换数据

```bash
python -m figures.figure13.plot --format png svg
cp -R figures/figure13/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 13 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
