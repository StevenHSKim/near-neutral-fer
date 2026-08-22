# sfew: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | -0.73 | 0.5481 | 1.0000 | 0.6250 | -0.20 |
| microexpnet | 5 | +13.63 | 0.0006 | 0.0084 | 0.0625 | 4.31 |
| mobilevit_xxs | 10 | -0.07 | 0.9553 | 1.0000 | 0.9056 | -0.02 |
| mobilevit_xxs_ban | 5 | +0.97 | 0.6135 | 1.0000 | 0.6250 | 0.24 |
| mobilevit_xxs_recipe | 5 | +2.09 | 0.2756 | 1.0000 | 0.3125 | 0.56 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.29 | 0.8681 | 1.0000 | 1.0000 | 0.08 |
| nnskd_mobilevit_xxs_ema | 5 | +1.17 | 0.6803 | 1.0000 | 0.8125 | 0.20 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.22 | 0.6164 | 1.0000 | 0.4375 | 0.24 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.34 | 0.8708 | 1.0000 | 0.8125 | 0.08 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.44 | 0.7863 | 1.0000 | 0.8125 | 0.13 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.39 | 0.8103 | 1.0000 | 1.0000 | 0.11 |
| pattlite | 5 | +2.92 | 0.1012 | 1.0000 | 0.1250 | 0.95 |
| resnet18 | 5 | -0.63 | 0.7821 | 1.0000 | 1.0000 | -0.13 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | +0.12 | 0.9098 | 1.0000 | 0.9219 | 0.04 |
| microexpnet | 5 | +17.93 | 0.0004 | 0.0047 | 0.0625 | 5.01 |
| mobilevit_xxs | 10 | +0.02 | 0.9852 | 1.0000 | 0.7695 | 0.01 |
| mobilevit_xxs_ban | 5 | +0.83 | 0.6403 | 1.0000 | 0.6250 | 0.23 |
| mobilevit_xxs_recipe | 5 | +0.10 | 0.9607 | 1.0000 | 0.8125 | 0.02 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.64 | 0.7544 | 1.0000 | 0.8125 | 0.15 |
| nnskd_mobilevit_xxs_ema | 5 | +0.64 | 0.8033 | 1.0000 | 1.0000 | 0.12 |
| nnskd_mobilevit_xxs_emaonly | 5 | +2.37 | 0.3492 | 1.0000 | 0.4375 | 0.47 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.05 | 0.9700 | 1.0000 | 1.0000 | -0.02 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.96 | 0.5340 | 1.0000 | 0.6250 | -0.30 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.05 | 0.9738 | 1.0000 | 1.0000 | 0.02 |
| pattlite | 5 | +2.41 | 0.0622 | 0.7469 | 0.0625 | 1.15 |
| resnet18 | 5 | +0.71 | 0.7597 | 1.0000 | 1.0000 | 0.15 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | -0.17 | 0.8910 | 1.0000 | 0.6250 | -0.04 |
| microexpnet | 5 | +12.07 | 0.0008 | 0.0106 | 0.0625 | 4.06 |
| mobilevit_xxs | 10 | -0.24 | 0.8759 | 1.0000 | 0.6250 | -0.05 |
| mobilevit_xxs_ban | 5 | +1.84 | 0.1310 | 1.0000 | 0.3125 | 0.85 |
| mobilevit_xxs_recipe | 5 | +0.05 | 0.9747 | 1.0000 | 1.0000 | 0.02 |
| nnskd_mobilevit_xxs_banlgf | 5 | +1.94 | 0.1377 | 1.0000 | 0.1875 | 0.83 |
| nnskd_mobilevit_xxs_ema | 5 | +2.92 | 0.0656 | 0.7871 | 0.1250 | 1.13 |
| nnskd_mobilevit_xxs_emaonly | 5 | +3.92 | 0.1569 | 1.0000 | 0.1875 | 0.78 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.79 | 0.4964 | 1.0000 | 0.6250 | 0.33 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.09 | 0.9515 | 1.0000 | 1.0000 | 0.03 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.83 | 0.5703 | 1.0000 | 0.8125 | 0.28 |
| pattlite | 5 | +3.90 | 0.1007 | 1.0000 | 0.1875 | 0.95 |
| resnet18 | 5 | +2.19 | 0.1057 | 1.0000 | 0.1875 | 0.93 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | +3.65 | 0.0092 | 0.1200 | 0.0195 | 1.04 |
| microexpnet | 5 | -9.24 | 0.0095 | 0.1200 | 0.0625 | -2.09 |
| mobilevit_xxs | 10 | +0.67 | 0.7735 | 1.0000 | 1.0000 | 0.09 |
| mobilevit_xxs_ban | 5 | -2.67 | 0.5618 | 1.0000 | 0.4652 | -0.28 |
| mobilevit_xxs_recipe | 5 | -1.82 | 0.3062 | 1.0000 | 0.3125 | -0.52 |
| nnskd_mobilevit_xxs_banlgf | 5 | +1.28 | 0.6259 | 1.0000 | 0.6250 | 0.24 |
| nnskd_mobilevit_xxs_ema | 5 | +2.19 | 0.7013 | 1.0000 | 0.8125 | 0.18 |
| nnskd_mobilevit_xxs_emaonly | 5 | +6.50 | 0.3356 | 1.0000 | 0.2850 | 0.49 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.64 | 0.7239 | 1.0000 | 1.0000 | 0.17 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.12 | 0.9716 | 1.0000 | 1.0000 | -0.02 |
| nnskd_mobilevit_xxs_v3 | 5 | +2.19 | 0.4086 | 1.0000 | 0.4375 | 0.41 |
| pattlite | 5 | +2.74 | 0.1819 | 1.0000 | 0.3125 | 0.72 |
| resnet18 | 5 | +7.36 | 0.0533 | 0.5868 | 0.0625 | 1.21 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | -1.59 | 0.7350 | 1.0000 | 0.8590 | -0.11 |
| microexpnet | 5 | +41.95 | 0.0018 | 0.0230 | 0.0625 | 3.31 |
| mobilevit_xxs | 10 | +2.56 | 0.6435 | 1.0000 | 0.6953 | 0.15 |
| mobilevit_xxs_ban | 5 | +8.05 | 0.4685 | 1.0000 | 0.6250 | 0.36 |
| mobilevit_xxs_recipe | 5 | +10.49 | 0.0461 | 0.5527 | 0.1250 | 1.28 |
| nnskd_mobilevit_xxs_banlgf | 5 | +1.71 | 0.7374 | 1.0000 | 0.8125 | 0.16 |
| nnskd_mobilevit_xxs_ema | 5 | +0.00 | 1.0000 | 1.0000 | 1.0000 | 0.00 |
| nnskd_mobilevit_xxs_emaonly | 5 | -3.66 | 0.7384 | 1.0000 | 1.0000 | -0.16 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.49 | 0.9581 | 1.0000 | 1.0000 | 0.03 |
| nnskd_mobilevit_xxs_v2 | 5 | +4.39 | 0.6076 | 1.0000 | 0.5930 | 0.25 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.24 | 0.9623 | 1.0000 | 1.0000 | -0.02 |
| pattlite | 5 | +9.27 | 0.2562 | 1.0000 | 0.3125 | 0.59 |
| resnet18 | 5 | -7.07 | 0.4843 | 1.0000 | 0.6250 | -0.34 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | +1.83 | 0.5485 | 1.0000 | 0.5566 | 0.20 |
| microexpnet | 5 | +36.66 | 0.0017 | 0.0225 | 0.0625 | 3.33 |
| mobilevit_xxs | 10 | +2.25 | 0.4374 | 1.0000 | 0.4316 | 0.26 |
| mobilevit_xxs_ban | 5 | +4.51 | 0.4379 | 1.0000 | 0.6250 | 0.38 |
| mobilevit_xxs_recipe | 5 | +6.24 | 0.0277 | 0.3322 | 0.1250 | 1.51 |
| nnskd_mobilevit_xxs_banlgf | 5 | +2.14 | 0.4093 | 1.0000 | 0.4375 | 0.41 |
| nnskd_mobilevit_xxs_ema | 5 | +2.83 | 0.6239 | 1.0000 | 0.8125 | 0.24 |
| nnskd_mobilevit_xxs_emaonly | 5 | +2.57 | 0.6234 | 1.0000 | 0.6250 | 0.24 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.87 | 0.5966 | 1.0000 | 0.4375 | 0.26 |
| nnskd_mobilevit_xxs_v2 | 5 | +2.98 | 0.4288 | 1.0000 | 0.3125 | 0.39 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.05 | 0.7756 | 1.0000 | 0.6250 | 0.14 |
| pattlite | 5 | +9.10 | 0.1159 | 1.0000 | 0.1875 | 0.90 |
| resnet18 | 5 | +1.32 | 0.7818 | 1.0000 | 0.8125 | 0.13 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | -0.12 | 0.0000 | 0.0002 | 0.0020 | -2.64 |
| microexpnet | 5 | -0.32 | 0.0001 | 0.0013 | 0.0625 | -6.85 |
| mobilevit_xxs | 10 | -0.02 | 0.0267 | 0.1600 | 0.0195 | -0.84 |
| mobilevit_xxs_ban | 5 | -0.03 | 0.1143 | 0.5714 | 0.1875 | -0.90 |
| mobilevit_xxs_recipe | 5 | -0.11 | 0.0068 | 0.0475 | 0.0625 | -2.30 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.00 | 0.7704 | 1.0000 | 1.0000 | -0.14 |
| nnskd_mobilevit_xxs_ema | 5 | -0.14 | 0.0043 | 0.0342 | 0.0625 | -2.61 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.08 | 0.1592 | 0.6368 | 0.1875 | -0.77 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.01 | 0.5967 | 1.0000 | 0.8125 | -0.26 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.12 | 0.0003 | 0.0028 | 0.0625 | -5.48 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.00 | 0.8505 | 1.0000 | 1.0000 | -0.09 |
| pattlite | 5 | -0.13 | 0.0014 | 0.0140 | 0.0625 | -3.53 |
| resnet18 | 5 | -0.14 | 0.0030 | 0.0274 | 0.0625 | -2.87 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | +3.26 | 0.3619 | 1.0000 | 0.4316 | 0.30 |
| microexpnet | 5 | +2.89 | 0.4511 | 1.0000 | 0.8125 | 0.37 |
| mobilevit_xxs | 10 | +1.04 | 0.8178 | 1.0000 | 0.8457 | 0.08 |
| mobilevit_xxs_ban | 5 | -1.53 | 0.8309 | 1.0000 | 1.0000 | -0.10 |
| mobilevit_xxs_recipe | 5 | -0.78 | 0.9072 | 1.0000 | 1.0000 | -0.06 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.91 | 0.7955 | 1.0000 | 1.0000 | 0.12 |
| nnskd_mobilevit_xxs_ema | 5 | -0.37 | 0.9219 | 1.0000 | 0.6250 | -0.05 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.83 | 0.5744 | 1.0000 | 0.8125 | 0.27 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.38 | 0.7816 | 1.0000 | 1.0000 | -0.13 |
| nnskd_mobilevit_xxs_v2 | 5 | -2.01 | 0.5664 | 1.0000 | 0.8125 | -0.28 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.32 | 0.9469 | 1.0000 | 1.0000 | -0.03 |
| pattlite | 5 | +5.44 | 0.3606 | 1.0000 | 0.4375 | 0.46 |
| resnet18 | 5 | -8.33 | 0.0062 | 0.0806 | 0.0625 | -2.36 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 10 | +3.85 | 0.1031 | 1.0000 | 0.1055 | 0.57 |
| microexpnet | 5 | +7.70 | 0.0235 | 0.3050 | 0.0625 | 1.59 |
| mobilevit_xxs | 10 | +2.47 | 0.3752 | 1.0000 | 0.3750 | 0.30 |
| mobilevit_xxs_ban | 5 | +2.03 | 0.6746 | 1.0000 | 0.8125 | 0.20 |
| mobilevit_xxs_recipe | 5 | +1.65 | 0.6820 | 1.0000 | 0.8125 | 0.20 |
| nnskd_mobilevit_xxs_banlgf | 5 | +1.84 | 0.1915 | 1.0000 | 0.3125 | 0.70 |
| nnskd_mobilevit_xxs_ema | 5 | +0.94 | 0.6908 | 1.0000 | 0.6250 | 0.19 |
| nnskd_mobilevit_xxs_emaonly | 5 | +2.98 | 0.1342 | 1.0000 | 0.3125 | 0.84 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.46 | 0.8808 | 1.0000 | 1.0000 | 0.07 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.15 | 0.9512 | 1.0000 | 0.6250 | 0.03 |
| nnskd_mobilevit_xxs_v3 | 5 | +2.31 | 0.4880 | 1.0000 | 0.4375 | 0.34 |
| pattlite | 5 | +4.11 | 0.3177 | 1.0000 | 0.3125 | 0.51 |
| resnet18 | 5 | -2.86 | 0.2042 | 1.0000 | 0.1875 | -0.68 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 66 | 61 | 0.7228 |
| efficientface | 1 | 43 | 62 | 0.07849 |
| efficientface | 2 | 48 | 68 | 0.07726 |
| efficientface | 3 | 54 | 51 | 0.8454 |
| efficientface | 4 | 67 | 49 | 0.1141 |
| efficientface | 5 | 68 | 45 | 0.03802 |
| efficientface | 6 | 48 | 59 | 0.3337 |
| efficientface | 7 | 45 | 57 | 0.276 |
| efficientface | 8 | 66 | 67 | 1 |
| efficientface | 9 | 56 | 72 | 0.1847 |
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
| mobilevit_xxs | 5 | 62 | 44 | 0.09824 |
| mobilevit_xxs | 6 | 49 | 49 | 1 |
| mobilevit_xxs | 7 | 24 | 55 | 0.0006394 |
| mobilevit_xxs | 8 | 51 | 48 | 0.8408 |
| mobilevit_xxs | 9 | 44 | 58 | 0.1978 |
| mobilevit_xxs_ban | 0 | 61 | 51 | 0.3952 |
| mobilevit_xxs_ban | 1 | 36 | 58 | 0.02977 |
| mobilevit_xxs_ban | 2 | 42 | 41 | 1 |
| mobilevit_xxs_ban | 3 | 59 | 37 | 0.03155 |
| mobilevit_xxs_ban | 4 | 56 | 47 | 0.4307 |
| mobilevit_xxs_recipe | 0 | 54 | 40 | 0.1797 |
| mobilevit_xxs_recipe | 1 | 33 | 42 | 0.3557 |
| mobilevit_xxs_recipe | 2 | 42 | 48 | 0.5984 |
| mobilevit_xxs_recipe | 3 | 58 | 33 | 0.01146 |
| mobilevit_xxs_recipe | 4 | 61 | 42 | 0.07562 |
| nnskd_mobilevit_xxs_banlgf | 0 | 34 | 37 | 0.8126 |
| nnskd_mobilevit_xxs_banlgf | 1 | 23 | 45 | 0.01034 |
| nnskd_mobilevit_xxs_banlgf | 2 | 27 | 24 | 0.7798 |
| nnskd_mobilevit_xxs_banlgf | 3 | 42 | 24 | 0.03558 |
| nnskd_mobilevit_xxs_banlgf | 4 | 41 | 31 | 0.2888 |
| nnskd_mobilevit_xxs_ema | 0 | 61 | 40 | 0.04604 |
| nnskd_mobilevit_xxs_ema | 1 | 38 | 64 | 0.01292 |
| nnskd_mobilevit_xxs_ema | 2 | 41 | 51 | 0.3481 |
| nnskd_mobilevit_xxs_ema | 3 | 67 | 32 | 0.0005622 |
| nnskd_mobilevit_xxs_ema | 4 | 49 | 45 | 0.7572 |
| nnskd_mobilevit_xxs_emaonly | 0 | 63 | 43 | 0.06446 |
| nnskd_mobilevit_xxs_emaonly | 1 | 46 | 65 | 0.08709 |
| nnskd_mobilevit_xxs_emaonly | 2 | 32 | 48 | 0.09291 |
| nnskd_mobilevit_xxs_emaonly | 3 | 58 | 36 | 0.02977 |
| nnskd_mobilevit_xxs_emaonly | 4 | 74 | 56 | 0.1357 |
| nnskd_mobilevit_xxs_gen2 | 0 | 28 | 32 | 0.6989 |
| nnskd_mobilevit_xxs_gen2 | 1 | 32 | 59 | 0.006106 |
| nnskd_mobilevit_xxs_gen2 | 2 | 38 | 33 | 0.6353 |
| nnskd_mobilevit_xxs_gen2 | 3 | 48 | 31 | 0.07116 |
| nnskd_mobilevit_xxs_gen2 | 4 | 42 | 26 | 0.06812 |
| nnskd_mobilevit_xxs_v2 | 0 | 38 | 45 | 0.5104 |
| nnskd_mobilevit_xxs_v2 | 1 | 40 | 49 | 0.3966 |
| nnskd_mobilevit_xxs_v2 | 2 | 35 | 39 | 0.7275 |
| nnskd_mobilevit_xxs_v2 | 3 | 49 | 24 | 0.004626 |
| nnskd_mobilevit_xxs_v2 | 4 | 41 | 37 | 0.7343 |
| nnskd_mobilevit_xxs_v3 | 0 | 35 | 34 | 1 |
| nnskd_mobilevit_xxs_v3 | 1 | 26 | 39 | 0.136 |
| nnskd_mobilevit_xxs_v3 | 2 | 29 | 39 | 0.275 |
| nnskd_mobilevit_xxs_v3 | 3 | 35 | 26 | 0.3057 |
| nnskd_mobilevit_xxs_v3 | 4 | 51 | 30 | 0.02565 |
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
