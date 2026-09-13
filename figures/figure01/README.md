# 01 · 空心柱状图与散点

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**screenshot_estimate** — 截图人工估读；柱高及误差按图估计；散点数量可能有遮挡

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 样本/动物编号、处理组及每个重复的 PCNA+ 细胞计数。
- 计数区域与长度、300 μm 归一化方法、重复单位及排除规则。
- 原始组间比较方法、误差类型和多重检验设置。

## 从原始数据到绘图输入

输入长表的 value 为样本计数；新 CSV 默认重算均值和 SEM。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure01.csv](data/figure01.csv)

`screenshot_estimate` · 40 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `category` | string | label | 分类/条件；与样式顺序一致 |
| `group` | string | label | 实验组或细胞群；与样式一致 |
| `sample` | string | identifier | 示例重复编号，真实数据应保留真实样本 ID |
| `value` | number | cells / 300 μm | 单个观测值；单位及归一化见本图原始数据要求 |
| `mean` | number | cells / 300 μm | 组均值；相同组每行重复同一数值 |
| `error` | number ≥ 0 | cells / 300 μm | 指定的误差幅度；需注明 SD/SEM/CI |

```csv
category,group,sample,value,mean,error
,Cont,1,130,205,23
,Cont,2,142,205,23
```

## 运行与替换数据

```bash
python -m figures.figure01.plot --format png svg
cp -R figures/figure01/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 1 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
