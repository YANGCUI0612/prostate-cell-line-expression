# Prostate Cell-Line Expression Explorer (V6)

A single, self-contained page for browsing DepMap prostate cell-line expression.
**Open `index.html` directly** (double-click) — no server needed. `data.js` must sit next to it.

## What it does
1. **Cell lines by lineage** (left) — 13 expression-ready lines grouped into
   AR/luminal-enriched · AR-low/mesenchymal-like · NE/small-cell · Benign/control.
   Click `A` / `B` to put a line into either comparison group.
2. **Volcano** (center) — log2 fold change (A vs B) vs −log10 p (Welch t-test across
   the cell lines in each group). Hover any point for the gene + stats; click to select it.
   Adjust the |log2FC| and p thresholds with the sliders.
3. **Differential genes** (right) — every column sortable ascending/descending; search by symbol.
4. **Gene across all 13 cell lines** (center-bottom) — click any gene (in the volcano or the
   table) to see its log1p(TPM) in every line, colored by lineage; A/B members are tagged.

## Honest stats notes
- Values are **DepMap Public 26Q1 log1p(TPM)**, protein-coding genes. **Not** batch-corrected by us.
- log2FC is computed from linear TPM means: `log2((meanTPM_A+1)/(meanTPM_B+1))`.
- p-values are a **Welch t-test treating cell lines as replicates** — they need **≥2 lines in each
  group**. With a single line in a group there are no replicates: the page says so and the y-axis
  falls back to mean expression (it becomes a fold-change vs abundance plot, not a statistical volcano).

## Rebuild the data
```
python3 build_data.py   # reads ../prostate_cell_line_rnaseq_catalog/raw/depmap_..._subset.csv -> data.js
```
