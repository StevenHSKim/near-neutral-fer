# sfew: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.63 | 0.7419 | 1.0000 | 0.8125 | -0.16 |
| microexpnet | 5 | +13.63 | 0.0006 | 0.0032 | 0.0625 | 4.31 |
| mobilevit_xxs | 5 | +1.02 | 0.5573 | 1.0000 | 0.6250 | 0.29 |
| pattlite | 5 | +2.92 | 0.1012 | 0.4048 | 0.1250 | 0.95 |
| resnet18 | 5 | -0.63 | 0.7821 | 1.0000 | 1.0000 | -0.13 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.70 | 0.6031 | 1.0000 | 0.8125 | -0.25 |
| microexpnet | 5 | +17.93 | 0.0004 | 0.0018 | 0.0625 | 5.01 |
| mobilevit_xxs | 5 | +0.52 | 0.7012 | 1.0000 | 0.8125 | 0.18 |
| pattlite | 5 | +2.41 | 0.0622 | 0.2490 | 0.0625 | 1.15 |
| resnet18 | 5 | +0.71 | 0.7597 | 1.0000 | 1.0000 | 0.15 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.43 | 0.7852 | 0.7852 | 0.8125 | -0.13 |
| microexpnet | 5 | +12.07 | 0.0008 | 0.0041 | 0.0625 | 4.06 |
| mobilevit_xxs | 5 | +1.50 | 0.2196 | 0.4393 | 0.1875 | 0.65 |
| pattlite | 5 | +3.90 | 0.1007 | 0.4029 | 0.1875 | 0.95 |
| resnet18 | 5 | +2.19 | 0.1057 | 0.4029 | 0.1875 | 0.93 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.10 | 0.0939 | 0.2818 | 0.1875 | 0.98 |
| microexpnet | 5 | -9.24 | 0.0095 | 0.0474 | 0.0625 | -2.09 |
| mobilevit_xxs | 5 | +0.97 | 0.8385 | 0.8385 | 0.8125 | 0.10 |
| pattlite | 5 | +2.74 | 0.1819 | 0.3637 | 0.3125 | 0.72 |
| resnet18 | 5 | +7.36 | 0.0533 | 0.2134 | 0.0625 | 1.21 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.24 | 0.9736 | 1.0000 | 1.0000 | 0.02 |
| microexpnet | 5 | +41.95 | 0.0018 | 0.0089 | 0.0625 | 3.31 |
| mobilevit_xxs | 5 | +1.95 | 0.8124 | 1.0000 | 1.0000 | 0.11 |
| pattlite | 5 | +9.27 | 0.2562 | 1.0000 | 0.3125 | 0.59 |
| resnet18 | 5 | -7.07 | 0.4843 | 1.0000 | 0.6250 | -0.34 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.48 | 0.6530 | 1.0000 | 0.8125 | 0.22 |
| microexpnet | 5 | +36.66 | 0.0017 | 0.0086 | 0.0625 | 3.33 |
| mobilevit_xxs | 5 | +1.76 | 0.5929 | 1.0000 | 0.6250 | 0.26 |
| pattlite | 5 | +9.10 | 0.1159 | 0.4636 | 0.1875 | 0.90 |
| resnet18 | 5 | +1.32 | 0.7818 | 1.0000 | 0.8125 | 0.13 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.12 | 0.0072 | 0.0098 | 0.0625 | -2.26 |
| microexpnet | 5 | -0.32 | 0.0001 | 0.0005 | 0.0625 | -6.85 |
| mobilevit_xxs | 5 | -0.03 | 0.0049 | 0.0098 | 0.0625 | -2.52 |
| pattlite | 5 | -0.13 | 0.0014 | 0.0056 | 0.0625 | -3.53 |
| resnet18 | 5 | -0.14 | 0.0030 | 0.0091 | 0.0625 | -2.87 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.50 | 0.6132 | 1.0000 | 0.6250 | 0.24 |
| microexpnet | 5 | +2.89 | 0.4511 | 1.0000 | 0.8125 | 0.37 |
| mobilevit_xxs | 5 | -1.40 | 0.8548 | 1.0000 | 1.0000 | -0.09 |
| pattlite | 5 | +5.44 | 0.3606 | 1.0000 | 0.4375 | 0.46 |
| resnet18 | 5 | -8.33 | 0.0062 | 0.0310 | 0.0625 | -2.36 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.31 | 0.4576 | 0.9531 | 0.3125 | 0.37 |
| microexpnet | 5 | +7.70 | 0.0235 | 0.1173 | 0.0625 | 1.59 |
| mobilevit_xxs | 5 | +1.29 | 0.7958 | 0.9531 | 0.8125 | 0.12 |
| pattlite | 5 | +4.11 | 0.3177 | 0.9531 | 0.3125 | 0.51 |
| resnet18 | 5 | -2.86 | 0.2042 | 0.8166 | 0.1875 | -0.68 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 66 | 61 | 0.7228 |
| efficientface | 1 | 43 | 62 | 0.07849 |
| efficientface | 2 | 48 | 68 | 0.07726 |
| efficientface | 3 | 54 | 51 | 0.8454 |
| efficientface | 4 | 67 | 49 | 0.1141 |
| microexpnet | 0 | 112 | 37 | 5.794e-10 |
| microexpnet | 1 | 82 | 34 | 9.686e-06 |
| microexpnet | 2 | 83 | 35 | 1.164e-05 |
| microexpnet | 3 | 111 | 47 | 3.779e-07 |
| microexpnet | 4 | 100 | 55 | 0.0003756 |
| mobilevit_xxs | 0 | 53 | 44 | 0.4168 |
| mobilevit_xxs | 1 | 35 | 50 | 0.1284 |
| mobilevit_xxs | 2 | 47 | 33 | 0.1456 |
| mobilevit_xxs | 3 | 60 | 40 | 0.05689 |
| mobilevit_xxs | 4 | 54 | 61 | 0.576 |
| pattlite | 0 | 56 | 47 | 0.4307 |
| pattlite | 1 | 51 | 53 | 0.9219 |
| pattlite | 2 | 58 | 41 | 0.1074 |
| pattlite | 3 | 58 | 53 | 0.7044 |
| pattlite | 4 | 84 | 53 | 0.01011 |
| resnet18 | 0 | 57 | 53 | 0.775 |
| resnet18 | 1 | 57 | 74 | 0.1619 |
| resnet18 | 2 | 38 | 66 | 0.0078 |
| resnet18 | 3 | 56 | 35 | 0.03545 |
| resnet18 | 4 | 69 | 62 | 0.6003 |
