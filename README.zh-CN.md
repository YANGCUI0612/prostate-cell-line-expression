<div align="center">

# 前列腺癌细胞系表达浏览器

**跨前列腺癌细胞系的基因表达交互式比较工具**

[![Live demo](https://img.shields.io/badge/live_demo-online-24292f?style=flat&labelColor=505965&logo=githubpages&logoColor=white)](https://yangcui0612.github.io/prostate-cell-line-expression/)
[![License](https://img.shields.io/badge/license-MIT-24292f?style=flat&labelColor=505965&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Data](https://img.shields.io/badge/data-DepMap_Public_26Q1-24292f?style=flat&labelColor=505965)](https://depmap.org/portal/)

[English](README.md)&nbsp;&nbsp;·&nbsp;&nbsp;**简体中文**&nbsp;&nbsp;·&nbsp;&nbsp;[日本語](README.ja.md)

<br/>

<a href="https://yangcui0612.github.io/prostate-cell-line-expression/">
<img src="assets/preview.png" alt="应用总览:谱系选择器、火山图、差异基因表、单基因柱状图" width="880">
</a>

</div>

<br/>

## 概述

前列腺癌研究依赖一小批经典细胞系,它们覆盖不同的分子谱系——雄激素受体(AR)驱动的管腔型、AR 低表达/间充质样、神经内分泌小细胞型,以及良性对照。本浏览器工具让这些模型之间的表达差异一目了然:任选细胞系分入两组、计算差异表达火山图、并在全部 13 个细胞系中读出某个基因的表达谱——完全在客户端运行,零依赖、无需构建。

## 功能

- **按谱系组织的面板** —— 13 个细胞系按分子谱系分组,便于快速定位与解读。
- **双组(A vs B)比较** —— 任意把细胞系分到两组,实时重新计算。
- **交互式火山图** —— 横轴 log₂ 倍数变化,纵轴 −log₁₀ *p*;悬浮显示单基因统计量,点击锁定基因,自动标注前十个最显著基因,阈值可调。
- **可排序的差异表达表** —— 每一列均可升序/降序排序,支持按基因名搜索。
- **单基因表达谱** —— 选择某个基因后,展示其在全部 13 个细胞系中的表达,并按谱系着色。

## 数据与方法

**数据来源。** *DepMap Public 26Q1* 的前列腺子集(`OmicsExpressionTPMLogp1HumanProteinCodingGenes`):13 个细胞系、19,215 个蛋白编码基因的 **log1p(TPM)**。数据为 DepMap 统一处理,**未**在此额外做批次校正。

**倍数变化。** 将表达还原为线性 TPM,以组均值的对数比表示:

$$\log_2\mathrm{FC} = \log_2\!\frac{\overline{\mathrm{TPM}}_A + 1}{\overline{\mathrm{TPM}}_B + 1}$$

**显著性。** 在 log1p(TPM) 值上计算双侧 **Welch t 检验**,将细胞系视为重复样本,自由度采用 Welch–Satterthwaite 近似:

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{s_A^2/n_A + s_B^2/n_B}}$$

该检验需要**每组 ≥ 2 个细胞系**;某组只有单个细胞系时 *p* 值无法定义,界面会明确提示,此时纵轴退化为平均表达量。默认阈值为 |log₂FC| ≥ 1 且 *p* ≤ 0.05,均可调整。

## 使用方法

```bash
git clone https://github.com/YANGCUI0612/prostate-cell-line-expression.git
cd prostate-cell-line-expression
open index.html            # 直接打开,无需服务器
```

从源 DepMap 矩阵重新生成 `data.js`:`python3 build_data.py`。

## 细胞系面板

| 细胞系 | 分子谱系 | 类型 |
|---|---|---|
| LNCaP、MDA PCa 2b、22Rv1、VCaP | AR / 管腔型 | 癌 |
| PC-3、DU 145 | AR 低表达 / 间充质样 | 癌 |
| NCI-H660 | 神经内分泌 / 小细胞 | 癌 |
| P4E6、PrEC LH、Shmac 4、Shmac 5、BPH-1、WPE1-NA22 | 良性 / 对照 | 良性 / 对照 |

## 许可

代码:[MIT](LICENSE) © 2026 YANGCUI0612。表达数据:[DepMap Public 26Q1](https://depmap.org/portal/)(Broad Institute),须遵守 DepMap 使用条款。
