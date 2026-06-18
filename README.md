<div align="center">

# Prostate Cell-Line Expression Explorer

**Interactive comparison of gene expression across prostate-cancer cell lines**

[![Live demo](https://img.shields.io/badge/live_demo-online-24292f?style=flat&labelColor=505965&logo=githubpages&logoColor=white)](https://yangcui0612.github.io/prostate-cell-line-expression/)
[![License](https://img.shields.io/badge/license-MIT-24292f?style=flat&labelColor=505965&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Data](https://img.shields.io/badge/data-DepMap_Public_26Q1-24292f?style=flat&labelColor=505965)](https://depmap.org/portal/)

**English**&nbsp;&nbsp;·&nbsp;&nbsp;[简体中文](README.zh-CN.md)&nbsp;&nbsp;·&nbsp;&nbsp;[日本語](README.ja.md)

<br/>

<a href="https://yangcui0612.github.io/prostate-cell-line-expression/">
<img src="assets/preview.png" alt="Application overview: lineage selector, volcano plot, differential-gene table, and per-gene bar chart" width="880">
</a>

</div>

<br/>

## Overview

Prostate-cancer research relies on a small set of canonical cell lines spanning distinct molecular lineages — androgen-receptor (AR)–driven luminal models, AR-low/mesenchymal models, neuroendocrine small-cell models, and benign controls. This browser-based tool makes the differences between them directly legible: assign any lines to two groups, compute a differential-expression volcano, and read a single gene's profile across all 13 lines — entirely client-side, with no dependencies and no build step.

## Features

- **Lineage-organized panel** — the 13 lines are grouped by molecular lineage, so a model can be located and interpreted at a glance.
- **Two-group (A vs B) comparison** — assign arbitrary lines to two groups and recompute instantly.
- **Interactive volcano plot** — log₂ fold-change against −log₁₀ *p*; hover for per-gene statistics, click to pin a gene, with the ten strongest hits labelled and adjustable thresholds.
- **Sortable differential-expression table** — every column sorts ascending or descending, with gene-symbol search.
- **Per-gene expression profile** — selecting a gene renders its expression across all 13 lines, coloured by lineage.

## Data and methods

**Source.** The prostate subset of *DepMap Public 26Q1* (`OmicsExpressionTPMLogp1HumanProteinCodingGenes`): **log1p(TPM)** for 19,215 protein-coding genes across 13 cell lines. Values are DepMap-harmonized; they are **not** additionally batch-corrected here.

**Fold change.** Expression is returned to linear TPM and summarized as a log-ratio of group means:

$$\log_2\mathrm{FC} = \log_2\!\frac{\overline{\mathrm{TPM}}_A + 1}{\overline{\mathrm{TPM}}_B + 1}$$

**Significance.** A two-sided **Welch's *t*-test** on the log1p(TPM) values, treating cell lines as replicates, with Welch–Satterthwaite degrees of freedom:

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{s_A^2/n_A + s_B^2/n_B}}$$

This requires **≥ 2 lines per group**; with a single line the *p*-value is undefined, the interface states so, and the ordinate falls back to mean expression. Default thresholds are |log₂FC| ≥ 1 and *p* ≤ 0.05, both adjustable.

## Usage

```bash
git clone https://github.com/YANGCUI0612/prostate-cell-line-expression.git
cd prostate-cell-line-expression
open index.html            # open directly — no server required
```

To regenerate `data.js` from the source DepMap matrix: `python3 build_data.py`.

## Cell-line panel

| Cell lines | Molecular lineage | Role |
|---|---|---|
| LNCaP, MDA PCa 2b, 22Rv1, VCaP | AR / luminal-enriched | cancer |
| PC-3, DU 145 | AR-low / mesenchymal-like | cancer |
| NCI-H660 | Neuroendocrine / small-cell | cancer |
| P4E6, PrEC LH, Shmac 4, Shmac 5, BPH-1, WPE1-NA22 | Benign / control | benign / control |

## License

Code: [MIT](LICENSE) © 2026 YANGCUI0612. Expression data: [DepMap Public 26Q1](https://depmap.org/portal/) (Broad Institute), subject to the DepMap terms of use.
