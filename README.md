<div align="center">

# Prostate Cell-Line Expression Explorer

**Interactive comparison of gene expression across prostate-cancer cell lines**

[![Live demo](https://img.shields.io/badge/demo-online-2ea44f?style=flat-square)](https://yangcui0612.github.io/prostate-cell-line-expression/)
[![License](https://img.shields.io/badge/license-MIT-1f6feb?style=flat-square)](LICENSE)
[![Data](https://img.shields.io/badge/data-DepMap%20Public%2026Q1-6e7781?style=flat-square)](https://depmap.org/portal/)

**English**&nbsp;&nbsp;·&nbsp;&nbsp;[简体中文](README.zh-CN.md)&nbsp;&nbsp;·&nbsp;&nbsp;[日本語](README.ja.md)

<br/>

<a href="https://yangcui0612.github.io/prostate-cell-line-expression/">
<img src="assets/preview.png" alt="Application overview: lineage selector, volcano plot, differential-gene table, and per-gene bar chart" width="880">
</a>

</div>

<br/>

> A browser-based tool for exploring and contrasting transcriptional programs across 13 expression-profiled prostate cell lines. Assign cell lines to two groups, compute a differential-expression volcano, and inspect any gene's profile across the full panel — entirely client-side, with no dependencies and no build step.

**Live application:** <https://yangcui0612.github.io/prostate-cell-line-expression/>

## Overview

Prostate-cancer research relies on a small set of canonical cell lines spanning distinct molecular lineages — androgen-receptor (AR)–driven luminal models, AR-low/mesenchymal models, neuroendocrine small-cell models, and benign controls. This application makes the expression differences between those models directly legible: a researcher can select any two sets of lines, see which genes separate them, and read a single gene's behaviour across the entire panel in one view.

## Features

- **Lineage-organized panel.** The 13 lines are grouped by molecular lineage so a model can be located and interpreted at a glance.
- **Two-group (A vs B) comparison.** Assign arbitrary lines to two groups and recompute instantly.
- **Interactive volcano plot.** Log2 fold-change against −log₁₀ *p*; hover for per-gene statistics, click to pin a gene, with the ten strongest hits labelled and adjustable fold-change / significance thresholds.
- **Sortable differential-expression table.** Every column sorts ascending or descending, with gene-symbol search.
- **Per-gene expression profile.** Selecting a gene renders its expression across all 13 lines, coloured by lineage.

## Data and methods

**Source.** Expression values are the prostate subset of *DepMap Public 26Q1* (`OmicsExpressionTPMLogp1HumanProteinCodingGenes`): **log1p(TPM)** for 19,215 protein-coding genes across 13 cell lines. Values are DepMap-harmonized; they are **not** additionally batch-corrected here, and this is not a multi-dataset integrated atlas.

**Fold change.** For groups *A* and *B*, expression is returned to linear TPM and summarized as a log-ratio of group means:

$$\log_2\mathrm{FC} = \log_2\!\frac{\overline{\mathrm{TPM}}_A + 1}{\overline{\mathrm{TPM}}_B + 1}$$

**Significance.** A two-sided **Welch's *t*-test** is computed on the log1p(TPM) values, treating cell lines as replicates:

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{s_A^2/n_A + s_B^2/n_B}}$$

with degrees of freedom from the Welch–Satterthwaite approximation. This requires **≥ 2 lines per group**; when a group contains a single line, no replicate-based *p*-value is defined, the interface states so, and the ordinate falls back to mean expression.

**Default thresholds.** |log₂FC| ≥ 1 and *p* ≤ 0.05, both adjustable in the interface.

## Usage

```bash
git clone https://github.com/YANGCUI0612/prostate-cell-line-expression.git
cd prostate-cell-line-expression

# Open directly — no server required:
open index.html            # macOS
# …or serve locally:
python3 -m http.server 8000   # then visit http://localhost:8000
```

To regenerate `data.js` from the source DepMap matrix:

```bash
python3 build_data.py
```

## Repository structure

```
index.html      Single-file application (interface and logic)
data.js         Embedded expression matrix (13 × 19,215, log1p TPM)
build_data.py   Regenerates data.js from the DepMap subset
assets/         Figures
LICENSE         MIT
```

## Cell-line panel

| Cell lines | Molecular lineage | Role |
|---|---|---|
| LNCaP, MDA PCa 2b, 22Rv1, VCaP | AR / luminal-enriched | cancer |
| PC-3, DU 145 | AR-low / mesenchymal-like | cancer |
| NCI-H660 | Neuroendocrine / small-cell | cancer |
| P4E6, PrEC LH, Shmac 4, Shmac 5, BPH-1, WPE1-NA22 | Benign / control | benign / control |

## Data attribution and license

The application code is released under the [MIT License](LICENSE) © 2026 YANGCUI0612.
Expression data are derived from [DepMap Public 26Q1](https://depmap.org/portal/) (Broad Institute) and remain subject to the DepMap terms of use.
