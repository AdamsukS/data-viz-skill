# 03 · 多队列 PCoA 组合图

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**digitized** — 截图颜色连通区域提取的近似点；重叠点和组别形状无法完全识别

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 各队列的特征表或统一距离矩阵；每个样本的 study、control/IBD 组别和 ID。
- 跨队列归一化/批次处理方法、PCoA 坐标及轴解释比例。
- 原始 PERMANOVA 设计，包括队列效应、协变量和置换约束。

## 从原始数据到绘图输入

先完成跨队列统一和 PCoA；把坐标与 study/group 合并。本项目只绘图和汇总边缘分布，不做批次校正或 PERMANOVA。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure03.csv](data/figure03.csv)

`digitized` · 1180 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `study` | string | identifier | 队列标识，与 styles 中 study 顺序一致 |
| `group` | string | label | 实验组或细胞群；与样式一致 |
| `x` | number | ordination coordinate | 已转换的横轴坐标；不是原始特征矩阵 |
| `y` | number | ordination coordinate | 已转换的纵轴坐标 |

```csv
study,group,x,y
Puxi_cohort,IBD,0.35842044134727064,0.5426829268292683
Puxi_cohort,IBD,0.34871273712737133,0.5232384823848238
```

## 运行与替换数据

```bash
python -m figures.figure03.plot --format png svg
cp -R figures/figure03/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 3 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
