# rafdb: nnskd_mobilevit_xxs_banlgf vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.93 | 0.0035 | 0.0566 | 0.0625 | 2.75 |
| microexpnet | 5 | +15.51 | 0.0000 | 0.0002 | 0.0625 | 12.23 |
| mobilevit_xxs | 5 | +0.81 | 0.1601 | 1.0000 | 0.1875 | 0.77 |
| mobilevit_xxs_ban | 5 | +0.33 | 0.2734 | 1.0000 | 0.3125 | 0.57 |
| mobilevit_xxs_recipe | 5 | +2.15 | 0.0220 | 0.3074 | 0.0625 | 1.63 |
| nnskd_mobilevit_xxs | 5 | -0.04 | 0.9142 | 1.0000 | 1.0000 | -0.05 |
| nnskd_mobilevit_xxs_aux | 5 | +0.19 | 0.5933 | 1.0000 | 0.6250 | 0.26 |
| nnskd_mobilevit_xxs_ema | 5 | +1.34 | 0.0247 | 0.3210 | 0.1250 | 1.57 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.22 | 0.5062 | 1.0000 | 0.6250 | 0.33 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.01 | 0.9871 | 1.0000 | 1.0000 | -0.01 |
| nnskd_mobilevit_xxs_kd | 5 | +0.16 | 0.7541 | 1.0000 | 0.7150 | 0.15 |
| nnskd_mobilevit_xxs_nm | 5 | +1.11 | 0.0682 | 0.8183 | 0.1250 | 1.11 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.00 | 1.0000 | 1.0000 | 1.0000 | 0.00 |
| nnskd_mobilevit_xxs_v2 | 5 | +1.95 | 0.0100 | 0.1496 | 0.0625 | 2.06 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.07 | 0.8879 | 1.0000 | 1.0000 | -0.07 |
| pattlite | 5 | +0.84 | 0.1262 | 1.0000 | 0.1250 | 0.86 |
| resnet18 | 5 | +0.72 | 0.2392 | 1.0000 | 0.3125 | 0.62 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +5.58 | 0.0034 | 0.0542 | 0.0625 | 2.78 |
| microexpnet | 5 | +28.46 | 0.0001 | 0.0015 | 0.0625 | 7.18 |
| mobilevit_xxs | 5 | +1.67 | 0.0463 | 0.5559 | 0.0625 | 1.28 |
| mobilevit_xxs_ban | 5 | +0.72 | 0.1041 | 1.0000 | 0.1250 | 0.94 |
| mobilevit_xxs_recipe | 5 | +3.17 | 0.0234 | 0.3047 | 0.0625 | 1.60 |
| nnskd_mobilevit_xxs | 5 | -0.12 | 0.8741 | 1.0000 | 1.0000 | -0.08 |
| nnskd_mobilevit_xxs_aux | 5 | +0.58 | 0.5136 | 1.0000 | 0.6250 | 0.32 |
| nnskd_mobilevit_xxs_ema | 5 | +2.07 | 0.0151 | 0.2259 | 0.0625 | 1.83 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.26 | 0.6740 | 1.0000 | 0.8125 | 0.20 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.19 | 0.7999 | 1.0000 | 1.0000 | -0.12 |
| nnskd_mobilevit_xxs_kd | 5 | +0.10 | 0.9064 | 1.0000 | 0.8125 | 0.06 |
| nnskd_mobilevit_xxs_nm | 5 | +1.88 | 0.1256 | 1.0000 | 0.1875 | 0.86 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.03 | 0.9594 | 1.0000 | 1.0000 | -0.02 |
| nnskd_mobilevit_xxs_v2 | 5 | +2.78 | 0.0174 | 0.2440 | 0.0625 | 1.75 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.26 | 0.7767 | 1.0000 | 1.0000 | -0.14 |
| pattlite | 5 | +1.75 | 0.0708 | 0.7790 | 0.0625 | 1.09 |
| resnet18 | 5 | +1.53 | 0.1119 | 1.0000 | 0.1875 | 0.91 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +7.18 | 0.0031 | 0.0493 | 0.0625 | 2.86 |
| microexpnet | 5 | +40.09 | 0.0002 | 0.0028 | 0.0625 | 6.10 |
| mobilevit_xxs | 5 | +2.29 | 0.0342 | 0.4099 | 0.0625 | 1.41 |
| mobilevit_xxs_ban | 5 | +1.03 | 0.1142 | 1.0000 | 0.1250 | 0.90 |
| mobilevit_xxs_recipe | 5 | +4.65 | 0.0263 | 0.3425 | 0.1250 | 1.54 |
| nnskd_mobilevit_xxs | 5 | -0.28 | 0.8028 | 1.0000 | 1.0000 | -0.12 |
| nnskd_mobilevit_xxs_aux | 5 | +1.13 | 0.4051 | 1.0000 | 0.6250 | 0.42 |
| nnskd_mobilevit_xxs_ema | 5 | +3.07 | 0.0115 | 0.1718 | 0.0625 | 1.98 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.39 | 0.6919 | 1.0000 | 0.6250 | 0.19 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.45 | 0.7040 | 1.0000 | 1.0000 | -0.18 |
| nnskd_mobilevit_xxs_kd | 5 | -0.00 | 0.9998 | 1.0000 | 0.8125 | -0.00 |
| nnskd_mobilevit_xxs_nm | 5 | +2.54 | 0.1530 | 1.0000 | 0.1875 | 0.79 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.02 | 0.9874 | 1.0000 | 1.0000 | -0.01 |
| nnskd_mobilevit_xxs_v2 | 5 | +4.16 | 0.0190 | 0.2664 | 0.0625 | 1.70 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.48 | 0.7282 | 1.0000 | 0.6250 | -0.17 |
| pattlite | 5 | +2.64 | 0.0363 | 0.4099 | 0.0625 | 1.39 |
| resnet18 | 5 | +2.22 | 0.0975 | 0.9747 | 0.1875 | 0.96 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.30 | 0.0197 | 0.2951 | 0.0625 | 1.68 |
| microexpnet | 5 | +8.67 | 0.0005 | 0.0081 | 0.0625 | 4.67 |
| mobilevit_xxs | 5 | -0.61 | 0.0734 | 1.0000 | 0.0625 | -1.08 |
| mobilevit_xxs_ban | 5 | -0.25 | 0.6624 | 1.0000 | 0.6250 | -0.21 |
| mobilevit_xxs_recipe | 5 | -0.74 | 0.4592 | 1.0000 | 0.6250 | -0.37 |
| nnskd_mobilevit_xxs | 5 | -0.71 | 0.1582 | 1.0000 | 0.1875 | -0.77 |
| nnskd_mobilevit_xxs_aux | 5 | -0.65 | 0.1815 | 1.0000 | 0.1875 | -0.72 |
| nnskd_mobilevit_xxs_ema | 5 | -0.02 | 0.9797 | 1.0000 | 1.0000 | -0.01 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.75 | 0.0767 | 1.0000 | 0.1250 | -1.06 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.64 | 0.2122 | 1.0000 | 0.3125 | -0.66 |
| nnskd_mobilevit_xxs_kd | 5 | -0.28 | 0.6483 | 1.0000 | 0.6250 | -0.22 |
| nnskd_mobilevit_xxs_nm | 5 | -1.16 | 0.0925 | 1.0000 | 0.1250 | -0.98 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.66 | 0.1824 | 1.0000 | 0.1875 | -0.72 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.59 | 0.4040 | 1.0000 | 0.4375 | -0.42 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.95 | 0.0143 | 0.2289 | 0.0625 | -1.85 |
| pattlite | 5 | -0.01 | 0.9842 | 1.0000 | 1.0000 | -0.01 |
| resnet18 | 5 | +0.18 | 0.5407 | 1.0000 | 0.6250 | 0.30 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.62 | 0.1340 | 0.6147 | 0.1875 | 0.84 |
| microexpnet | 5 | +7.88 | 0.0055 | 0.0928 | 0.0625 | 2.44 |
| mobilevit_xxs | 5 | +3.82 | 0.0234 | 0.3278 | 0.0625 | 1.60 |
| mobilevit_xxs_ban | 5 | +2.24 | 0.0311 | 0.3730 | 0.0625 | 1.46 |
| mobilevit_xxs_recipe | 5 | +5.12 | 0.1023 | 0.6147 | 0.1250 | 0.94 |
| nnskd_mobilevit_xxs | 5 | +2.85 | 0.0538 | 0.5385 | 0.1250 | 1.21 |
| nnskd_mobilevit_xxs_aux | 5 | +2.32 | 0.0458 | 0.5033 | 0.0625 | 1.28 |
| nnskd_mobilevit_xxs_ema | 5 | +1.74 | 0.1580 | 0.6147 | 0.1250 | 0.78 |
| nnskd_mobilevit_xxs_emaonly | 5 | +3.62 | 0.0089 | 0.1420 | 0.0625 | 2.13 |
| nnskd_mobilevit_xxs_gen2 | 5 | +2.15 | 0.0690 | 0.6147 | 0.1250 | 1.10 |
| nnskd_mobilevit_xxs_kd | 5 | +1.59 | 0.2098 | 0.6147 | 0.2733 | 0.67 |
| nnskd_mobilevit_xxs_nm | 5 | +6.38 | 0.0251 | 0.3278 | 0.0625 | 1.56 |
| nnskd_mobilevit_xxs_tinf | 5 | +2.74 | 0.0711 | 0.6147 | 0.1250 | 1.09 |
| nnskd_mobilevit_xxs_v2 | 5 | +3.00 | 0.0934 | 0.6147 | 0.1250 | 0.98 |
| nnskd_mobilevit_xxs_v3 | 5 | +3.03 | 0.0188 | 0.2813 | 0.0625 | 1.71 |
| pattlite | 5 | +2.65 | 0.0902 | 0.6147 | 0.1875 | 0.99 |
| resnet18 | 5 | +2.06 | 0.0683 | 0.6147 | 0.1250 | 1.11 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +5.20 | 0.0009 | 0.0151 | 0.0625 | 3.91 |
| microexpnet | 5 | +15.04 | 0.0001 | 0.0011 | 0.0625 | 7.73 |
| mobilevit_xxs | 5 | +1.36 | 0.2096 | 1.0000 | 0.3125 | 0.67 |
| mobilevit_xxs_ban | 5 | +0.92 | 0.2413 | 1.0000 | 0.3125 | 0.61 |
| mobilevit_xxs_recipe | 5 | +1.97 | 0.0705 | 0.9166 | 0.1250 | 1.10 |
| nnskd_mobilevit_xxs | 5 | +0.64 | 0.1068 | 0.9616 | 0.1250 | 0.93 |
| nnskd_mobilevit_xxs_aux | 5 | +0.42 | 0.6207 | 1.0000 | 0.4375 | 0.24 |
| nnskd_mobilevit_xxs_ema | 5 | +0.97 | 0.2245 | 1.0000 | 0.3125 | 0.64 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.03 | 0.0481 | 0.6738 | 0.1250 | 1.26 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.34 | 0.1986 | 1.0000 | 0.3125 | 0.69 |
| nnskd_mobilevit_xxs_kd | 5 | +0.52 | 0.2728 | 1.0000 | 0.3125 | 0.57 |
| nnskd_mobilevit_xxs_nm | 5 | +2.09 | 0.0427 | 0.6405 | 0.0625 | 1.31 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.64 | 0.0884 | 0.9616 | 0.1250 | 1.00 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.92 | 0.0954 | 0.9616 | 0.1875 | 0.97 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.40 | 0.5439 | 1.0000 | 0.6250 | 0.30 |
| pattlite | 5 | +1.52 | 0.0834 | 0.9616 | 0.1250 | 1.03 |
| resnet18 | 5 | +1.43 | 0.0801 | 0.9616 | 0.1250 | 1.04 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.02 | 0.0041 | 0.0536 | 0.0625 | -2.64 |
| microexpnet | 5 | +0.10 | 0.0000 | 0.0006 | 0.0625 | 8.79 |
| mobilevit_xxs | 5 | -0.01 | 0.0246 | 0.2956 | 0.0625 | -1.57 |
| mobilevit_xxs_ban | 5 | -0.01 | 0.0587 | 0.5872 | 0.1250 | -1.17 |
| mobilevit_xxs_recipe | 5 | +0.14 | 0.0001 | 0.0018 | 0.0625 | 6.65 |
| nnskd_mobilevit_xxs | 5 | -0.00 | 0.4517 | 1.0000 | 0.6250 | -0.37 |
| nnskd_mobilevit_xxs_aux | 5 | -0.00 | 0.1055 | 0.8438 | 0.3125 | -0.93 |
| nnskd_mobilevit_xxs_ema | 5 | +0.15 | 0.0000 | 0.0002 | 0.0625 | 11.75 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.01 | 0.0285 | 0.3136 | 0.0625 | -1.50 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.00 | 0.1504 | 1.0000 | 0.1875 | 0.79 |
| nnskd_mobilevit_xxs_kd | 5 | +0.00 | 0.5601 | 1.0000 | 0.6250 | 0.28 |
| nnskd_mobilevit_xxs_nm | 5 | +0.00 | 0.8247 | 1.0000 | 1.0000 | 0.11 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.00 | 0.4657 | 1.0000 | 0.6250 | -0.36 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.16 | 0.0002 | 0.0022 | 0.0625 | 6.21 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.00 | 0.8989 | 1.0000 | 0.8125 | 0.06 |
| pattlite | 5 | -0.00 | 0.3757 | 1.0000 | 0.6250 | -0.45 |
| resnet18 | 5 | -0.01 | 0.0859 | 0.7727 | 0.1250 | -1.01 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.14 | 0.1253 | 1.0000 | 0.1875 | 0.86 |
| microexpnet | 5 | +24.21 | 0.0000 | 0.0000 | 0.0625 | 17.25 |
| mobilevit_xxs | 5 | -1.06 | 0.0972 | 1.0000 | 0.1875 | -0.96 |
| mobilevit_xxs_ban | 5 | +0.19 | 0.6927 | 1.0000 | 0.7150 | 0.19 |
| mobilevit_xxs_recipe | 5 | -1.27 | 0.5193 | 1.0000 | 0.6250 | -0.32 |
| nnskd_mobilevit_xxs | 5 | +0.86 | 0.5424 | 1.0000 | 0.8125 | 0.30 |
| nnskd_mobilevit_xxs_aux | 5 | -0.84 | 0.3198 | 1.0000 | 0.3125 | -0.51 |
| nnskd_mobilevit_xxs_ema | 5 | -1.45 | 0.0616 | 0.9854 | 0.1250 | -1.15 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.49 | 0.2174 | 1.0000 | 0.3125 | -0.65 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.58 | 0.5566 | 1.0000 | 0.6250 | 0.29 |
| nnskd_mobilevit_xxs_kd | 5 | +0.24 | 0.8399 | 1.0000 | 0.8125 | 0.10 |
| nnskd_mobilevit_xxs_nm | 5 | +0.71 | 0.5441 | 1.0000 | 0.8125 | 0.30 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.97 | 0.5517 | 1.0000 | 0.8125 | 0.29 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.71 | 0.3749 | 1.0000 | 0.4375 | -0.45 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.55 | 0.1914 | 1.0000 | 0.1875 | -0.70 |
| pattlite | 5 | -0.09 | 0.9497 | 1.0000 | 0.8125 | -0.03 |
| resnet18 | 5 | +0.73 | 0.5161 | 1.0000 | 0.4652 | 0.32 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.62 | 0.0154 | 0.2163 | 0.0625 | 1.81 |
| microexpnet | 5 | +26.03 | 0.0000 | 0.0001 | 0.0625 | 15.96 |
| mobilevit_xxs | 5 | +0.56 | 0.2186 | 1.0000 | 0.1875 | 0.65 |
| mobilevit_xxs_ban | 5 | +1.98 | 0.0290 | 0.3770 | 0.0625 | 1.49 |
| mobilevit_xxs_recipe | 5 | -2.99 | 0.1052 | 1.0000 | 0.1250 | -0.93 |
| nnskd_mobilevit_xxs | 5 | +0.46 | 0.6500 | 1.0000 | 0.8125 | 0.22 |
| nnskd_mobilevit_xxs_aux | 5 | -0.03 | 0.9728 | 1.0000 | 1.0000 | -0.02 |
| nnskd_mobilevit_xxs_ema | 5 | -1.36 | 0.0931 | 1.0000 | 0.1250 | -0.98 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.40 | 0.7311 | 1.0000 | 0.8125 | 0.16 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.63 | 0.4774 | 1.0000 | 0.8125 | 0.35 |
| nnskd_mobilevit_xxs_kd | 5 | +0.70 | 0.3059 | 1.0000 | 0.4375 | 0.52 |
| nnskd_mobilevit_xxs_nm | 5 | +0.91 | 0.4205 | 1.0000 | 0.8125 | 0.40 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.46 | 0.6998 | 1.0000 | 1.0000 | 0.19 |
| nnskd_mobilevit_xxs_v2 | 5 | -2.77 | 0.0115 | 0.1842 | 0.0625 | -1.98 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.05 | 0.2489 | 1.0000 | 0.3125 | -0.60 |
| pattlite | 5 | +0.19 | 0.8718 | 1.0000 | 1.0000 | 0.08 |
| resnet18 | 5 | +2.46 | 0.0126 | 0.1891 | 0.0625 | 1.92 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 282 | 183 | 5.093e-06 |
| efficientface | 1 | 314 | 153 | 7.533e-14 |
| efficientface | 2 | 245 | 191 | 0.01106 |
| efficientface | 3 | 297 | 151 | 4.796e-12 |
| efficientface | 4 | 291 | 148 | 8.064e-12 |
| microexpnet | 0 | 617 | 138 | 4.447e-73 |
| microexpnet | 1 | 593 | 122 | 4.302e-75 |
| microexpnet | 2 | 568 | 155 | 3.448e-56 |
| microexpnet | 3 | 637 | 131 | 1.413e-80 |
| microexpnet | 4 | 636 | 126 | 1.013e-82 |
| mobilevit_xxs | 0 | 200 | 172 | 0.1615 |
| mobilevit_xxs | 1 | 170 | 149 | 0.2628 |
| mobilevit_xxs | 2 | 149 | 160 | 0.5695 |
| mobilevit_xxs | 3 | 157 | 147 | 0.6058 |
| mobilevit_xxs | 4 | 196 | 120 | 2.254e-05 |
| mobilevit_xxs_ban | 0 | 190 | 170 | 0.3166 |
| mobilevit_xxs_ban | 1 | 156 | 155 | 1 |
| mobilevit_xxs_ban | 2 | 161 | 177 | 0.4146 |
| mobilevit_xxs_ban | 3 | 165 | 149 | 0.3973 |
| mobilevit_xxs_ban | 4 | 162 | 132 | 0.09061 |
| mobilevit_xxs_recipe | 0 | 202 | 159 | 0.02693 |
| mobilevit_xxs_recipe | 1 | 206 | 146 | 0.001625 |
| mobilevit_xxs_recipe | 2 | 186 | 172 | 0.4921 |
| mobilevit_xxs_recipe | 3 | 250 | 140 | 2.773e-08 |
| mobilevit_xxs_recipe | 4 | 230 | 127 | 5.481e-08 |
| nnskd_mobilevit_xxs | 0 | 126 | 146 | 0.2493 |
| nnskd_mobilevit_xxs | 1 | 127 | 124 | 0.8996 |
| nnskd_mobilevit_xxs | 2 | 112 | 139 | 0.1006 |
| nnskd_mobilevit_xxs | 3 | 117 | 111 | 0.7406 |
| nnskd_mobilevit_xxs | 4 | 124 | 92 | 0.03468 |
| nnskd_mobilevit_xxs_aux | 0 | 166 | 144 | 0.2329 |
| nnskd_mobilevit_xxs_aux | 1 | 129 | 122 | 0.705 |
| nnskd_mobilevit_xxs_aux | 2 | 137 | 167 | 0.0961 |
| nnskd_mobilevit_xxs_aux | 3 | 140 | 137 | 0.9044 |
| nnskd_mobilevit_xxs_aux | 4 | 129 | 102 | 0.08692 |
| nnskd_mobilevit_xxs_ema | 0 | 207 | 170 | 0.06358 |
| nnskd_mobilevit_xxs_ema | 1 | 208 | 160 | 0.01417 |
| nnskd_mobilevit_xxs_ema | 2 | 170 | 171 | 1 |
| nnskd_mobilevit_xxs_ema | 3 | 185 | 132 | 0.003429 |
| nnskd_mobilevit_xxs_ema | 4 | 207 | 138 | 0.0002405 |
| nnskd_mobilevit_xxs_emaonly | 0 | 170 | 177 | 0.7474 |
| nnskd_mobilevit_xxs_emaonly | 1 | 170 | 157 | 0.507 |
| nnskd_mobilevit_xxs_emaonly | 2 | 145 | 165 | 0.2805 |
| nnskd_mobilevit_xxs_emaonly | 3 | 155 | 141 | 0.4499 |
| nnskd_mobilevit_xxs_emaonly | 4 | 168 | 134 | 0.05739 |
| nnskd_mobilevit_xxs_gen2 | 0 | 114 | 135 | 0.2049 |
| nnskd_mobilevit_xxs_gen2 | 1 | 132 | 109 | 0.1563 |
| nnskd_mobilevit_xxs_gen2 | 2 | 112 | 137 | 0.1281 |
| nnskd_mobilevit_xxs_gen2 | 3 | 93 | 103 | 0.5204 |
| nnskd_mobilevit_xxs_gen2 | 4 | 121 | 89 | 0.03217 |
| nnskd_mobilevit_xxs_kd | 0 | 128 | 154 | 0.1364 |
| nnskd_mobilevit_xxs_kd | 1 | 119 | 121 | 0.9486 |
| nnskd_mobilevit_xxs_kd | 2 | 134 | 134 | 1 |
| nnskd_mobilevit_xxs_kd | 3 | 120 | 127 | 0.7027 |
| nnskd_mobilevit_xxs_kd | 4 | 150 | 91 | 0.0001746 |
| nnskd_mobilevit_xxs_nm | 0 | 146 | 155 | 0.6448 |
| nnskd_mobilevit_xxs_nm | 1 | 201 | 137 | 0.0005905 |
| nnskd_mobilevit_xxs_nm | 2 | 144 | 131 | 0.4694 |
| nnskd_mobilevit_xxs_nm | 3 | 189 | 138 | 0.00561 |
| nnskd_mobilevit_xxs_nm | 4 | 171 | 119 | 0.002684 |
| nnskd_mobilevit_xxs_tinf | 0 | 128 | 146 | 0.3044 |
| nnskd_mobilevit_xxs_tinf | 1 | 125 | 123 | 0.9494 |
| nnskd_mobilevit_xxs_tinf | 2 | 119 | 138 | 0.2615 |
| nnskd_mobilevit_xxs_tinf | 3 | 117 | 114 | 0.8953 |
| nnskd_mobilevit_xxs_tinf | 4 | 123 | 91 | 0.03384 |
| nnskd_mobilevit_xxs_v2 | 0 | 185 | 142 | 0.02006 |
| nnskd_mobilevit_xxs_v2 | 1 | 199 | 127 | 7.91e-05 |
| nnskd_mobilevit_xxs_v2 | 2 | 193 | 163 | 0.1242 |
| nnskd_mobilevit_xxs_v2 | 3 | 184 | 134 | 0.005913 |
| nnskd_mobilevit_xxs_v2 | 4 | 208 | 104 | 3.986e-09 |
| nnskd_mobilevit_xxs_v3 | 0 | 137 | 142 | 0.8108 |
| nnskd_mobilevit_xxs_v3 | 1 | 149 | 110 | 0.01804 |
| nnskd_mobilevit_xxs_v3 | 2 | 112 | 164 | 0.002086 |
| nnskd_mobilevit_xxs_v3 | 3 | 113 | 114 | 1 |
| nnskd_mobilevit_xxs_v3 | 4 | 109 | 101 | 0.6292 |
| pattlite | 0 | 209 | 203 | 0.8055 |
| pattlite | 1 | 207 | 172 | 0.08059 |
| pattlite | 2 | 197 | 202 | 0.8413 |
| pattlite | 3 | 198 | 177 | 0.3017 |
| pattlite | 4 | 216 | 144 | 0.0001744 |
| resnet18 | 0 | 193 | 207 | 0.5157 |
| resnet18 | 1 | 217 | 171 | 0.02222 |
| resnet18 | 2 | 187 | 206 | 0.3639 |
| resnet18 | 3 | 209 | 168 | 0.03925 |
| resnet18 | 4 | 204 | 148 | 0.003316 |
