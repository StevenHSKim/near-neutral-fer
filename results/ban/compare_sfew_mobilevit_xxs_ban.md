# sfew: mobilevit_xxs_ban vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -1.61 | 0.3268 | 1.0000 | 0.4375 | -0.50 |
| microexpnet | 5 | +12.65 | 0.0014 | 0.0184 | 0.0625 | 3.52 |
| mobilevit_xxs | 5 | +0.05 | 0.9694 | 1.0000 | 1.0000 | 0.02 |
| mobilevit_xxs_recipe | 5 | +1.12 | 0.2526 | 1.0000 | 0.3125 | 0.60 |
| nnskd_mobilevit_xxs | 5 | -0.97 | 0.6135 | 1.0000 | 0.4375 | -0.24 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.68 | 0.3655 | 1.0000 | 0.4652 | -0.46 |
| nnskd_mobilevit_xxs_ema | 5 | +0.19 | 0.8741 | 1.0000 | 0.8125 | 0.08 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.24 | 0.8473 | 1.0000 | 0.7150 | 0.09 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.63 | 0.5234 | 1.0000 | 0.6250 | -0.31 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.54 | 0.6805 | 1.0000 | 0.6250 | -0.20 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.58 | 0.6756 | 1.0000 | 0.6250 | -0.20 |
| pattlite | 5 | +1.95 | 0.3434 | 1.0000 | 0.4375 | 0.48 |
| resnet18 | 5 | -1.61 | 0.3238 | 1.0000 | 0.3125 | -0.50 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -1.52 | 0.1884 | 1.0000 | 0.3125 | -0.71 |
| microexpnet | 5 | +17.10 | 0.0004 | 0.0058 | 0.0625 | 4.75 |
| mobilevit_xxs | 5 | -0.30 | 0.8400 | 1.0000 | 1.0000 | -0.10 |
| mobilevit_xxs_recipe | 5 | -0.73 | 0.5344 | 1.0000 | 0.4375 | -0.30 |
| nnskd_mobilevit_xxs | 5 | -0.83 | 0.6403 | 1.0000 | 0.6250 | -0.23 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.19 | 0.8717 | 1.0000 | 0.8125 | -0.08 |
| nnskd_mobilevit_xxs_ema | 5 | -0.19 | 0.9092 | 1.0000 | 1.0000 | -0.05 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.54 | 0.4348 | 1.0000 | 0.4375 | 0.39 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.88 | 0.4916 | 1.0000 | 0.8125 | -0.34 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.79 | 0.2875 | 1.0000 | 0.4375 | -0.55 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.77 | 0.5230 | 1.0000 | 0.4375 | -0.31 |
| pattlite | 5 | +1.59 | 0.4332 | 1.0000 | 0.4375 | 0.39 |
| resnet18 | 5 | -0.11 | 0.9480 | 1.0000 | 1.0000 | -0.03 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -2.27 | 0.1763 | 1.0000 | 0.1875 | -0.73 |
| microexpnet | 5 | +10.23 | 0.0034 | 0.0437 | 0.0625 | 2.79 |
| mobilevit_xxs | 5 | -0.34 | 0.7921 | 1.0000 | 0.6250 | -0.13 |
| mobilevit_xxs_recipe | 5 | -1.79 | 0.4170 | 1.0000 | 0.6250 | -0.40 |
| nnskd_mobilevit_xxs | 5 | -1.84 | 0.1310 | 1.0000 | 0.3125 | -0.85 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.10 | 0.8730 | 1.0000 | 0.8125 | 0.08 |
| nnskd_mobilevit_xxs_ema | 5 | +1.08 | 0.5595 | 1.0000 | 0.6250 | 0.28 |
| nnskd_mobilevit_xxs_emaonly | 5 | +2.08 | 0.4546 | 1.0000 | 0.4375 | 0.37 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.05 | 0.3886 | 1.0000 | 0.4375 | -0.43 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.75 | 0.3786 | 1.0000 | 0.6250 | -0.44 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.01 | 0.5812 | 1.0000 | 1.0000 | -0.27 |
| pattlite | 5 | +2.06 | 0.3392 | 1.0000 | 0.4375 | 0.48 |
| resnet18 | 5 | +0.35 | 0.8259 | 1.0000 | 1.0000 | 0.10 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +5.78 | 0.2715 | 1.0000 | 0.4375 | 0.57 |
| microexpnet | 5 | -6.57 | 0.1023 | 1.0000 | 0.1875 | -0.94 |
| mobilevit_xxs | 5 | +3.65 | 0.4249 | 1.0000 | 0.4375 | 0.40 |
| mobilevit_xxs_recipe | 5 | +0.85 | 0.8658 | 1.0000 | 1.0000 | 0.08 |
| nnskd_mobilevit_xxs | 5 | +2.67 | 0.5618 | 1.0000 | 0.4652 | 0.28 |
| nnskd_mobilevit_xxs_banlgf | 5 | +3.95 | 0.2361 | 1.0000 | 0.3125 | 0.62 |
| nnskd_mobilevit_xxs_ema | 5 | +4.86 | 0.3887 | 1.0000 | 0.6250 | 0.43 |
| nnskd_mobilevit_xxs_emaonly | 5 | +9.18 | 0.2138 | 1.0000 | 0.3125 | 0.66 |
| nnskd_mobilevit_xxs_gen2 | 5 | +4.32 | 0.3335 | 1.0000 | 0.8125 | 0.49 |
| nnskd_mobilevit_xxs_v2 | 5 | +2.55 | 0.4921 | 1.0000 | 0.3125 | 0.34 |
| nnskd_mobilevit_xxs_v3 | 5 | +4.86 | 0.2135 | 1.0000 | 0.1875 | 0.66 |
| pattlite | 5 | +5.41 | 0.1768 | 1.0000 | 0.3125 | 0.73 |
| resnet18 | 5 | +10.03 | 0.0298 | 0.3873 | 0.1250 | 1.48 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -7.80 | 0.2913 | 1.0000 | 0.3125 | -0.54 |
| microexpnet | 5 | +33.90 | 0.0017 | 0.0217 | 0.0625 | 3.37 |
| mobilevit_xxs | 5 | -6.10 | 0.4179 | 1.0000 | 0.4652 | -0.40 |
| mobilevit_xxs_recipe | 5 | +2.44 | 0.8122 | 1.0000 | 1.0000 | 0.11 |
| nnskd_mobilevit_xxs | 5 | -8.05 | 0.4685 | 1.0000 | 0.6250 | -0.36 |
| nnskd_mobilevit_xxs_banlgf | 5 | -6.34 | 0.4901 | 1.0000 | 0.5930 | -0.34 |
| nnskd_mobilevit_xxs_ema | 5 | -8.05 | 0.4225 | 1.0000 | 0.6250 | -0.40 |
| nnskd_mobilevit_xxs_emaonly | 5 | -11.71 | 0.1404 | 1.0000 | 0.1875 | -0.82 |
| nnskd_mobilevit_xxs_gen2 | 5 | -7.56 | 0.4035 | 1.0000 | 0.4652 | -0.42 |
| nnskd_mobilevit_xxs_v2 | 5 | -3.66 | 0.5695 | 1.0000 | 0.6250 | -0.28 |
| nnskd_mobilevit_xxs_v3 | 5 | -8.29 | 0.2706 | 1.0000 | 0.3125 | -0.57 |
| pattlite | 5 | +1.22 | 0.8870 | 1.0000 | 0.4652 | 0.07 |
| resnet18 | 5 | -15.12 | 0.0174 | 0.2088 | 0.0625 | -1.75 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -2.03 | 0.5700 | 1.0000 | 0.8125 | -0.28 |
| microexpnet | 5 | +32.15 | 0.0012 | 0.0154 | 0.0625 | 3.69 |
| mobilevit_xxs | 5 | -2.75 | 0.3979 | 1.0000 | 0.6250 | -0.42 |
| mobilevit_xxs_recipe | 5 | +1.73 | 0.7294 | 1.0000 | 0.8125 | 0.17 |
| nnskd_mobilevit_xxs | 5 | -4.51 | 0.4379 | 1.0000 | 0.6250 | -0.38 |
| nnskd_mobilevit_xxs_banlgf | 5 | -2.37 | 0.6457 | 1.0000 | 0.6250 | -0.22 |
| nnskd_mobilevit_xxs_ema | 5 | -1.68 | 0.6222 | 1.0000 | 0.6250 | -0.24 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.94 | 0.4152 | 1.0000 | 0.4375 | -0.41 |
| nnskd_mobilevit_xxs_gen2 | 5 | -2.64 | 0.5711 | 1.0000 | 1.0000 | -0.28 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.53 | 0.6744 | 1.0000 | 1.0000 | -0.20 |
| nnskd_mobilevit_xxs_v3 | 5 | -3.46 | 0.4668 | 1.0000 | 0.8125 | -0.36 |
| pattlite | 5 | +4.59 | 0.3085 | 1.0000 | 0.4375 | 0.52 |
| resnet18 | 5 | -3.19 | 0.1233 | 1.0000 | 0.1250 | -0.87 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.09 | 0.0028 | 0.0282 | 0.0625 | -2.93 |
| microexpnet | 5 | -0.29 | 0.0001 | 0.0012 | 0.0625 | -7.03 |
| mobilevit_xxs | 5 | +0.00 | 0.9977 | 1.0000 | 0.8125 | 0.00 |
| mobilevit_xxs_recipe | 5 | -0.08 | 0.0043 | 0.0383 | 0.0625 | -2.62 |
| nnskd_mobilevit_xxs | 5 | +0.03 | 0.1143 | 0.5714 | 0.1875 | 0.90 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.02 | 0.1887 | 0.7547 | 0.3125 | 0.71 |
| nnskd_mobilevit_xxs_ema | 5 | -0.12 | 0.0010 | 0.0119 | 0.0625 | -3.86 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.06 | 0.2291 | 0.7547 | 0.1875 | -0.63 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.01 | 0.5876 | 1.0000 | 0.6250 | 0.26 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.10 | 0.0014 | 0.0156 | 0.0625 | -3.51 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.02 | 0.0475 | 0.2852 | 0.1250 | 1.26 |
| pattlite | 5 | -0.10 | 0.0060 | 0.0478 | 0.0625 | -2.38 |
| resnet18 | 5 | -0.12 | 0.0061 | 0.0478 | 0.0625 | -2.37 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +5.03 | 0.4001 | 1.0000 | 0.4375 | 0.42 |
| microexpnet | 5 | +4.42 | 0.5210 | 1.0000 | 0.6250 | 0.31 |
| mobilevit_xxs | 5 | +0.13 | 0.9805 | 1.0000 | 0.8125 | 0.01 |
| mobilevit_xxs_recipe | 5 | +0.76 | 0.8806 | 1.0000 | 1.0000 | 0.07 |
| nnskd_mobilevit_xxs | 5 | +1.53 | 0.8309 | 1.0000 | 1.0000 | 0.10 |
| nnskd_mobilevit_xxs_banlgf | 5 | +2.44 | 0.5872 | 1.0000 | 1.0000 | 0.26 |
| nnskd_mobilevit_xxs_ema | 5 | +1.17 | 0.8548 | 1.0000 | 1.0000 | 0.09 |
| nnskd_mobilevit_xxs_emaonly | 5 | +3.37 | 0.6418 | 1.0000 | 0.6250 | 0.22 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.15 | 0.9796 | 1.0000 | 1.0000 | 0.01 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.47 | 0.9052 | 1.0000 | 1.0000 | -0.06 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.21 | 0.8491 | 1.0000 | 1.0000 | 0.09 |
| pattlite | 5 | +6.97 | 0.1525 | 1.0000 | 0.1875 | 0.79 |
| resnet18 | 5 | -6.80 | 0.3801 | 1.0000 | 0.4375 | -0.44 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.28 | 0.6938 | 1.0000 | 0.8125 | 0.19 |
| microexpnet | 5 | +5.67 | 0.1566 | 1.0000 | 0.1250 | 0.78 |
| mobilevit_xxs | 5 | -0.74 | 0.8099 | 1.0000 | 1.0000 | -0.11 |
| mobilevit_xxs_recipe | 5 | -0.38 | 0.9039 | 1.0000 | 1.0000 | -0.06 |
| nnskd_mobilevit_xxs | 5 | -2.03 | 0.6746 | 1.0000 | 0.8125 | -0.20 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.19 | 0.9575 | 1.0000 | 0.8125 | -0.03 |
| nnskd_mobilevit_xxs_ema | 5 | -1.09 | 0.8104 | 1.0000 | 0.8125 | -0.11 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.95 | 0.8306 | 1.0000 | 1.0000 | 0.10 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.57 | 0.6152 | 1.0000 | 0.8125 | -0.24 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.88 | 0.5086 | 1.0000 | 0.8125 | -0.32 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.28 | 0.9447 | 1.0000 | 1.0000 | 0.03 |
| pattlite | 5 | +2.08 | 0.5241 | 1.0000 | 0.6250 | 0.31 |
| resnet18 | 5 | -4.89 | 0.2046 | 1.0000 | 0.3125 | -0.68 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 67 | 72 | 0.7345 |
| efficientface | 1 | 56 | 53 | 0.8482 |
| efficientface | 2 | 49 | 70 | 0.06629 |
| efficientface | 3 | 47 | 66 | 0.08995 |
| efficientface | 4 | 60 | 51 | 0.4478 |
| microexpnet | 0 | 88 | 23 | 3.796e-10 |
| microexpnet | 1 | 103 | 33 | 1.42e-09 |
| microexpnet | 2 | 87 | 40 | 3.693e-05 |
| microexpnet | 3 | 87 | 45 | 0.0003232 |
| microexpnet | 4 | 95 | 59 | 0.004637 |
| mobilevit_xxs | 0 | 50 | 51 | 1 |
| mobilevit_xxs | 1 | 34 | 27 | 0.4426 |
| mobilevit_xxs | 2 | 38 | 25 | 0.1299 |
| mobilevit_xxs | 3 | 31 | 33 | 0.9007 |
| mobilevit_xxs | 4 | 27 | 43 | 0.07224 |
| mobilevit_xxs_recipe | 0 | 54 | 50 | 0.7688 |
| mobilevit_xxs_recipe | 1 | 42 | 29 | 0.1539 |
| mobilevit_xxs_recipe | 2 | 43 | 50 | 0.5341 |
| mobilevit_xxs_recipe | 3 | 39 | 36 | 0.8176 |
| mobilevit_xxs_recipe | 4 | 53 | 43 | 0.3584 |
| nnskd_mobilevit_xxs | 0 | 51 | 61 | 0.3952 |
| nnskd_mobilevit_xxs | 1 | 58 | 36 | 0.02977 |
| nnskd_mobilevit_xxs | 2 | 41 | 42 | 1 |
| nnskd_mobilevit_xxs | 3 | 37 | 59 | 0.03155 |
| nnskd_mobilevit_xxs | 4 | 47 | 56 | 0.4307 |
| nnskd_mobilevit_xxs_banlgf | 0 | 51 | 64 | 0.2631 |
| nnskd_mobilevit_xxs_banlgf | 1 | 45 | 45 | 1 |
| nnskd_mobilevit_xxs_banlgf | 2 | 41 | 39 | 0.9111 |
| nnskd_mobilevit_xxs_banlgf | 3 | 37 | 41 | 0.7343 |
| nnskd_mobilevit_xxs_banlgf | 4 | 42 | 41 | 1 |
| nnskd_mobilevit_xxs_ema | 0 | 64 | 53 | 0.3553 |
| nnskd_mobilevit_xxs_ema | 1 | 47 | 51 | 0.762 |
| nnskd_mobilevit_xxs_ema | 2 | 34 | 45 | 0.2604 |
| nnskd_mobilevit_xxs_ema | 3 | 57 | 44 | 0.2323 |
| nnskd_mobilevit_xxs_ema | 4 | 42 | 47 | 0.6718 |
| nnskd_mobilevit_xxs_emaonly | 0 | 58 | 48 | 0.3821 |
| nnskd_mobilevit_xxs_emaonly | 1 | 59 | 56 | 0.8522 |
| nnskd_mobilevit_xxs_emaonly | 2 | 35 | 52 | 0.08569 |
| nnskd_mobilevit_xxs_emaonly | 3 | 49 | 49 | 1 |
| nnskd_mobilevit_xxs_emaonly | 4 | 63 | 54 | 0.4597 |
| nnskd_mobilevit_xxs_gen2 | 0 | 49 | 63 | 0.2191 |
| nnskd_mobilevit_xxs_gen2 | 1 | 42 | 47 | 0.6718 |
| nnskd_mobilevit_xxs_gen2 | 2 | 53 | 49 | 0.7666 |
| nnskd_mobilevit_xxs_gen2 | 3 | 42 | 47 | 0.6718 |
| nnskd_mobilevit_xxs_gen2 | 4 | 48 | 41 | 0.525 |
| nnskd_mobilevit_xxs_v2 | 0 | 47 | 64 | 0.1285 |
| nnskd_mobilevit_xxs_v2 | 1 | 54 | 41 | 0.2181 |
| nnskd_mobilevit_xxs_v2 | 2 | 41 | 46 | 0.6683 |
| nnskd_mobilevit_xxs_v2 | 3 | 45 | 42 | 0.8304 |
| nnskd_mobilevit_xxs_v2 | 4 | 45 | 50 | 0.6817 |
| nnskd_mobilevit_xxs_v3 | 0 | 50 | 59 | 0.4437 |
| nnskd_mobilevit_xxs_v3 | 1 | 42 | 33 | 0.3557 |
| nnskd_mobilevit_xxs_v3 | 2 | 36 | 47 | 0.2723 |
| nnskd_mobilevit_xxs_v3 | 3 | 43 | 56 | 0.2276 |
| nnskd_mobilevit_xxs_v3 | 4 | 52 | 40 | 0.2513 |
| pattlite | 0 | 51 | 52 | 1 |
| pattlite | 1 | 62 | 42 | 0.06193 |
| pattlite | 2 | 59 | 43 | 0.1371 |
| pattlite | 3 | 47 | 64 | 0.1285 |
| pattlite | 4 | 77 | 55 | 0.06717 |
| resnet18 | 0 | 56 | 62 | 0.6455 |
| resnet18 | 1 | 61 | 56 | 0.7117 |
| resnet18 | 2 | 37 | 66 | 0.005536 |
| resnet18 | 3 | 46 | 47 | 1 |
| resnet18 | 4 | 50 | 52 | 0.9212 |
