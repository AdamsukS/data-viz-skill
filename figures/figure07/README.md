# 07 · 基因表达分组柱状图

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**screenshot_estimate** — 柱高 误差 散点人工估读

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 每个基因、基因型、Day15 样本的 mRNA 测量和生物学重复 ID。
- 原始 Ct/表达量、内参和归一化方法；保留技术重复与生物学重复的对应关系。
- 组间比较与多重检验、误差定义；P 值不能从图片恢复计算过程。

## 从原始数据到绘图输入

先归一化 mRNA 表达，再填每组重复值；默认重算均值和 SEM，不做新的显著性检验。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure07.csv](data/figure07.csv)

`screenshot_estimate` · 91 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `category` | string | label | 分类/条件；与样式顺序一致 |
| `group` | string | label | 实验组或细胞群；与样式一致 |
| `sample` | string | identifier | 示例重复编号，真实数据应保留真实样本 ID |
| `value` | number | normalized expression / fold change | 单个观测值；单位及归一化见本图原始数据要求 |
| `mean` | number | normalized expression / fold change | 组均值；相同组每行重复同一数值 |
| `error` | number ≥ 0 | normalized expression / fold change | 指定的误差幅度；需注明 SD/SEM/CI |

```csv
category,group,sample,value,mean,error
ubq-1,Wild-type,1,0.55,1,0.03
ubq-1,Wild-type,2,0.83,1,0.03
```

## 运行与替换数据

```bash
python -m figures.figure07.plot --format png svg
cp -R figures/figure07/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 7 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
