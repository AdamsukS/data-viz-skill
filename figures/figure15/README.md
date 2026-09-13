# 15 · 流式细胞术山脊矩阵

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**synthetic_fitted_curve** — 按截图峰位与多峰形态估计的混合高斯示例轮廓；不是原始流式数据

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 原始 FCS 文件或每个 event 的 marker 强度、样本 ID、细胞群和刺激 −/+ 条件。
- 补偿矩阵、门控层级、活细胞/双细胞排除及 marker 对应通道。
- 对数/logicle/arcsinh 变换及参数、阴性对照和密度归一化方法。

## 从原始数据到绘图输入

先完成补偿、门控与表达变换，再提供 marker/group/condition/value；也可提供 x/density。横轴上的 10 的幂标签假定输入已在对应对数坐标。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure15.csv](data/figure15.csv)

`synthetic_fitted_curve` · 12320 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `marker` | string | identifier | 通道对应的 marker 名称 |
| `group` | string | label | 实验组或细胞群；与样式一致 |
| `condition` | − / + | category | 未刺激/刺激；注意负号为 Unicode − |
| `x` | number | transformed expression | 已转换的横轴坐标；不是原始特征矩阵 |
| `density` | number ≥ 0 | row spacing | 分布的展示高度，不是样本量 |

```csv
marker,group,condition,x,density
IFN-γ,ILC3,−,-0.8,0.0
IFN-γ,ILC3,−,-0.7689,0.0
```

## 运行与替换数据

```bash
python -m figures.figure15.plot --format png svg
cp -R figures/figure15/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 15 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
