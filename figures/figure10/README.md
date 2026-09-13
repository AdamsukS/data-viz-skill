# 10 · 环形系统发育树与分类注释

**中文** | [English](README.en.md)

[← 返回总目录](../../README.md)

![Preview](preview.png)

## 数据来源

**synthetic** — 模拟树拓扑 分支长度及叶节点注释；仅复现图式，不能用于系统发育推断

原始实验数据未提供；论文/DOI 尚未核实。这里的值仅用于图式复用，不是原始研究数据，也不构成像素完全一致的复现。

## 需要哪些原始数据

- 原始 Newick/Nexus 系统发育树：真实拓扑、枝长、根和叶节点唯一编号。
- 每个叶节点的 phylum、WGS/MAG/SAG 类型和样本检出情况。
- 检出类别的阈值和样本范围；树的末端顺序与图例计数。

## 从原始数据到绘图输入

把 Newick/Nexus 转为 node/parent/length 的边表，并按 tip ID 合并注释。保留根、枝长单位与排序；此代码不做树推断。

## 文件与字段

`plot.py` 是本图实际绘图代码；`style.json` 控制画布、标签、颜色和分类顺序；`data/` 保存可替换 CSV。`provenance.json` 逐文件记录来源类别、行数、SHA-256、字段含义与单位。

### [figure10.csv](data/figure10.csv)

`synthetic` · 1119 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `node` | string | identifier | 唯一节点 ID；不能命名为 root |
| `parent` | string | identifier | 父节点 ID 或隐含根 root |
| `length` | number ≥ 0 | tree-specific | 从父节点到该节点的枝长；必须指定单位 |
| `phylum` | string | taxonomy | 门分类；与 style.phyla 中名称一致 |

```csv
node,parent,length,phylum
n0,root,0.14456846775405963,Other
n1,n0,0.11218894987123149,Other
```

### [figure10_leaves.csv](data/figure10_leaves.csv)

`synthetic` · 565 行。空值/NaN/Inf 不受支持；字段使用 UTF-8。

| 字段 | 类型 | 单位 | 含义 |
|---|---|---|---|
| `node` | string | identifier | 唯一节点 ID；不能命名为 root |
| `order` | unique number | ordering | 圆周上叶节点顺序，不可重复 |
| `phylum` | string | taxonomy | 门分类；与 style.phyla 中名称一致 |
| `type` | WGS / MAG / SAG | category | 基因组类型；图 10 使用 |
| `presence` | 0 / 1 / 2 | category | 图10的缺失/至少1/至少10样本检出类别 |
| `fraction` | number [0, 1] | fraction | 图11检出比例；颜色范围默认 0–0.6 |
| `bsh` | 0 / 1 | boolean | 图11的 bsh 缺失/存在 |

```csv
node,order,phylum,type,presence,fraction,bsh
n3,0,Other,MAG,0,0.0024,1
n5,1,Other,MAG,1,0.0872,1
```

## 运行与替换数据

```bash
python -m figures.figure10.plot --format png svg
cp -R figures/figure10/data my_data
# 修改 my_data 内所有对应 CSV，再运行：
python render.py --figure 10 --data-dir my_data --out my_output --format png svg pdf
```

命令均从仓库根目录执行。修改组名、基因名、面板数、样本量标签或量纲时，也要修改 `style.json` 与必要的 `plot.py` 布局；固定画布不会自动容纳任意数量的分组。示例原图统计标注在 CSV 改动后默认停用。完整统计模式说明见[总 README](../../README.md)。
