# fer2013: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.05 | 0.0100 | 0.0599 | 0.0625 | 2.06 |
| microexpnet | 5 | +17.82 | 0.0000 | 0.0000 | 0.0625 | 20.92 |
| mobilevit_xxs | 5 | -0.64 | 0.1016 | 0.3079 | 0.1875 | -0.95 |
| mobilevit_xxs_ban | 5 | -1.39 | 0.0040 | 0.0283 | 0.0625 | -2.65 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.86 | 0.0003 | 0.0027 | 0.0625 | -5.24 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.66 | 0.0292 | 0.1458 | 0.0625 | -1.49 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.89 | 0.0034 | 0.0271 | 0.0625 | -2.79 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.46 | 0.0770 | 0.3079 | 0.1250 | -1.06 |
| pattlite | 5 | +0.14 | 0.4553 | 0.6517 | 0.8125 | 0.37 |
| resnet18 | 5 | -0.38 | 0.3259 | 0.6517 | 0.4375 | -0.50 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.60 | 0.2927 | 0.6839 | 0.4375 | 0.54 |
| microexpnet | 5 | +26.94 | 0.0000 | 0.0000 | 0.0625 | 31.22 |
| mobilevit_xxs | 5 | -1.24 | 0.0792 | 0.3169 | 0.1250 | -1.05 |
| mobilevit_xxs_ban | 5 | -2.09 | 0.0062 | 0.0497 | 0.0625 | -2.36 |
| nnskd_mobilevit_xxs_banlgf | 5 | -1.16 | 0.0047 | 0.0421 | 0.0625 | -2.55 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.92 | 0.0375 | 0.1877 | 0.0625 | -1.37 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.21 | 0.0257 | 0.1540 | 0.0625 | -1.55 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.64 | 0.2280 | 0.6839 | 0.3125 | -0.64 |
| pattlite | 5 | -0.46 | 0.3609 | 0.6839 | 0.3125 | -0.46 |
| resnet18 | 5 | -1.41 | 0.0170 | 0.1192 | 0.0625 | -1.76 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.40 | 0.5809 | 0.7085 | 0.6250 | 0.27 |
| microexpnet | 5 | +36.56 | 0.0000 | 0.0000 | 0.0625 | 25.26 |
| mobilevit_xxs | 5 | -1.62 | 0.0933 | 0.3732 | 0.1250 | -0.98 |
| mobilevit_xxs_ban | 5 | -2.81 | 0.0098 | 0.0787 | 0.0625 | -2.07 |
| nnskd_mobilevit_xxs_banlgf | 5 | -1.46 | 0.0058 | 0.0520 | 0.0625 | -2.40 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.22 | 0.0408 | 0.2451 | 0.1250 | -1.33 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.59 | 0.0483 | 0.2451 | 0.0625 | -1.26 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.81 | 0.3543 | 0.7085 | 0.4375 | -0.47 |
| pattlite | 5 | -1.04 | 0.2007 | 0.6022 | 0.3125 | -0.68 |
| resnet18 | 5 | -2.06 | 0.0230 | 0.1609 | 0.0625 | -1.61 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.12 | 0.5263 | 1.0000 | 0.6250 | 0.31 |
| microexpnet | 5 | +3.56 | 0.0003 | 0.0026 | 0.0625 | 5.45 |
| mobilevit_xxs | 5 | -0.24 | 0.5987 | 1.0000 | 0.6250 | -0.26 |
| mobilevit_xxs_ban | 5 | -0.81 | 0.1121 | 1.0000 | 0.1250 | -0.91 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.03 | 0.9080 | 1.0000 | 0.6250 | 0.06 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.24 | 0.5159 | 1.0000 | 0.6250 | 0.32 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.22 | 0.5695 | 1.0000 | 0.6250 | 0.28 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.36 | 0.4356 | 1.0000 | 0.4375 | 0.39 |
| pattlite | 5 | -0.20 | 0.5587 | 1.0000 | 0.6250 | -0.28 |
| resnet18 | 5 | -0.03 | 0.9580 | 1.0000 | 0.8125 | -0.03 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.30 | 0.0163 | 0.1470 | 0.0625 | 1.78 |
| microexpnet | 5 | +16.65 | 0.0000 | 0.0000 | 0.0625 | 19.98 |
| mobilevit_xxs | 5 | +0.22 | 0.8696 | 1.0000 | 1.0000 | 0.08 |
| mobilevit_xxs_ban | 5 | +0.16 | 0.9013 | 1.0000 | 1.0000 | 0.06 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.54 | 0.5631 | 1.0000 | 0.8125 | -0.28 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.22 | 0.7429 | 1.0000 | 1.0000 | 0.16 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.05 | 0.3505 | 1.0000 | 0.3125 | -0.47 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.31 | 0.2052 | 1.0000 | 0.3125 | -0.68 |
| pattlite | 5 | +3.07 | 0.0269 | 0.2156 | 0.0625 | 1.53 |
| resnet18 | 5 | +2.11 | 0.1731 | 1.0000 | 0.3125 | 0.74 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.63 | 0.0219 | 0.1973 | 0.0625 | 1.63 |
| microexpnet | 5 | +15.72 | 0.0000 | 0.0001 | 0.0625 | 14.02 |
| mobilevit_xxs | 5 | -0.22 | 0.7632 | 1.0000 | 0.6250 | -0.14 |
| mobilevit_xxs_ban | 5 | -1.15 | 0.1270 | 0.8888 | 0.1875 | -0.86 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.28 | 0.4915 | 1.0000 | 0.6250 | -0.34 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.50 | 0.3279 | 1.0000 | 0.3125 | 0.50 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.30 | 0.3833 | 1.0000 | 0.4375 | -0.44 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.24 | 0.4218 | 1.0000 | 0.4375 | -0.40 |
| pattlite | 5 | +1.63 | 0.0333 | 0.2665 | 0.1250 | 1.43 |
| resnet18 | 5 | +1.28 | 0.1397 | 0.8888 | 0.3125 | 0.82 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.01 | 0.0380 | 0.3042 | 0.0625 | -1.36 |
| microexpnet | 5 | +0.03 | 0.0022 | 0.0201 | 0.0625 | 3.12 |
| mobilevit_xxs | 5 | -0.00 | 0.5841 | 1.0000 | 0.8125 | -0.27 |
| mobilevit_xxs_ban | 5 | -0.01 | 0.1157 | 0.8100 | 0.1875 | -0.90 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.00 | 0.6678 | 1.0000 | 0.4375 | 0.21 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.00 | 0.4753 | 1.0000 | 0.8125 | -0.35 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.01 | 0.2531 | 1.0000 | 0.6250 | 0.60 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.00 | 0.5918 | 1.0000 | 0.8125 | 0.26 |
| pattlite | 5 | +0.01 | 0.4084 | 1.0000 | 0.4375 | 0.41 |
| resnet18 | 5 | +0.03 | 0.0007 | 0.0071 | 0.0625 | 4.21 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.05 | 0.1916 | 1.0000 | 0.3125 | 0.70 |
| microexpnet | 5 | +19.76 | 0.0000 | 0.0003 | 0.0625 | 9.51 |
| mobilevit_xxs | 5 | -1.32 | 0.3263 | 1.0000 | 0.4375 | -0.50 |
| mobilevit_xxs_ban | 5 | -1.12 | 0.2178 | 1.0000 | 0.3125 | -0.65 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.95 | 0.4940 | 1.0000 | 0.4375 | -0.34 |
| nnskd_mobilevit_xxs_emaonly | 5 | -2.18 | 0.1400 | 1.0000 | 0.1875 | -0.82 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.54 | 0.6884 | 1.0000 | 0.4375 | 0.19 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.13 | 0.8735 | 1.0000 | 0.6250 | 0.08 |
| pattlite | 5 | +0.73 | 0.7019 | 1.0000 | 0.6250 | 0.18 |
| resnet18 | 5 | +4.70 | 0.0385 | 0.3468 | 0.0625 | 1.36 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.87 | 0.1935 | 1.0000 | 0.3125 | 0.70 |
| microexpnet | 5 | +23.47 | 0.0002 | 0.0025 | 0.0625 | 5.51 |
| mobilevit_xxs | 5 | -1.35 | 0.4972 | 1.0000 | 0.6250 | -0.33 |
| mobilevit_xxs_ban | 5 | -0.92 | 0.5466 | 1.0000 | 0.6250 | -0.29 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.03 | 0.9864 | 1.0000 | 1.0000 | -0.01 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.02 | 0.3238 | 1.0000 | 0.4375 | -0.50 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.46 | 0.4024 | 1.0000 | 0.4375 | 0.42 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.84 | 0.6104 | 1.0000 | 0.8125 | 0.25 |
| pattlite | 5 | +1.85 | 0.4973 | 1.0000 | 0.6250 | 0.33 |
| resnet18 | 5 | +5.09 | 0.0535 | 0.4816 | 0.1250 | 1.21 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 305 | 281 | 0.3421 |
| efficientface | 1 | 341 | 274 | 0.007731 |
| efficientface | 2 | 329 | 307 | 0.405 |
| efficientface | 3 | 337 | 295 | 0.1028 |
| efficientface | 4 | 309 | 276 | 0.1858 |
| microexpnet | 0 | 891 | 257 | 2.73e-82 |
| microexpnet | 1 | 921 | 258 | 1.026e-87 |
| microexpnet | 2 | 875 | 249 | 4.965e-82 |
| microexpnet | 3 | 843 | 244 | 1.195e-77 |
| microexpnet | 4 | 922 | 246 | 2.572e-92 |
| mobilevit_xxs | 0 | 289 | 279 | 0.7057 |
| mobilevit_xxs | 1 | 275 | 281 | 0.8321 |
| mobilevit_xxs | 2 | 251 | 286 | 0.1422 |
| mobilevit_xxs | 3 | 251 | 285 | 0.154 |
| mobilevit_xxs | 4 | 248 | 297 | 0.03968 |
| mobilevit_xxs_ban | 0 | 257 | 279 | 0.3644 |
| mobilevit_xxs_ban | 1 | 234 | 279 | 0.05195 |
| mobilevit_xxs_ban | 2 | 232 | 295 | 0.006862 |
| mobilevit_xxs_ban | 3 | 217 | 288 | 0.001812 |
| mobilevit_xxs_ban | 4 | 237 | 286 | 0.03573 |
| nnskd_mobilevit_xxs_banlgf | 0 | 167 | 198 | 0.1162 |
| nnskd_mobilevit_xxs_banlgf | 1 | 186 | 226 | 0.05455 |
| nnskd_mobilevit_xxs_banlgf | 2 | 182 | 214 | 0.1192 |
| nnskd_mobilevit_xxs_banlgf | 3 | 173 | 201 | 0.1626 |
| nnskd_mobilevit_xxs_banlgf | 4 | 192 | 216 | 0.2548 |
| nnskd_mobilevit_xxs_emaonly | 0 | 265 | 268 | 0.931 |
| nnskd_mobilevit_xxs_emaonly | 1 | 238 | 253 | 0.5276 |
| nnskd_mobilevit_xxs_emaonly | 2 | 246 | 280 | 0.1501 |
| nnskd_mobilevit_xxs_emaonly | 3 | 251 | 274 | 0.337 |
| nnskd_mobilevit_xxs_emaonly | 4 | 239 | 283 | 0.05972 |
| nnskd_mobilevit_xxs_gen2 | 0 | 161 | 195 | 0.08015 |
| nnskd_mobilevit_xxs_gen2 | 1 | 166 | 212 | 0.02052 |
| nnskd_mobilevit_xxs_gen2 | 2 | 165 | 179 | 0.4834 |
| nnskd_mobilevit_xxs_gen2 | 3 | 177 | 211 | 0.09374 |
| nnskd_mobilevit_xxs_gen2 | 4 | 189 | 221 | 0.1257 |
| nnskd_mobilevit_xxs_v3 | 0 | 222 | 217 | 0.8486 |
| nnskd_mobilevit_xxs_v3 | 1 | 211 | 226 | 0.5031 |
| nnskd_mobilevit_xxs_v3 | 2 | 220 | 241 | 0.3516 |
| nnskd_mobilevit_xxs_v3 | 3 | 181 | 194 | 0.5355 |
| nnskd_mobilevit_xxs_v3 | 4 | 196 | 234 | 0.07425 |
| pattlite | 0 | 325 | 296 | 0.2612 |
| pattlite | 1 | 321 | 324 | 0.9372 |
| pattlite | 2 | 309 | 302 | 0.8082 |
| pattlite | 3 | 297 | 302 | 0.8702 |
| pattlite | 4 | 299 | 301 | 0.9674 |
| resnet18 | 0 | 294 | 322 | 0.2766 |
| resnet18 | 1 | 336 | 304 | 0.2204 |
| resnet18 | 2 | 309 | 335 | 0.3246 |
| resnet18 | 3 | 295 | 331 | 0.1618 |
| resnet18 | 4 | 324 | 334 | 0.7257 |
