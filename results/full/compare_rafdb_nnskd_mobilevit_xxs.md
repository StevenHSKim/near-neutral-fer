# rafdb: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.97 | 0.0007 | 0.0060 | 0.0625 | 4.16 |
| microexpnet | 5 | +15.55 | 0.0000 | 0.0000 | 0.0625 | 19.22 |
| mobilevit_xxs | 5 | +0.85 | 0.0381 | 0.1663 | 0.0625 | 1.36 |
| nnskd_mobilevit_xxs_aux | 5 | +0.23 | 0.4747 | 1.0000 | 1.0000 | 0.35 |
| nnskd_mobilevit_xxs_kd | 5 | +0.20 | 0.5276 | 1.0000 | 0.8125 | 0.31 |
| nnskd_mobilevit_xxs_nm | 5 | +1.15 | 0.0167 | 0.1004 | 0.0625 | 1.77 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.04 | 0.5583 | 1.0000 | 0.7150 | 0.29 |
| pattlite | 5 | +0.88 | 0.0032 | 0.0223 | 0.0625 | 2.83 |
| resnet18 | 5 | +0.76 | 0.0333 | 0.1663 | 0.0625 | 1.43 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +5.70 | 0.0002 | 0.0012 | 0.0625 | 6.25 |
| microexpnet | 5 | +28.58 | 0.0000 | 0.0003 | 0.0625 | 8.89 |
| mobilevit_xxs | 5 | +1.78 | 0.0322 | 0.1929 | 0.1250 | 1.44 |
| nnskd_mobilevit_xxs_aux | 5 | +0.69 | 0.3529 | 1.0000 | 0.4375 | 0.47 |
| nnskd_mobilevit_xxs_kd | 5 | +0.22 | 0.7946 | 1.0000 | 0.8125 | 0.12 |
| nnskd_mobilevit_xxs_nm | 5 | +1.99 | 0.0403 | 0.2014 | 0.0625 | 1.34 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.08 | 0.5967 | 1.0000 | 0.8125 | 0.26 |
| pattlite | 5 | +1.87 | 0.0443 | 0.2014 | 0.1250 | 1.29 |
| resnet18 | 5 | +1.64 | 0.0176 | 0.1232 | 0.0625 | 1.74 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +7.46 | 0.0001 | 0.0006 | 0.0625 | 7.77 |
| microexpnet | 5 | +40.37 | 0.0001 | 0.0006 | 0.0625 | 7.37 |
| mobilevit_xxs | 5 | +2.57 | 0.0512 | 0.2814 | 0.1250 | 1.23 |
| nnskd_mobilevit_xxs_aux | 5 | +1.41 | 0.1992 | 0.5975 | 0.1250 | 0.69 |
| nnskd_mobilevit_xxs_kd | 5 | +0.28 | 0.8308 | 0.8308 | 0.8125 | 0.10 |
| nnskd_mobilevit_xxs_nm | 5 | +2.82 | 0.0513 | 0.2814 | 0.0625 | 1.23 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.26 | 0.2609 | 0.5975 | 0.3125 | 0.59 |
| pattlite | 5 | +2.92 | 0.0469 | 0.2814 | 0.1250 | 1.27 |
| resnet18 | 5 | +2.50 | 0.0181 | 0.1264 | 0.0625 | 1.73 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.02 | 0.0329 | 0.2634 | 0.1250 | 1.43 |
| microexpnet | 5 | +9.38 | 0.0004 | 0.0032 | 0.0625 | 5.03 |
| mobilevit_xxs | 5 | +0.10 | 0.8373 | 1.0000 | 0.8125 | 0.10 |
| nnskd_mobilevit_xxs_aux | 5 | +0.06 | 0.9341 | 1.0000 | 0.8125 | 0.04 |
| nnskd_mobilevit_xxs_kd | 5 | +0.44 | 0.4888 | 1.0000 | 0.8125 | 0.34 |
| nnskd_mobilevit_xxs_nm | 5 | -0.45 | 0.6185 | 1.0000 | 0.6250 | -0.24 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.05 | 0.3239 | 1.0000 | 0.2850 | 0.50 |
| pattlite | 5 | +0.70 | 0.3839 | 1.0000 | 0.4375 | 0.44 |
| resnet18 | 5 | +0.89 | 0.0925 | 0.6475 | 0.1250 | 0.98 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.76 | 0.7931 | 1.0000 | 1.0000 | 0.13 |
| microexpnet | 5 | +5.03 | 0.0329 | 0.2958 | 0.0625 | 1.43 |
| mobilevit_xxs | 5 | +0.97 | 0.4225 | 1.0000 | 0.6250 | 0.40 |
| nnskd_mobilevit_xxs_aux | 5 | -0.53 | 0.7602 | 1.0000 | 0.8125 | -0.15 |
| nnskd_mobilevit_xxs_kd | 5 | -1.26 | 0.4249 | 1.0000 | 0.6250 | -0.40 |
| nnskd_mobilevit_xxs_nm | 5 | +3.53 | 0.1905 | 1.0000 | 0.1875 | 0.70 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.12 | 0.6213 | 1.0000 | 0.8125 | -0.24 |
| pattlite | 5 | -0.21 | 0.9104 | 1.0000 | 0.6250 | -0.05 |
| resnet18 | 5 | -0.79 | 0.5618 | 1.0000 | 0.6250 | -0.28 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +4.56 | 0.0003 | 0.0025 | 0.0625 | 5.18 |
| microexpnet | 5 | +14.41 | 0.0000 | 0.0001 | 0.0625 | 11.09 |
| mobilevit_xxs | 5 | +0.72 | 0.4094 | 1.0000 | 0.8125 | 0.41 |
| nnskd_mobilevit_xxs_aux | 5 | -0.22 | 0.7252 | 1.0000 | 0.8125 | -0.17 |
| nnskd_mobilevit_xxs_kd | 5 | -0.12 | 0.8493 | 1.0000 | 0.8125 | -0.09 |
| nnskd_mobilevit_xxs_nm | 5 | +1.46 | 0.1177 | 0.6472 | 0.1250 | 0.89 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.01 | 0.9560 | 1.0000 | 1.0000 | 0.03 |
| pattlite | 5 | +0.88 | 0.1079 | 0.6472 | 0.1875 | 0.92 |
| resnet18 | 5 | +0.79 | 0.0794 | 0.5559 | 0.1250 | 1.05 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.02 | 0.0098 | 0.0783 | 0.0625 | -2.07 |
| microexpnet | 5 | +0.10 | 0.0000 | 0.0002 | 0.0625 | 10.90 |
| mobilevit_xxs | 5 | -0.01 | 0.0375 | 0.2624 | 0.0625 | -1.37 |
| nnskd_mobilevit_xxs_aux | 5 | -0.00 | 0.5483 | 1.0000 | 0.8125 | -0.29 |
| nnskd_mobilevit_xxs_kd | 5 | +0.00 | 0.3066 | 1.0000 | 0.3125 | 0.52 |
| nnskd_mobilevit_xxs_nm | 5 | +0.00 | 0.4067 | 1.0000 | 0.4375 | 0.41 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.00 | 0.5566 | 1.0000 | 0.6250 | -0.29 |
| pattlite | 5 | -0.00 | 0.7244 | 1.0000 | 0.8125 | -0.17 |
| resnet18 | 5 | -0.01 | 0.1213 | 0.7277 | 0.1875 | -0.88 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.28 | 0.8760 | 1.0000 | 1.0000 | 0.07 |
| microexpnet | 5 | +23.34 | 0.0001 | 0.0007 | 0.0625 | 7.52 |
| mobilevit_xxs | 5 | -1.92 | 0.1742 | 1.0000 | 0.1875 | -0.74 |
| nnskd_mobilevit_xxs_aux | 5 | -1.70 | 0.2991 | 1.0000 | 0.2733 | -0.53 |
| nnskd_mobilevit_xxs_kd | 5 | -0.63 | 0.7706 | 1.0000 | 1.0000 | -0.14 |
| nnskd_mobilevit_xxs_nm | 5 | -0.15 | 0.8982 | 1.0000 | 1.0000 | -0.06 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.11 | 0.6836 | 1.0000 | 0.8125 | 0.20 |
| pattlite | 5 | -0.95 | 0.6307 | 1.0000 | 1.0000 | -0.23 |
| resnet18 | 5 | -0.13 | 0.9422 | 1.0000 | 0.8125 | -0.03 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.17 | 0.1000 | 0.7998 | 0.1875 | 0.95 |
| microexpnet | 5 | +25.57 | 0.0000 | 0.0002 | 0.0625 | 9.89 |
| mobilevit_xxs | 5 | +0.10 | 0.9219 | 1.0000 | 1.0000 | 0.05 |
| nnskd_mobilevit_xxs_aux | 5 | -0.48 | 0.6935 | 1.0000 | 1.0000 | -0.19 |
| nnskd_mobilevit_xxs_kd | 5 | +0.25 | 0.7705 | 1.0000 | 0.8125 | 0.14 |
| nnskd_mobilevit_xxs_nm | 5 | +0.45 | 0.6676 | 1.0000 | 0.6250 | 0.21 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.00 | 0.9912 | 1.0000 | 1.0000 | 0.01 |
| pattlite | 5 | -0.26 | 0.8953 | 1.0000 | 1.0000 | -0.06 |
| resnet18 | 5 | +2.00 | 0.1157 | 0.8100 | 0.1250 | 0.90 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 283 | 164 | 1.984e-08 |
| efficientface | 1 | 327 | 169 | 1.166e-12 |
| efficientface | 2 | 258 | 177 | 0.0001201 |
| efficientface | 3 | 285 | 145 | 1.356e-11 |
| efficientface | 4 | 294 | 183 | 4.227e-07 |
| microexpnet | 0 | 653 | 154 | 7.403e-74 |
| microexpnet | 1 | 610 | 142 | 7.089e-70 |
| microexpnet | 2 | 575 | 135 | 1.803e-65 |
| microexpnet | 3 | 614 | 114 | 1.143e-83 |
| microexpnet | 4 | 632 | 154 | 1.726e-69 |
| mobilevit_xxs | 0 | 210 | 162 | 0.01471 |
| mobilevit_xxs | 1 | 172 | 154 | 0.3464 |
| mobilevit_xxs | 2 | 165 | 149 | 0.3973 |
| mobilevit_xxs | 3 | 154 | 150 | 0.8634 |
| mobilevit_xxs | 4 | 197 | 153 | 0.0214 |
| nnskd_mobilevit_xxs_aux | 0 | 176 | 134 | 0.01973 |
| nnskd_mobilevit_xxs_aux | 1 | 130 | 126 | 0.8513 |
| nnskd_mobilevit_xxs_aux | 2 | 151 | 154 | 0.9089 |
| nnskd_mobilevit_xxs_aux | 3 | 140 | 143 | 0.9054 |
| nnskd_mobilevit_xxs_aux | 4 | 131 | 136 | 0.8067 |
| nnskd_mobilevit_xxs_kd | 0 | 123 | 129 | 0.7529 |
| nnskd_mobilevit_xxs_kd | 1 | 113 | 118 | 0.7925 |
| nnskd_mobilevit_xxs_kd | 2 | 152 | 125 | 0.1181 |
| nnskd_mobilevit_xxs_kd | 3 | 119 | 132 | 0.4489 |
| nnskd_mobilevit_xxs_kd | 4 | 157 | 130 | 0.1247 |
| nnskd_mobilevit_xxs_nm | 0 | 170 | 159 | 0.5815 |
| nnskd_mobilevit_xxs_nm | 1 | 186 | 125 | 0.0006447 |
| nnskd_mobilevit_xxs_nm | 2 | 170 | 130 | 0.02418 |
| nnskd_mobilevit_xxs_nm | 3 | 181 | 136 | 0.01334 |
| nnskd_mobilevit_xxs_nm | 4 | 151 | 131 | 0.2578 |
| nnskd_mobilevit_xxs_tinf | 0 | 18 | 16 | 0.8642 |
| nnskd_mobilevit_xxs_tinf | 1 | 8 | 9 | 1 |
| nnskd_mobilevit_xxs_tinf | 2 | 16 | 8 | 0.1516 |
| nnskd_mobilevit_xxs_tinf | 3 | 9 | 12 | 0.6636 |
| nnskd_mobilevit_xxs_tinf | 4 | 9 | 9 | 1 |
| pattlite | 0 | 217 | 191 | 0.2158 |
| pattlite | 1 | 206 | 174 | 0.1117 |
| pattlite | 2 | 203 | 181 | 0.2839 |
| pattlite | 3 | 193 | 178 | 0.4674 |
| pattlite | 4 | 224 | 184 | 0.05338 |
| resnet18 | 0 | 196 | 190 | 0.7992 |
| resnet18 | 1 | 209 | 166 | 0.02996 |
| resnet18 | 2 | 193 | 185 | 0.7189 |
| resnet18 | 3 | 203 | 168 | 0.07739 |
| resnet18 | 4 | 199 | 175 | 0.2343 |
