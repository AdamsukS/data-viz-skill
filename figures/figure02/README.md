# 02 · PCoA 与边缘箱线图

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**digitized** — 截图颜色连通区域提取的近似点；遮挡点不可恢复；椭圆由截图估读

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 每个样本的丰度/特征矩阵或样本间距离矩阵，以及样本 ID 到组别的映射。
- 距离度量、变换方法、PCoA 实现、PCoA1/2 坐标和各轴解释比例。
- PERMANOVA 的模型、置换次数、分层信息，以及椭圆计算约定。

## 从原始数据到绘图输入

先在原分析流程中计算 PCoA，再把前两轴坐标写入 x/y。本项目不运行 PCoA 或 PERMANOVA；新数据的椭圆使用二维协方差近似。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure02.csv](data/figure02.csv)

`digitized` · 94 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `group` | string | label | 实验组或细胞群；与样式一致 |
| `x` | number | ordination coordinate | 已转换的横轴坐标；不是原始特征矩阵 |
| `y` | number | ordination coordinate | 已转换的纵轴坐标 |

```csv
group,x,y
HC,0.28514867617107936,0.25433960354707724
HC,0.440606896551724,0.2349796530306275
```

## 运行与替换数据

```bash
python -m figures.figure02.plot --format png svg
cp -R figures/figure02/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 2 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
