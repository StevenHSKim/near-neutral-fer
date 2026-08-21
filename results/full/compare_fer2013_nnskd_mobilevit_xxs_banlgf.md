# fer2013: nnskd_mobilevit_xxs_banlgf vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.91 | 0.0024 | 0.0191 | 0.0625 | 3.06 |
| microexpnet | 5 | +18.68 | 0.0000 | 0.0000 | 0.0625 | 21.19 |
| mobilevit_xxs | 5 | +0.23 | 0.5504 | 1.0000 | 0.8125 | 0.29 |
| mobilevit_xxs_ban | 5 | -0.53 | 0.1110 | 0.6661 | 0.1875 | -0.91 |
| nnskd_mobilevit_xxs | 5 | +0.86 | 0.0003 | 0.0027 | 0.0625 | 5.24 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.20 | 0.4632 | 1.0000 | 0.4375 | 0.36 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.03 | 0.8457 | 1.0000 | 0.6250 | -0.09 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.41 | 0.1556 | 0.7780 | 0.1875 | 0.78 |
| pattlite | 5 | +1.01 | 0.0063 | 0.0441 | 0.0625 | 2.35 |
| resnet18 | 5 | +0.48 | 0.2847 | 1.0000 | 0.3125 | 0.55 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.76 | 0.0556 | 0.4445 | 0.0625 | 1.20 |
| microexpnet | 5 | +28.11 | 0.0000 | 0.0000 | 0.0625 | 25.44 |
| mobilevit_xxs | 5 | -0.07 | 0.9099 | 1.0000 | 1.0000 | -0.05 |
| mobilevit_xxs_ban | 5 | -0.93 | 0.1451 | 0.8713 | 0.1875 | -0.81 |
| nnskd_mobilevit_xxs | 5 | +1.16 | 0.0047 | 0.0421 | 0.0625 | 2.55 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.24 | 0.6313 | 1.0000 | 0.6250 | 0.23 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.05 | 0.7878 | 1.0000 | 0.8125 | -0.13 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.53 | 0.3789 | 1.0000 | 0.6250 | 0.44 |
| pattlite | 5 | +0.70 | 0.1245 | 0.8713 | 0.0625 | 0.87 |
| resnet18 | 5 | -0.25 | 0.6581 | 1.0000 | 0.6250 | -0.21 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.87 | 0.1052 | 0.8419 | 0.1250 | 0.93 |
| microexpnet | 5 | +38.03 | 0.0000 | 0.0000 | 0.0625 | 21.94 |
| mobilevit_xxs | 5 | -0.15 | 0.8619 | 1.0000 | 1.0000 | -0.08 |
| mobilevit_xxs_ban | 5 | -1.34 | 0.1345 | 0.9414 | 0.1875 | -0.84 |
| nnskd_mobilevit_xxs | 5 | +1.46 | 0.0058 | 0.0520 | 0.0625 | 2.40 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.24 | 0.6934 | 1.0000 | 0.6250 | 0.19 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.13 | 0.7327 | 1.0000 | 1.0000 | -0.16 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.65 | 0.4809 | 1.0000 | 0.6250 | 0.35 |
| pattlite | 5 | +0.42 | 0.5090 | 1.0000 | 0.8125 | 0.32 |
| resnet18 | 5 | -0.60 | 0.4519 | 1.0000 | 0.6250 | -0.37 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.09 | 0.5955 | 1.0000 | 0.4375 | 0.26 |
| microexpnet | 5 | +3.53 | 0.0000 | 0.0001 | 0.0625 | 12.66 |
| mobilevit_xxs | 5 | -0.27 | 0.4302 | 1.0000 | 0.4375 | -0.39 |
| mobilevit_xxs_ban | 5 | -0.84 | 0.0315 | 0.2832 | 0.0625 | -1.45 |
| nnskd_mobilevit_xxs | 5 | -0.03 | 0.9080 | 1.0000 | 0.6250 | -0.06 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.21 | 0.3700 | 1.0000 | 0.3125 | 0.45 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.20 | 0.5934 | 1.0000 | 0.6250 | 0.26 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.34 | 0.3506 | 1.0000 | 0.4375 | 0.47 |
| pattlite | 5 | -0.23 | 0.4456 | 1.0000 | 0.3125 | -0.38 |
| resnet18 | 5 | -0.05 | 0.8664 | 1.0000 | 0.8125 | -0.08 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.84 | 0.1009 | 0.8072 | 0.1875 | 0.95 |
| microexpnet | 5 | +17.19 | 0.0000 | 0.0003 | 0.0625 | 9.23 |
| mobilevit_xxs | 5 | +0.77 | 0.6399 | 1.0000 | 0.8125 | 0.23 |
| mobilevit_xxs_ban | 5 | +0.70 | 0.6339 | 1.0000 | 0.8125 | 0.23 |
| nnskd_mobilevit_xxs | 5 | +0.54 | 0.5631 | 1.0000 | 0.8125 | 0.28 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.77 | 0.3673 | 1.0000 | 0.4375 | 0.45 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.51 | 0.6347 | 1.0000 | 0.4375 | -0.23 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.77 | 0.4978 | 1.0000 | 0.4375 | -0.33 |
| pattlite | 5 | +3.61 | 0.0659 | 0.5934 | 0.1250 | 1.12 |
| resnet18 | 5 | +2.65 | 0.1128 | 0.8072 | 0.1250 | 0.91 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.91 | 0.0641 | 0.5130 | 0.0625 | 1.13 |
| microexpnet | 5 | +16.00 | 0.0000 | 0.0001 | 0.0625 | 12.55 |
| mobilevit_xxs | 5 | +0.06 | 0.9475 | 1.0000 | 1.0000 | 0.03 |
| mobilevit_xxs_ban | 5 | -0.87 | 0.2574 | 1.0000 | 0.3125 | -0.59 |
| nnskd_mobilevit_xxs | 5 | +0.28 | 0.4915 | 1.0000 | 0.6250 | 0.34 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.77 | 0.2610 | 1.0000 | 0.3125 | 0.58 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.02 | 0.9463 | 1.0000 | 1.0000 | -0.03 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.04 | 0.9495 | 1.0000 | 1.0000 | 0.03 |
| pattlite | 5 | +1.91 | 0.0493 | 0.4439 | 0.1250 | 1.25 |
| resnet18 | 5 | +1.56 | 0.1274 | 0.8916 | 0.1250 | 0.86 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.01 | 0.0305 | 0.2441 | 0.0625 | -1.47 |
| microexpnet | 5 | +0.03 | 0.0001 | 0.0010 | 0.0625 | 6.89 |
| mobilevit_xxs | 5 | -0.00 | 0.1300 | 0.6502 | 0.1875 | -0.85 |
| mobilevit_xxs_ban | 5 | -0.01 | 0.0479 | 0.3353 | 0.1250 | -1.26 |
| nnskd_mobilevit_xxs | 5 | -0.00 | 0.6678 | 1.0000 | 0.4375 | -0.21 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.01 | 0.0974 | 0.5844 | 0.1250 | -0.96 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.00 | 0.3699 | 1.0000 | 0.4375 | 0.45 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.00 | 0.8474 | 1.0000 | 1.0000 | 0.09 |
| pattlite | 5 | +0.00 | 0.2525 | 1.0000 | 0.3125 | 0.60 |
| resnet18 | 5 | +0.02 | 0.0063 | 0.0568 | 0.0625 | 2.35 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.00 | 0.1036 | 0.7255 | 0.1250 | 0.94 |
| microexpnet | 5 | +20.71 | 0.0000 | 0.0000 | 0.0625 | 18.18 |
| mobilevit_xxs | 5 | -0.37 | 0.7290 | 1.0000 | 0.8125 | -0.17 |
| mobilevit_xxs_ban | 5 | -0.17 | 0.8829 | 1.0000 | 0.8125 | -0.07 |
| nnskd_mobilevit_xxs | 5 | +0.95 | 0.4940 | 1.0000 | 0.4375 | 0.34 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.23 | 0.3597 | 1.0000 | 0.3125 | -0.46 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.49 | 0.0042 | 0.0380 | 0.0625 | 2.62 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.08 | 0.2947 | 1.0000 | 0.1975 | 0.54 |
| pattlite | 5 | +1.68 | 0.2509 | 1.0000 | 0.1875 | 0.60 |
| resnet18 | 5 | +5.65 | 0.0119 | 0.0953 | 0.0625 | 1.96 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.90 | 0.1604 | 1.0000 | 0.1875 | 0.77 |
| microexpnet | 5 | +23.50 | 0.0000 | 0.0001 | 0.0625 | 13.71 |
| mobilevit_xxs | 5 | -1.32 | 0.3081 | 1.0000 | 0.4375 | -0.52 |
| mobilevit_xxs_ban | 5 | -0.89 | 0.4275 | 1.0000 | 0.4375 | -0.39 |
| nnskd_mobilevit_xxs | 5 | +0.03 | 0.9864 | 1.0000 | 1.0000 | 0.01 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.99 | 0.3434 | 1.0000 | 0.4375 | -0.48 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.49 | 0.0201 | 0.1810 | 0.0625 | 1.67 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.87 | 0.4036 | 1.0000 | 0.4375 | 0.42 |
| pattlite | 5 | +1.88 | 0.3333 | 1.0000 | 0.3125 | 0.49 |
| resnet18 | 5 | +5.12 | 0.0362 | 0.2900 | 0.1250 | 1.39 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 309 | 254 | 0.02277 |
| efficientface | 1 | 357 | 250 | 1.612e-05 |
| efficientface | 2 | 336 | 282 | 0.03293 |
| efficientface | 3 | 335 | 265 | 0.004808 |
| efficientface | 4 | 313 | 256 | 0.01881 |
| microexpnet | 0 | 924 | 259 | 6.139e-88 |
| microexpnet | 1 | 931 | 228 | 3.712e-101 |
| microexpnet | 2 | 901 | 243 | 2.809e-89 |
| microexpnet | 3 | 872 | 245 | 7.12e-83 |
| microexpnet | 4 | 962 | 262 | 2.864e-94 |
| mobilevit_xxs | 0 | 264 | 223 | 0.06979 |
| mobilevit_xxs | 1 | 281 | 247 | 0.1509 |
| mobilevit_xxs | 2 | 240 | 243 | 0.9275 |
| mobilevit_xxs | 3 | 242 | 248 | 0.8213 |
| mobilevit_xxs | 4 | 246 | 271 | 0.2912 |
| mobilevit_xxs_ban | 0 | 252 | 243 | 0.7192 |
| mobilevit_xxs_ban | 1 | 237 | 242 | 0.855 |
| mobilevit_xxs_ban | 2 | 223 | 254 | 0.1695 |
| mobilevit_xxs_ban | 3 | 208 | 251 | 0.04983 |
| mobilevit_xxs_ban | 4 | 231 | 256 | 0.2768 |
| nnskd_mobilevit_xxs | 0 | 198 | 167 | 0.1162 |
| nnskd_mobilevit_xxs | 1 | 226 | 186 | 0.05455 |
| nnskd_mobilevit_xxs | 2 | 214 | 182 | 0.1192 |
| nnskd_mobilevit_xxs | 3 | 201 | 173 | 0.1626 |
| nnskd_mobilevit_xxs | 4 | 216 | 192 | 0.2548 |
| nnskd_mobilevit_xxs_emaonly | 0 | 254 | 226 | 0.2178 |
| nnskd_mobilevit_xxs_emaonly | 1 | 234 | 209 | 0.2541 |
| nnskd_mobilevit_xxs_emaonly | 2 | 242 | 244 | 0.9638 |
| nnskd_mobilevit_xxs_emaonly | 3 | 254 | 249 | 0.8585 |
| nnskd_mobilevit_xxs_emaonly | 4 | 231 | 251 | 0.3868 |
| nnskd_mobilevit_xxs_gen2 | 0 | 130 | 133 | 0.9019 |
| nnskd_mobilevit_xxs_gen2 | 1 | 148 | 154 | 0.7736 |
| nnskd_mobilevit_xxs_gen2 | 2 | 172 | 154 | 0.3464 |
| nnskd_mobilevit_xxs_gen2 | 3 | 152 | 158 | 0.7765 |
| nnskd_mobilevit_xxs_gen2 | 4 | 143 | 151 | 0.6832 |
| nnskd_mobilevit_xxs_v3 | 0 | 251 | 215 | 0.1048 |
| nnskd_mobilevit_xxs_v3 | 1 | 226 | 201 | 0.2454 |
| nnskd_mobilevit_xxs_v3 | 2 | 230 | 219 | 0.637 |
| nnskd_mobilevit_xxs_v3 | 3 | 209 | 194 | 0.4856 |
| nnskd_mobilevit_xxs_v3 | 4 | 177 | 191 | 0.498 |
| pattlite | 0 | 321 | 261 | 0.01439 |
| pattlite | 1 | 341 | 304 | 0.1563 |
| pattlite | 2 | 316 | 277 | 0.1186 |
| pattlite | 3 | 297 | 274 | 0.3572 |
| pattlite | 4 | 308 | 286 | 0.3889 |
| resnet18 | 0 | 289 | 286 | 0.9335 |
| resnet18 | 1 | 336 | 264 | 0.003713 |
| resnet18 | 2 | 312 | 306 | 0.8406 |
| resnet18 | 3 | 297 | 305 | 0.7754 |
| resnet18 | 4 | 313 | 299 | 0.5993 |
