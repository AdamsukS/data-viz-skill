# Scientific Figure Gallery

**中文** | [English](README.en.md)

可复用的 Python 科研绘图案例库。当前收录 19 张复现图，每张图拥有**独立绘图代码、CSV 示例数据、JSON 样式、双语数据说明和预览图**。支持替换数据和新增图式，统一导出 PNG、SVG、PDF。

这些案例来自位图参考的近似重绘，**不是像素完全一致的复刻**。当前没有取得原始实验数据；CSV 包括截图估读、数字化提取、模拟观测和拟合示例曲线。树拓扑也是模拟的。每张图都明确记录了来源，示例值不能用于原研究的统计结论。

[查看全部预览](docs/GALLERY.md) · [每张图需要的原始数据](docs/DATA.md) · [新增图表](CONTRIBUTING.md)

## 快速开始

需要 Python 3.10+。以下命令在仓库根目录执行：

```bash
git clone https://github.com/AdamsukS/scientific-figure-gallery.git
cd scientific-figure-gallery
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

python render.py --list
python render.py --figure all --format png svg
python render.py --figure 7 --format png svg pdf
```

Windows 可用 `py -m venv .venv`，PowerShell 激活命令为 `.venv\Scripts\Activate.ps1`。命令行 `cp` 示例在 Windows 中可用文件管理器复制目录代替。

输出默认写入 `output/`；该目录不进入版本控制。PNG 默认保持参考画布的宽高，`--scale 3` 导出三倍像素尺寸。SVG 保留可编辑文字，PDF 嵌入 TrueType 字体。优先使用已安装的 Arial，否则回退到 DejaVu Sans；跨平台字体与抗锯齿可能不同。

## 每张图都可以单独运行

```bash
python -m figures.figure07.plot --format png svg
python -m figures.figure12.plot --out my_output --format pdf
```

`figures/figure07/plot.py` 中是第 7 张图实际的 `draw(context, rows)` 绘图实现，不是调用一个包含所有图的中央大函数。共用的画布、CSV、箱线图、KDE 等小工具放在 `vizlib/common.py`；批量入口 `render.py` 自动发现图目录。

```text
figures/
  figure07/
    plot.py               # 这一张图的实际绘图代码
    style.json            # 尺寸、字体、颜色、标签、分类顺序
    data/
      figure07.csv        # 已注明来源的可替换示例数据
    provenance.json       # 数据类别、字段、单位、原始数据需求、文件校验值
    example_hashes.json   # 已发布示例的指纹，用于识别旧统计标注
    README.md             # 中文说明
    README.en.md          # English documentation
    preview.png           # 本图示例预览
vizlib/common.py          # 共用绘图小工具
render.py                 # 自动发现与批量导出
check_reuse.py            # 数据替换、导出、数据说明和扩展检查
scripts/new_figure.py     # 创建新图目录
scripts/build_gallery.py  # 更新中英文目录
```

## 替换成自己的数据

先阅读目标图的 README 中“需要哪些原始数据”和“从原始数据到绘图输入”。**科研原始数据与绘图 CSV 是不同层次**：例如，PCoA 图需要上游分析生成坐标；系统发育树需要真实树文件；气泡图需要从表达矩阵计算均值与阳性率。

```bash
cp -R figures/figure07/data my_data
# 修改 my_data/figure07.csv
python render.py --figure 7 --data-dir my_data --out my_output --format png svg pdf
```

`--data-dir` 可以是单张图的数据目录；批量替换时也可以是包含 `figure01/`、`figure02/` 等 CSV 子目录的父目录。组合图的辅助 CSV 必须一起更新，例如图 17 的密度、五数概括和 rug 数据必须来自同一批样本。

CSV 保持 UTF-8、列名及分类值一致。数字列不接受空值、NaN 或 Infinity。修改组名、基因名、单位、面板数或图例样本量时，需要同步修改样式。固定版式不会自动容纳任意数量的分类；复杂面板位置和点大小在该图的 `plot.py` 中调整。

```bash
cp figures/figure07/style.json my_style.json
python render.py --figure 7 --style my_style.json --data-dir my_data --out my_output
```

### 均值和误差

图 1、6、7、8 使用 `category,group,sample,value,mean,error` 长表。`value` 是样本值；`mean/error` 是重复填写的同组汇总。参考图中遮挡点无法完整恢复，所以估读的散点均值可能不同于估读的柱高。

| 模式 | 行为 |
|---|---|
| `--summary auto`（默认） | 未改动的示例用给定 `mean/error`；CSV 改动后从 `value` 计算均值和 SEM |
| `--summary samples` | 总是从样本值计算均值和 SEM，SEM = 样本标准差 / √n |
| `--summary provided` | 使用输入的 `mean/error`；需自行注明误差是 SD、SEM 还是 CI |

给定误差必须非负，同一组的重复汇总字段必须一致。一个样本的 SEM 按 0 展示，这不代表没有实验不确定性。图 4、9 接收预计算汇总值；图 18 接收五数概括，不自动从原始实验记录计算。

### 统计标注

代码**不会从截图或新数据自动推断显著性**。未改动的示例可以显示原图 P 值和星号作为外观参考，但这些不是重新计算的检验结果。

