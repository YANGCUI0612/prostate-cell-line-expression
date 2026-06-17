<div align="center">

# 前列腺癌细胞系表达浏览器

**跨前列腺癌细胞系的基因表达交互式比较工具**

[![Live demo](https://img.shields.io/badge/demo-online-2ea44f?style=flat-square)](https://yangcui0612.github.io/prostate-cell-line-expression/)
[![License](https://img.shields.io/badge/license-MIT-1f6feb?style=flat-square)](LICENSE)
[![Data](https://img.shields.io/badge/data-DepMap%20Public%2026Q1-6e7781?style=flat-square)](https://depmap.org/portal/)

[English](README.md)&nbsp;&nbsp;·&nbsp;&nbsp;**简体中文**&nbsp;&nbsp;·&nbsp;&nbsp;[日本語](README.ja.md)

<br/>

<a href="https://yangcui0612.github.io/prostate-cell-line-expression/">
<img src="assets/preview.png" alt="应用总览:谱系选择器、火山图、差异基因表、单基因柱状图" width="880">
</a>

</div>

<br/>

> 一个基于浏览器的工具,用于浏览并对比 13 个已做表达谱分析的前列腺细胞系的转录程序。将细胞系分入两组、计算差异表达火山图、并在整组细胞系中查看任意基因的表达——完全在客户端运行,零依赖、无需构建。

**在线应用:** <https://yangcui0612.github.io/prostate-cell-line-expression/>

## 概述

前列腺癌研究依赖一小批经典细胞系,它们覆盖了不同的分子谱系——雄激素受体(AR)驱动的管腔型、AR 低表达/间充质样、神经内分泌小细胞型,以及良性对照。本应用让这些模型之间的表达差异一目了然:研究者可任选两组细胞系,查看哪些基因将它们区分开,并在单一视图中读出某个基因在整组细胞系中的行为。

## 功能

- **按谱系组织的面板。** 13 个细胞系按分子谱系分组,便于快速定位与解读。
- **双组(A vs B)比较。** 任意把细胞系分到两组,实时重新计算。
- **交互式火山图。** 横轴 log2 倍数变化,纵轴 −log₁₀ *p*;悬浮显示单基因统计量,点击锁定基因,自动标注前十个最显著基因,倍数与显著性阈值可调。
- **可排序的差异表达表。** 每一列均可升序/降序排序,支持按基因名搜索。
- **单基因表达谱。** 选择某个基因后,展示其在全部 13 个细胞系中的表达,并按谱系着色。

## 数据与方法

**数据来源。** 表达值取自 *DepMap Public 26Q1* 的前列腺子集(`OmicsExpressionTPMLogp1HumanProteinCodingGenes`):13 个细胞系、19,215 个蛋白编码基因的 **log1p(TPM)**。数据为 DepMap 统一处理,**未**在此额外做批次校正,也并非多数据集整合图谱。

**倍数变化。** 对于 A、B 两组,先将表达还原为线性 TPM,再以组均值的对数比表示:

$$\log_2\mathrm{FC} = \log_2\!\frac{\overline{\mathrm{TPM}}_A + 1}{\overline{\mathrm{TPM}}_B + 1}$$

**显著性。** 在 log1p(TPM) 值上计算双侧 **Welch t 检验**,将细胞系视为重复样本:

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{s_A^2/n_A + s_B^2/n_B}}$$

自由度采用 Welch–Satterthwaite 近似。该检验需要**每组 ≥ 2 个细胞系**;当某组只有单个细胞系时,无法定义基于重复的 *p* 值,界面会明确提示,此时纵轴退化为平均表达量。

**默认阈值。** |log₂FC| ≥ 1 且 *p* ≤ 0.05,均可在界面中调整。

## 使用方法

```bash
git clone https://github.com/YANGCUI0612/prostate-cell-line-expression.git
cd prostate-cell-line-expression

# 直接打开,无需服务器:
open index.html            # macOS
# …或本地启动服务:
python3 -m http.server 8000   # 然后访问 http://localhost:8000
```

从源 DepMap 矩阵重新生成 `data.js`:

```bash
python3 build_data.py
```

## 仓库结构

```
index.html      单文件应用(界面与逻辑)
data.js         内嵌表达矩阵(13 × 19,215,log1p TPM)
build_data.py   从 DepMap 子集重新生成 data.js
assets/         图片
LICENSE         MIT
```

## 细胞系面板

| 细胞系 | 分子谱系 | 类型 |
|---|---|---|
| LNCaP、MDA PCa 2b、22Rv1、VCaP | AR / 管腔型 | 癌 |
| PC-3、DU 145 | AR 低表达 / 间充质样 | 癌 |
| NCI-H660 | 神经内分泌 / 小细胞 | 癌 |
| P4E6、PrEC LH、Shmac 4、Shmac 5、BPH-1、WPE1-NA22 | 良性 / 对照 | 良性 / 对照 |

## 数据出处与许可

应用代码以 [MIT 许可证](LICENSE) 发布 © 2026 YANGCUI0612。
表达数据来自 [DepMap Public 26Q1](https://depmap.org/portal/)(Broad Institute),其使用须遵守 DepMap 使用条款。
