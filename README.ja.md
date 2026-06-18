<div align="center">

# 前立腺がん細胞株 発現エクスプローラー

**前立腺がん細胞株間の遺伝子発現を比較するインタラクティブツール**

[![Live demo](https://img.shields.io/badge/live_demo-online-24292f?style=flat&labelColor=505965&logo=githubpages&logoColor=white)](https://yangcui0612.github.io/prostate-cell-line-expression/)
[![License](https://img.shields.io/badge/license-MIT-24292f?style=flat&labelColor=505965&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Data](https://img.shields.io/badge/data-DepMap_Public_26Q1-24292f?style=flat&labelColor=505965)](https://depmap.org/portal/)

[English](README.md)&nbsp;&nbsp;·&nbsp;&nbsp;[简体中文](README.zh-CN.md)&nbsp;&nbsp;·&nbsp;&nbsp;**日本語**

<br/>

<a href="https://yangcui0612.github.io/prostate-cell-line-expression/">
<img src="assets/preview.png" alt="アプリ概要:系統セレクター、ボルケーノ図、発現変動遺伝子表、遺伝子別バーチャート" width="880">
</a>

</div>

<br/>

## 概要

前立腺がん研究は、異なる分子系統にまたがる少数の代表的な細胞株に依拠しています——アンドロゲン受容体(AR)駆動のルミナル型、AR 低発現/間葉系様、神経内分泌小細胞型、そして良性対照です。本ブラウザツールは、これらのモデル間の発現差を直接可視化します。任意の細胞株を 2 群に割り当て、発現変動のボルケーノ図を計算し、ある遺伝子のプロファイルを全 13 株にわたって読み取れます。すべてクライアントサイドで動作し、依存関係もビルド工程もありません。

## 特長

- **系統別に整理されたパネル** —— 13 株を分子系統ごとにグループ化し、モデルの位置づけと解釈を一目で把握。
- **2 群(A vs B)比較** —— 任意の株を 2 群に割り当て、即座に再計算。
- **インタラクティブなボルケーノ図** —— 横軸 log₂ フォールドチェンジ、縦軸 −log₁₀ *p*。ホバーで遺伝子別の統計量、クリックで固定し、上位 10 遺伝子を自動ラベル、しきい値は調整可能。
- **並べ替え可能な発現変動遺伝子表** —— 全列を昇順/降順で並べ替え、遺伝子名で検索。
- **遺伝子別の発現プロファイル** —— 遺伝子を選択すると、全 13 株での発現を系統別の色で表示。

## データと方法

**データソース。** *DepMap Public 26Q1* の前立腺サブセット(`OmicsExpressionTPMLogp1HumanProteinCodingGenes`):13 株・19,215 のタンパク質コード遺伝子の **log1p(TPM)**。値は DepMap により統一処理され、ここで追加のバッチ補正は**行っていません**。

**フォールドチェンジ。** 発現を線形 TPM に戻し、群平均の対数比として要約します:

$$\log_2\mathrm{FC} = \log_2\!\frac{\overline{\mathrm{TPM}}_A + 1}{\overline{\mathrm{TPM}}_B + 1}$$

**有意性。** log1p(TPM) 値に対する両側 **Welch の *t* 検定**(細胞株をレプリケートとみなす)、自由度は Welch–Satterthwaite 近似:

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{s_A^2/n_A + s_B^2/n_B}}$$

本検定には**各群 ≥ 2 株**が必要です。片群が 1 株のみの場合は *p* 値が定義できず、その旨を表示し、縦軸は平均発現量に切り替わります。既定のしきい値は |log₂FC| ≥ 1 かつ *p* ≤ 0.05(いずれも調整可能)。

## 使い方

```bash
git clone https://github.com/YANGCUI0612/prostate-cell-line-expression.git
cd prostate-cell-line-expression
open index.html            # そのまま開く(サーバー不要)
```

ソースの DepMap 行列から `data.js` を再生成:`python3 build_data.py`。

## 細胞株パネル

| 細胞株 | 分子系統 | 区分 |
|---|---|---|
| LNCaP, MDA PCa 2b, 22Rv1, VCaP | AR / ルミナル型 | がん |
| PC-3, DU 145 | AR 低発現 / 間葉系様 | がん |
| NCI-H660 | 神経内分泌 / 小細胞 | がん |
| P4E6, PrEC LH, Shmac 4, Shmac 5, BPH-1, WPE1-NA22 | 良性 / 対照 | 良性 / 対照 |

## ライセンス

コード:[MIT](LICENSE) © 2026 YANGCUI0612。発現データ:[DepMap Public 26Q1](https://depmap.org/portal/)(Broad Institute)、DepMap 利用規約に従います。
