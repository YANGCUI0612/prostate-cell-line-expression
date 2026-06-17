#!/usr/bin/env python3
"""Build compact data.js for the prostate cell-line expression explorer (V6).

Reads the DepMap Public 26Q1 prostate log1p(TPM) subset and emits a single
classic-script `data.js` that assigns window.EXPR_DATA. No server required:
open index.html directly from the filesystem.
"""
import csv, json, os, sys

SRC = os.path.join(
    os.path.dirname(__file__), "..",
    "prostate_cell_line_rnaseq_catalog", "raw",
    "depmap_public_26q1_prostate_expression_tpm_logp1_subset.csv",
)
OUT = os.path.join(os.path.dirname(__file__), "data.js")

# raw depmap display id -> (pretty name, lineage)
META = {
    "LNCAPCLONEFGC": ("LNCaP",       "AR/luminal-enriched"),
    "MDAPCA2B":      ("MDA PCa 2b",  "AR/luminal-enriched"),
    "22RV1":         ("22Rv1",       "AR/luminal-enriched"),
    "VCAP":          ("VCaP",        "AR/luminal-enriched"),
    "PC3":           ("PC-3",        "AR-low / mesenchymal-like"),
    "DU145":         ("DU 145",      "AR-low / mesenchymal-like"),
    "NCIH660":       ("NCI-H660",    "NE / small-cell"),
    "P4E6":          ("P4E6",        "Benign / control"),
    "PRECLH":        ("PrEC LH",     "Benign / control"),
    "SHMAC4":        ("Shmac 4",     "Benign / control"),
    "SHMAC5":        ("Shmac 5",     "Benign / control"),
    "BPH1":          ("BPH-1",       "Benign / control"),
    "WPE1NA22":      ("WPE1-NA22",   "Benign / control"),
}

N_META_COLS = 7  # depmap_id, cell_line_display_name, lineage_1, lineage_2, lineage_3, lineage_6, lineage_4

def main():
    with open(SRC, newline="") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        genes = header[N_META_COLS:]
        cell_lines, matrix = [], []
        for row in reader:
            raw_id = row[1]
            pretty, lineage = META.get(raw_id, (raw_id, "Unassigned"))
            cell_lines.append({
                "id": row[0],
                "raw": raw_id,
                "name": pretty,
                "lineage": lineage,
            })
            # round to 2 decimals (0.01 resolution in log space is plenty)
            vals = [round(float(v), 2) if v not in ("", "NA") else 0.0
                    for v in row[N_META_COLS:]]
            matrix.append(vals)

    print(f"genes={len(genes)} cell_lines={len(cell_lines)}", file=sys.stderr)

    data = {
        "source": "DepMap Public 26Q1 — OmicsExpressionTPMLogp1HumanProteinCodingGenes (prostate subset)",
        "unit": "log1p(TPM)",
        "note": "Not batch-corrected by us; DepMap-harmonized expression only.",
        "genes": genes,
        "cellLines": cell_lines,
        "matrix": matrix,  # [cellLineIndex][geneIndex]
    }
    payload = json.dumps(data, separators=(",", ":"))
    with open(OUT, "w") as fh:
        fh.write("window.EXPR_DATA=")
        fh.write(payload)
        fh.write(";\n")
    print(f"wrote {OUT} ({os.path.getsize(OUT)/1e6:.2f} MB)", file=sys.stderr)

if __name__ == "__main__":
    main()
