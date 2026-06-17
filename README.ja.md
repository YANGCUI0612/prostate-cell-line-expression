<div align="center">

# 前立腺がん細胞株 発現エクスプローラー

**前立腺がん細胞株間の遺伝子発現を比較するインタラクティブツール**

[![Live demo](https://img.shields.io/badge/demo-online-2ea44f?style=flat-square)](https://yangcui0612.github.io/prostate-cell-line-expression/)
[![License](https://img.shields.io/badge/license-MIT-1f6feb?style=flat-square)](LICENSE)
[![Data](https://img.shields.io/badge/data-DepMap%20Public%2026Q1-6e7781?style=flat-square)](https://depmap.org/portal/)

[English](README.md)&nbsp;&nbsp;·&nbsp;&nbsp;[简体中文](README.zh-CN.md)&nbsp;&nbsp;·&nbsp;&nbsp;**日本語**

<br/>

<a href="https://yangcui0612.github.io/prostate-cell-line-expression/">
<img src="assets/preview.png" alt="アプリ概要:系統セレクター、ボルケーノ図、発現変動遺伝子表、遺伝子別バーチャート" width="880">
</a>

</div>

<br/>

> 発現プロファイルが得られている 13 種の前立腺細胞株について、転写プログラムを閲覧・比較するためのブラウザベースのツールです。細胞株を 2 群に割り当て、発現変動のボルケーノ図を計算し、任意の遺伝子のプロファイルを全パネルにわたって確認できます。すべてクライアントサイドで動作し、依存関係もビルド工程もありません。

**オンラインアプリ:** <https://yangcui0612.github.io/prostate-cell-line-expression/>

## 概要

前立腺がん研究は、異なる分子系統にまたがる少数の代表的な細胞株に依拠しています——アンドロゲン受容体(AR)駆動のルミナル型、AR 低発現/間葉系様、神経内分泌小細胞型、そして良性対照です。本アプリはこれらのモデル間の発現差を直接可視化します。研究者は任意の 2 群を選び、両者を分ける遺伝子を確認し、ある遺伝子の挙動をパネル全体にわたって一画面で読み取れます。

## 特長

- **系統別に整理されたパネル。** 13 株を分子系統ごとにグループ化し、モデルの位置づけと解釈を一目で把握。
- **2 群(A vs B)比較。** 任意の株を 2 群に割り当て、即座に再計算。
- **インタラクティブなボルケーノ図。** 横軸 log2 フォールドチェンジ、縦軸 −log₁₀ *p*。ホバーで遺伝子別の統計量を表示、クリックで固定し、上位 10 遺伝子を自動ラベル。フォールドチェンジ・有意性のしきい値は調整可能。
- **並べ替え可能な発現変動遺伝子表。** 全列を昇順/降順で並べ替え、遺伝子名で検索。
- **遺伝子別の発現プロファイル。** 遺伝子を選択すると、全 13 株での発現を系統別の色で表示。

## データと方法

**データソース。** 発現値は *DepMap Public 26Q1* の前立腺サブセット(`OmicsExpressionTPMLogp1HumanProteinCodingGenes`):13 株・19,215 のタンパク質コード遺伝子の **log1p(TPM)**。値は DepMap により統一処理されており、ここで追加のバッチ補正は**行っていません**。また複数データセットの統合アトラスではありません。

**フォールドチェンジ。** A・B 両群について、発現を線形 TPM に戻し、群平均の対数比として要約します:

$$\log_2\mathrm{FC} = \log_2\!\frac{\overline{\mathrm{TPM}}_A + 1}{\overline{\mathrm{TPM}}_B + 1}$$

**有意性。** log1p(TPM) 値に対して両側 **Welch の *t* 検定**を、細胞株をレプリケートとみなして計算します:

$$t = \frac{\bar{x}_A - \bar{x}_B}{\sqrt{s_A^2/n_A + s_B^2/n_B}}$$

自由度は Welch–Satterthwaite 近似によります。本検定には**各群 ≥ 2 株**が必要です。片群が 1 株のみの場合はレプリケートに基づく *p* 値が定義できないため、その旨を表示し、縦軸は平均発現量に切り替わります。

**既定のしきい値。** |log₂FC| ≥ 1 かつ *p* ≤ 0.05(いずれも UI で調整可能)。

## 使い方

```bash
git clone https://github.com/YANGCUI0612/prostate-cell-line-expression.git
cd prostate-cell-line-expression

# そのまま開く(サーバー不要):
open index.html            # macOS
# …またはローカルで配信:
python3 -m http.server 8000   # http://localhost:8000 へアクセス
```

ソースの DepMap 行列から `data.js` を再生成:

```bash
python3 build_data.py
```

## リポジトリ構成

```
index.html      単一ファイルのアプリ(UI とロジック)
data.js         埋め込み発現行列(13 × 19,215、log1p TPM)
build_data.py   DepMap サブセットから data.js を再生成
assets/         図版
LICENSE         MIT
```

## 細胞株パネル

| 細胞株 | 分子系統 | 区分 |
|---|---|---|
| LNCaP, MDA PCa 2b, 22Rv1, VCaP | AR / ルミナル型 | がん |
| PC-3, DU 145 | AR 低発現 / 間葉系様 | がん |
| NCI-H660 | 神経内分泌 / 小細胞 | がん |
| P4E6, PrEC LH, Shmac 4, Shmac 5, BPH-1, WPE1-NA22 | 良性 / 対照 | 良性 / 対照 |

## データ出典とライセンス

アプリケーションのコードは [MIT ライセンス](LICENSE) で公開しています © 2026 YANGCUI0612。
発現データは [DepMap Public 26Q1](https://depmap.org/portal/)(Broad Institute)に由来し、DepMap の利用規約に従います。
