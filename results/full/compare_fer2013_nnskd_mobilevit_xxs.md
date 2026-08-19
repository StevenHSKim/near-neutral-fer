# fer2013: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.05 | 0.0100 | 0.0400 | 0.0625 | 2.06 |
| microexpnet | 5 | +17.82 | 0.0000 | 0.0000 | 0.0625 | 20.92 |
| mobilevit_xxs | 5 | -0.64 | 0.1016 | 0.3049 | 0.1875 | -0.95 |
| pattlite | 5 | +0.14 | 0.4553 | 0.6517 | 0.8125 | 0.37 |
| resnet18 | 5 | -0.38 | 0.3259 | 0.6517 | 0.4375 | -0.50 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.60 | 0.2927 | 0.5855 | 0.4375 | 0.54 |
| microexpnet | 5 | +26.94 | 0.0000 | 0.0000 | 0.0625 | 31.22 |
| mobilevit_xxs | 5 | -1.24 | 0.0792 | 0.2377 | 0.1250 | -1.05 |
| pattlite | 5 | -0.46 | 0.3609 | 0.5855 | 0.3125 | -0.46 |
| resnet18 | 5 | -1.41 | 0.0170 | 0.0681 | 0.0625 | -1.76 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.40 | 0.5809 | 0.5809 | 0.6250 | 0.27 |
| microexpnet | 5 | +36.56 | 0.0000 | 0.0000 | 0.0625 | 25.26 |
| mobilevit_xxs | 5 | -1.62 | 0.0933 | 0.2799 | 0.1250 | -0.98 |
| pattlite | 5 | -1.04 | 0.2007 | 0.4015 | 0.3125 | -0.68 |
| resnet18 | 5 | -2.06 | 0.0230 | 0.0919 | 0.0625 | -1.61 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.12 | 0.5263 | 1.0000 | 0.6250 | 0.31 |
| microexpnet | 5 | +3.56 | 0.0003 | 0.0013 | 0.0625 | 5.45 |
| mobilevit_xxs | 5 | -0.24 | 0.5987 | 1.0000 | 0.6250 | -0.26 |
| pattlite | 5 | -0.20 | 0.5587 | 1.0000 | 0.6250 | -0.28 |
| resnet18 | 5 | -0.03 | 0.9580 | 1.0000 | 0.8125 | -0.03 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.30 | 0.0163 | 0.0654 | 0.0625 | 1.78 |
| microexpnet | 5 | +16.65 | 0.0000 | 0.0000 | 0.0625 | 19.98 |
| mobilevit_xxs | 5 | +0.22 | 0.8696 | 0.8696 | 1.0000 | 0.08 |
| pattlite | 5 | +3.07 | 0.0269 | 0.0808 | 0.0625 | 1.53 |
| resnet18 | 5 | +2.11 | 0.1731 | 0.3461 | 0.3125 | 0.74 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.63 | 0.0219 | 0.0877 | 0.0625 | 1.63 |
| microexpnet | 5 | +15.72 | 0.0000 | 0.0000 | 0.0625 | 14.02 |
| mobilevit_xxs | 5 | -0.22 | 0.7632 | 0.7632 | 0.6250 | -0.14 |
| pattlite | 5 | +1.63 | 0.0333 | 0.0999 | 0.1250 | 1.43 |
| resnet18 | 5 | +1.28 | 0.1397 | 0.2794 | 0.3125 | 0.82 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.01 | 0.0380 | 0.1141 | 0.0625 | -1.36 |
| microexpnet | 5 | +0.03 | 0.0022 | 0.0089 | 0.0625 | 3.12 |
| mobilevit_xxs | 5 | -0.00 | 0.5841 | 0.8168 | 0.8125 | -0.27 |
| pattlite | 5 | +0.01 | 0.4084 | 0.8168 | 0.4375 | 0.41 |
| resnet18 | 5 | +0.03 | 0.0007 | 0.0035 | 0.0625 | 4.21 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.05 | 0.1916 | 0.5747 | 0.3125 | 0.70 |
| microexpnet | 5 | +19.76 | 0.0000 | 0.0001 | 0.0625 | 9.51 |
| mobilevit_xxs | 5 | -1.32 | 0.3263 | 0.6526 | 0.4375 | -0.50 |
| pattlite | 5 | +0.73 | 0.7019 | 0.7019 | 0.6250 | 0.18 |
| resnet18 | 5 | +4.70 | 0.0385 | 0.1541 | 0.0625 | 1.36 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.87 | 0.1935 | 0.5806 | 0.3125 | 0.70 |
| microexpnet | 5 | +23.47 | 0.0002 | 0.0012 | 0.0625 | 5.51 |
| mobilevit_xxs | 5 | -1.35 | 0.4972 | 0.9943 | 0.6250 | -0.33 |
| pattlite | 5 | +1.85 | 0.4973 | 0.9943 | 0.6250 | 0.33 |
| resnet18 | 5 | +5.09 | 0.0535 | 0.2140 | 0.1250 | 1.21 |

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