- `--annotations auto`（默认）：任一相关 CSV 改动后，停用原图统计标注。
- `--annotations none`：始终不显示参考统计标注。
- `--annotations reference`：强制显示参考标注，只适合外观比较，不适合报告新实验结果。

每张图的 `example_hashes.json` 位于数据目录外；替换数据目录中的同名文件不会被当作可信指纹。不要修改示例指纹来让真实数据显示旧结论。图 9 的三点为构造的参考外观符号，新数据默认隐藏。每次运行会写出 `render_log.json`，记录实际模式，日志不包含机器绝对路径。

### 山脊图的原始样本入口

图 14–16 接收两种形式：已经整理好的 `x,density` 曲线，或将这两列替换为 `value` 的样本长表。分组列保持不变，例如图 14：

```csv
panel,group,value
0,0,2.71
0,0,2.83
0,0,2.90
```

真实文件应包含样式要求的全部分组。程序按组计算高斯核密度估计，默认把峰归一化到 1.4 个行距；可增加 `height` 列控制展示高度。该高度不表示样本数量或组间可比较的绝对概率密度。流式样本需先完成补偿、门控和所需的 log/logicle/arcsinh 变换；本项目不执行这些上游处理。

## 图表索引

每个链接都包含：原始数据要求、预处理约定、当前数据来源、逐文件字段/单位、CSV 示例行、单图运行方法。

<!-- FIGURES:START -->

| ID | 图式 | 数据来源 |
|---|---|---|
| 01 | [空心柱状图与散点](figures/figure01/README.md) | `screenshot_estimate` |
| 02 | [PCoA 与边缘箱线图](figures/figure02/README.md) | `digitized` |
| 03 | [多队列 PCoA 组合图](figures/figure03/README.md) | `digitized` |
| 04 | [时间序列与 iAUC 插图](figures/figure04/README.md) | `mixed` |
| 05 | [半小提琴 雨云图](figures/figure05/README.md) | `synthetic_from_estimated_distribution` |
| 06 | [断轴分组柱状图](figures/figure06/README.md) | `screenshot_estimate` |
| 07 | [基因表达分组柱状图](figures/figure07/README.md) | `screenshot_estimate` |
| 08 | [PARP1 变体柱状图](figures/figure08/README.md) | `screenshot_estimate` |
| 09 | [双轴嵌套柱状图](figures/figure09/README.md) | `mixed` |
| 10 | [环形系统发育树与分类注释](figures/figure10/README.md) | `synthetic` |
| 11 | [环形系统发育树与热图](figures/figure11/README.md) | `synthetic` |
| 12 | [分组基因气泡矩阵](figures/figure12/README.md) | `digitized` |
| 13 | [双对数散点与边缘直方图](figures/figure13/README.md) | `synthetic` |
| 14 | [三组分子动力学山脊图](figures/figure14/README.md) | `synthetic_fitted_curve` |
| 15 | [流式细胞术山脊矩阵](figures/figure15/README.md) | `synthetic_fitted_curve` |
| 16 | [细胞群表达山脊矩阵](figures/figure16/README.md) | `synthetic_fitted_curve` |
| 17 | [区域年代分布 雨云图](figures/figure17/README.md) | `mixed` |
| 18 | [进化年龄分面箱线图](figures/figure18/README.md) | `screenshot_estimate` |
| 19 | [相关性 哑铃 气泡 与条形组合图](figures/figure19/README.md) | `screenshot_estimate_and_digitized` |

<!-- FIGURES:END -->

## 新增第 20 张图

```bash
python -m scripts.new_figure --id 20 --title "新的图表" --title-en "New chart"
python -m figures.figure20.plot --format png svg
```

创建器会生成一个可运行的两组模拟数据案例，且不会覆盖已有图。将它替换为需要的图式：编辑 `plot.py`、`style.json`、`data/`、`provenance.json` 和两份 README，然后更新预览与目录：

```bash
cp output/figure20.png figures/figure20/preview.png
python -m scripts.build_gallery
python check_reuse.py
```

`render.py --figure all` 自动包含新图，不需要中央注册项。如何记录真实来源、导入树和更新指纹见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 验证与范围

```bash
python check_reuse.py
```

检查会逐图渲染原始示例及修改后的 CSV，验证输出尺寸、SVG 未嵌入位图、数据变化确实改变图像、旧统计标注停用，以及文档、字段、指纹匹配。还会在临时项目中新建并运行一张图，验证新增流程。GitHub Actions 在推送和 PR 时执行相同检查。

19 个初始模块拆分后，在相同本机字体/依赖环境下，输出与拆分前预览逐像素一致。**这是对重构的回归检查，不表示与文档原图逐像素一致。** 科学计算方法、数据来源真实性和最终科研结论仍需由实际数据与原分析流程确认。

原始 Word、参考截图、本地对照网页、虚拟环境和临时文件不在公开仓库中。预览是代码重绘结果。已公布的模拟/估读 CSV 足以运行全部模板，不依赖参考图片。原始论文/DOI 尚未核实，`source_publication` 明确为 null。

## 许可证

[MIT](LICENSE) 适用于本项目代码和项目撰写的说明。模拟/估读数据的性质逐文件记载；本仓库不声称拥有或授予参考论文、原始研究数据或第三方图片的权利。
