# rafdb: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.97 | 0.0007 | 0.0112 | 0.0625 | 4.16 |
| microexpnet | 5 | +15.55 | 0.0000 | 0.0000 | 0.0625 | 19.22 |
| mobilevit_xxs | 10 | +0.63 | 0.0042 | 0.0464 | 0.0039 | 1.20 |
| mobilevit_xxs_ban | 5 | +0.37 | 0.2118 | 1.0000 | 0.3125 | 0.66 |
| mobilevit_xxs_recipe | 5 | +2.19 | 0.0030 | 0.0389 | 0.0625 | 2.88 |
| nnskd_mobilevit_xxs_aux | 5 | +0.23 | 0.4747 | 1.0000 | 1.0000 | 0.35 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.04 | 0.9142 | 1.0000 | 1.0000 | 0.05 |
| nnskd_mobilevit_xxs_ema | 5 | +1.38 | 0.0012 | 0.0171 | 0.0625 | 3.65 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.26 | 0.0117 | 0.1166 | 0.0625 | 1.97 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.03 | 0.8699 | 1.0000 | 0.7150 | 0.08 |
| nnskd_mobilevit_xxs_kd | 5 | +0.20 | 0.5276 | 1.0000 | 0.8125 | 0.31 |
| nnskd_mobilevit_xxs_nm | 5 | +1.15 | 0.0167 | 0.1506 | 0.0625 | 1.77 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.04 | 0.5583 | 1.0000 | 0.7150 | 0.29 |
| nnskd_mobilevit_xxs_v2 | 5 | +1.99 | 0.0003 | 0.0040 | 0.0625 | 5.49 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.03 | 0.9363 | 1.0000 | 1.0000 | -0.04 |
| pattlite | 5 | +0.88 | 0.0032 | 0.0389 | 0.0625 | 2.83 |
| resnet18 | 5 | +0.76 | 0.0333 | 0.2661 | 0.0625 | 1.43 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +5.70 | 0.0002 | 0.0024 | 0.0625 | 6.25 |
| microexpnet | 5 | +28.58 | 0.0000 | 0.0006 | 0.0625 | 8.89 |
| mobilevit_xxs | 10 | +1.18 | 0.0118 | 0.1417 | 0.0195 | 0.99 |
| mobilevit_xxs_ban | 5 | +0.84 | 0.1659 | 1.0000 | 0.1875 | 0.76 |
| mobilevit_xxs_recipe | 5 | +3.28 | 0.0002 | 0.0024 | 0.0625 | 6.19 |
| nnskd_mobilevit_xxs_aux | 5 | +0.69 | 0.3529 | 1.0000 | 0.4375 | 0.47 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.12 | 0.8741 | 1.0000 | 1.0000 | 0.08 |
| nnskd_mobilevit_xxs_ema | 5 | +2.19 | 0.0039 | 0.0513 | 0.0625 | 2.67 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.38 | 0.2756 | 1.0000 | 0.3125 | 0.56 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.07 | 0.8884 | 1.0000 | 0.8125 | -0.07 |
| nnskd_mobilevit_xxs_kd | 5 | +0.22 | 0.7946 | 1.0000 | 0.8125 | 0.12 |
| nnskd_mobilevit_xxs_nm | 5 | +1.99 | 0.0403 | 0.4029 | 0.0625 | 1.34 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.08 | 0.5967 | 1.0000 | 0.8125 | 0.26 |
| nnskd_mobilevit_xxs_v2 | 5 | +2.90 | 0.0015 | 0.0209 | 0.0625 | 3.47 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.15 | 0.8167 | 1.0000 | 0.8125 | -0.11 |
| pattlite | 5 | +1.87 | 0.0443 | 0.4029 | 0.1250 | 1.29 |
| resnet18 | 5 | +1.64 | 0.0176 | 0.1936 | 0.0625 | 1.74 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +7.46 | 0.0001 | 0.0011 | 0.0625 | 7.77 |
| microexpnet | 5 | +40.37 | 0.0001 | 0.0013 | 0.0625 | 7.37 |
| mobilevit_xxs | 10 | +1.40 | 0.0593 | 0.5333 | 0.1055 | 0.68 |
| mobilevit_xxs_ban | 5 | +1.31 | 0.1804 | 1.0000 | 0.1875 | 0.72 |
| mobilevit_xxs_recipe | 5 | +4.93 | 0.0003 | 0.0046 | 0.0625 | 5.22 |
| nnskd_mobilevit_xxs_aux | 5 | +1.41 | 0.1992 | 1.0000 | 0.1250 | 0.69 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.28 | 0.8028 | 1.0000 | 1.0000 | 0.12 |
| nnskd_mobilevit_xxs_ema | 5 | +3.35 | 0.0075 | 0.0969 | 0.0625 | 2.24 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.67 | 0.3407 | 1.0000 | 0.4375 | 0.48 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.17 | 0.8406 | 1.0000 | 1.0000 | -0.10 |
| nnskd_mobilevit_xxs_kd | 5 | +0.28 | 0.8308 | 1.0000 | 0.8125 | 0.10 |
| nnskd_mobilevit_xxs_nm | 5 | +2.82 | 0.0513 | 0.5159 | 0.0625 | 1.23 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.26 | 0.2609 | 1.0000 | 0.3125 | 0.59 |
| nnskd_mobilevit_xxs_v2 | 5 | +4.44 | 0.0025 | 0.0351 | 0.0625 | 3.02 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.20 | 0.8348 | 1.0000 | 1.0000 | -0.10 |
| pattlite | 5 | +2.92 | 0.0469 | 0.5159 | 0.1250 | 1.27 |
| resnet18 | 5 | +2.50 | 0.0181 | 0.2167 | 0.0625 | 1.73 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.02 | 0.0329 | 0.5268 | 0.1250 | 1.43 |
| microexpnet | 5 | +9.38 | 0.0004 | 0.0061 | 0.0625 | 5.03 |
| mobilevit_xxs | 10 | -0.12 | 0.6813 | 1.0000 | 0.7695 | -0.13 |
| mobilevit_xxs_ban | 5 | +0.46 | 0.5968 | 1.0000 | 0.8125 | 0.26 |
| mobilevit_xxs_recipe | 5 | -0.03 | 0.9838 | 1.0000 | 0.8125 | -0.01 |
| nnskd_mobilevit_xxs_aux | 5 | +0.06 | 0.9341 | 1.0000 | 0.8125 | 0.04 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.71 | 0.1582 | 1.0000 | 0.1875 | 0.77 |
| nnskd_mobilevit_xxs_ema | 5 | +0.70 | 0.1375 | 1.0000 | 0.1875 | 0.83 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.03 | 0.9507 | 1.0000 | 0.8125 | -0.03 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.08 | 0.9062 | 1.0000 | 1.0000 | 0.06 |
| nnskd_mobilevit_xxs_kd | 5 | +0.44 | 0.4888 | 1.0000 | 0.8125 | 0.34 |
| nnskd_mobilevit_xxs_nm | 5 | -0.45 | 0.6185 | 1.0000 | 0.6250 | -0.24 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.05 | 0.3239 | 1.0000 | 0.2850 | 0.50 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.13 | 0.8253 | 1.0000 | 1.0000 | 0.11 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.24 | 0.5538 | 1.0000 | 0.8125 | -0.29 |
| pattlite | 5 | +0.70 | 0.3839 | 1.0000 | 0.4375 | 0.44 |
| resnet18 | 5 | +0.89 | 0.0925 | 1.0000 | 0.1250 | 0.98 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.76 | 0.7931 | 1.0000 | 1.0000 | 0.13 |
| microexpnet | 5 | +5.03 | 0.0329 | 0.5362 | 0.0625 | 1.43 |
| mobilevit_xxs | 10 | +1.97 | 0.0315 | 0.5362 | 0.0488 | 0.80 |
| mobilevit_xxs_ban | 5 | -0.62 | 0.7226 | 1.0000 | 0.6250 | -0.17 |
| mobilevit_xxs_recipe | 5 | +2.26 | 0.5335 | 1.0000 | 0.4652 | 0.30 |
| nnskd_mobilevit_xxs_aux | 5 | -0.53 | 0.7602 | 1.0000 | 0.8125 | -0.15 |
| nnskd_mobilevit_xxs_banlgf | 5 | -2.85 | 0.0538 | 0.8077 | 0.1250 | -1.21 |
| nnskd_mobilevit_xxs_ema | 5 | -1.12 | 0.1633 | 1.0000 | 0.1250 | -0.76 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.76 | 0.5300 | 1.0000 | 0.8125 | 0.31 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.71 | 0.6327 | 1.0000 | 0.8125 | -0.23 |
| nnskd_mobilevit_xxs_kd | 5 | -1.26 | 0.4249 | 1.0000 | 0.6250 | -0.40 |
| nnskd_mobilevit_xxs_nm | 5 | +3.53 | 0.1905 | 1.0000 | 0.1875 | 0.70 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.12 | 0.6213 | 1.0000 | 0.8125 | -0.24 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.15 | 0.9060 | 1.0000 | 1.0000 | 0.06 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.18 | 0.8558 | 1.0000 | 1.0000 | 0.09 |
| pattlite | 5 | -0.21 | 0.9104 | 1.0000 | 0.6250 | -0.05 |
| resnet18 | 5 | -0.79 | 0.5618 | 1.0000 | 0.6250 | -0.28 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +4.56 | 0.0003 | 0.0051 | 0.0625 | 5.18 |
| microexpnet | 5 | +14.41 | 0.0000 | 0.0003 | 0.0625 | 11.09 |
| mobilevit_xxs | 10 | +0.97 | 0.0409 | 0.6133 | 0.0645 | 0.75 |
| mobilevit_xxs_ban | 5 | +0.28 | 0.5995 | 1.0000 | 0.8125 | 0.25 |
| mobilevit_xxs_recipe | 5 | +1.33 | 0.1049 | 1.0000 | 0.1250 | 0.93 |
| nnskd_mobilevit_xxs_aux | 5 | -0.22 | 0.7252 | 1.0000 | 0.8125 | -0.17 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.64 | 0.1068 | 1.0000 | 0.1250 | -0.93 |
| nnskd_mobilevit_xxs_ema | 5 | +0.33 | 0.4550 | 1.0000 | 0.6250 | 0.37 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.39 | 0.2022 | 1.0000 | 0.1875 | 0.68 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.30 | 0.3741 | 1.0000 | 0.4375 | -0.45 |
| nnskd_mobilevit_xxs_kd | 5 | -0.12 | 0.8493 | 1.0000 | 0.8125 | -0.09 |
| nnskd_mobilevit_xxs_nm | 5 | +1.46 | 0.1177 | 1.0000 | 0.1250 | 0.89 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.01 | 0.9560 | 1.0000 | 1.0000 | 0.03 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.28 | 0.3746 | 1.0000 | 0.4375 | 0.45 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.23 | 0.5492 | 1.0000 | 0.6250 | -0.29 |
| pattlite | 5 | +0.88 | 0.1079 | 1.0000 | 0.1875 | 0.92 |
| resnet18 | 5 | +0.79 | 0.0794 | 1.0000 | 0.1250 | 1.05 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.02 | 0.0098 | 0.1174 | 0.0625 | -2.07 |
| microexpnet | 5 | +0.10 | 0.0000 | 0.0003 | 0.0625 | 10.90 |
| mobilevit_xxs | 10 | -0.01 | 0.0063 | 0.0823 | 0.0137 | -1.12 |
| mobilevit_xxs_ban | 5 | -0.00 | 0.2540 | 1.0000 | 0.3125 | -0.60 |
| mobilevit_xxs_recipe | 5 | +0.15 | 0.0001 | 0.0019 | 0.0625 | 6.47 |
| nnskd_mobilevit_xxs_aux | 5 | -0.00 | 0.5483 | 1.0000 | 0.8125 | -0.29 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.00 | 0.4517 | 1.0000 | 0.6250 | 0.37 |
| nnskd_mobilevit_xxs_ema | 5 | +0.16 | 0.0000 | 0.0000 | 0.0625 | 17.88 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.01 | 0.0225 | 0.2474 | 0.0625 | -1.62 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.00 | 0.2185 | 1.0000 | 0.3125 | 0.65 |
| nnskd_mobilevit_xxs_kd | 5 | +0.00 | 0.3066 | 1.0000 | 0.3125 | 0.52 |
| nnskd_mobilevit_xxs_nm | 5 | +0.00 | 0.4067 | 1.0000 | 0.4375 | 0.41 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.00 | 0.5566 | 1.0000 | 0.6250 | -0.29 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.16 | 0.0001 | 0.0019 | 0.0625 | 6.59 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.00 | 0.5076 | 1.0000 | 0.4375 | 0.33 |
| pattlite | 5 | -0.00 | 0.7244 | 1.0000 | 0.8125 | -0.17 |
| resnet18 | 5 | -0.01 | 0.1213 | 1.0000 | 0.1875 | -0.88 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.28 | 0.8760 | 1.0000 | 1.0000 | 0.07 |
| microexpnet | 5 | +23.34 | 0.0001 | 0.0012 | 0.0625 | 7.52 |
| mobilevit_xxs | 10 | -0.30 | 0.7218 | 1.0000 | 1.0000 | -0.12 |
| mobilevit_xxs_ban | 5 | -0.67 | 0.6948 | 1.0000 | 0.8125 | -0.19 |
| mobilevit_xxs_recipe | 5 | -2.14 | 0.4520 | 1.0000 | 0.6250 | -0.37 |
| nnskd_mobilevit_xxs_aux | 5 | -1.70 | 0.2991 | 1.0000 | 0.2733 | -0.53 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.86 | 0.5424 | 1.0000 | 0.8125 | -0.30 |
| nnskd_mobilevit_xxs_ema | 5 | -2.31 | 0.1772 | 1.0000 | 0.1250 | -0.73 |
| nnskd_mobilevit_xxs_emaonly | 5 | -2.35 | 0.1832 | 1.0000 | 0.1875 | -0.72 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.28 | 0.8685 | 1.0000 | 1.0000 | -0.08 |
| nnskd_mobilevit_xxs_kd | 5 | -0.63 | 0.7706 | 1.0000 | 1.0000 | -0.14 |
| nnskd_mobilevit_xxs_nm | 5 | -0.15 | 0.8982 | 1.0000 | 1.0000 | -0.06 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.11 | 0.6836 | 1.0000 | 0.8125 | 0.20 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.57 | 0.3594 | 1.0000 | 0.4375 | -0.46 |
| nnskd_mobilevit_xxs_v3 | 5 | -2.42 | 0.0920 | 1.0000 | 0.1250 | -0.99 |
| pattlite | 5 | -0.95 | 0.6307 | 1.0000 | 1.0000 | -0.23 |
| resnet18 | 5 | -0.13 | 0.9422 | 1.0000 | 0.8125 | -0.03 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.17 | 0.1000 | 1.0000 | 0.1875 | 0.95 |
| microexpnet | 5 | +25.57 | 0.0000 | 0.0004 | 0.0625 | 9.89 |
| mobilevit_xxs | 10 | +0.31 | 0.6921 | 1.0000 | 0.8457 | 0.13 |
| mobilevit_xxs_ban | 5 | +1.53 | 0.2235 | 1.0000 | 0.3125 | 0.64 |
| mobilevit_xxs_recipe | 5 | -3.44 | 0.2104 | 1.0000 | 0.3125 | -0.67 |
| nnskd_mobilevit_xxs_aux | 5 | -0.48 | 0.6935 | 1.0000 | 1.0000 | -0.19 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.46 | 0.6500 | 1.0000 | 0.8125 | -0.22 |
| nnskd_mobilevit_xxs_ema | 5 | -1.82 | 0.2096 | 1.0000 | 0.1875 | -0.67 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.05 | 0.9775 | 1.0000 | 1.0000 | -0.01 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.18 | 0.8994 | 1.0000 | 0.6250 | 0.06 |
| nnskd_mobilevit_xxs_kd | 5 | +0.25 | 0.7705 | 1.0000 | 0.8125 | 0.14 |
| nnskd_mobilevit_xxs_nm | 5 | +0.45 | 0.6676 | 1.0000 | 0.6250 | 0.21 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.00 | 0.9912 | 1.0000 | 1.0000 | 0.01 |
| nnskd_mobilevit_xxs_v2 | 5 | -3.22 | 0.1066 | 1.0000 | 0.1875 | -0.93 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.50 | 0.3133 | 1.0000 | 0.4375 | -0.52 |
| pattlite | 5 | -0.26 | 0.8953 | 1.0000 | 1.0000 | -0.06 |
| resnet18 | 5 | +2.00 | 0.1157 | 1.0000 | 0.1250 | 0.90 |

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
| mobilevit_xxs | 5 | 200 | 183 | 0.4136 |
| mobilevit_xxs | 6 | 158 | 154 | 0.8652 |
| mobilevit_xxs | 7 | 184 | 162 | 0.2589 |
| mobilevit_xxs | 8 | 185 | 163 | 0.2603 |
| mobilevit_xxs | 9 | 172 | 173 | 1 |
| mobilevit_xxs_ban | 0 | 207 | 167 | 0.04359 |
| mobilevit_xxs_ban | 1 | 155 | 157 | 0.9549 |
| mobilevit_xxs_ban | 2 | 178 | 167 | 0.5904 |
| mobilevit_xxs_ban | 3 | 179 | 169 | 0.6295 |
| mobilevit_xxs_ban | 4 | 169 | 171 | 0.9568 |
| mobilevit_xxs_recipe | 0 | 227 | 164 | 0.001681 |
| mobilevit_xxs_recipe | 1 | 210 | 153 | 0.003235 |
| mobilevit_xxs_recipe | 2 | 202 | 161 | 0.03563 |
| mobilevit_xxs_recipe | 3 | 266 | 162 | 5.667e-07 |
| mobilevit_xxs_recipe | 4 | 236 | 165 | 0.0004585 |
| nnskd_mobilevit_xxs_aux | 0 | 176 | 134 | 0.01973 |
| nnskd_mobilevit_xxs_aux | 1 | 130 | 126 | 0.8513 |
| nnskd_mobilevit_xxs_aux | 2 | 151 | 154 | 0.9089 |
| nnskd_mobilevit_xxs_aux | 3 | 140 | 143 | 0.9054 |
| nnskd_mobilevit_xxs_aux | 4 | 131 | 136 | 0.8067 |
| nnskd_mobilevit_xxs_banlgf | 0 | 146 | 126 | 0.2493 |
| nnskd_mobilevit_xxs_banlgf | 1 | 124 | 127 | 0.8996 |
| nnskd_mobilevit_xxs_banlgf | 2 | 139 | 112 | 0.1006 |
| nnskd_mobilevit_xxs_banlgf | 3 | 111 | 117 | 0.7406 |
| nnskd_mobilevit_xxs_banlgf | 4 | 92 | 124 | 0.03468 |
| nnskd_mobilevit_xxs_ema | 0 | 213 | 156 | 0.003498 |
| nnskd_mobilevit_xxs_ema | 1 | 212 | 167 | 0.02369 |
| nnskd_mobilevit_xxs_ema | 2 | 178 | 152 | 0.1687 |
| nnskd_mobilevit_xxs_ema | 3 | 202 | 155 | 0.01479 |
| nnskd_mobilevit_xxs_ema | 4 | 208 | 171 | 0.06429 |
| nnskd_mobilevit_xxs_emaonly | 0 | 171 | 158 | 0.5083 |
| nnskd_mobilevit_xxs_emaonly | 1 | 163 | 153 | 0.6127 |
| nnskd_mobilevit_xxs_emaonly | 2 | 170 | 163 | 0.7424 |
| nnskd_mobilevit_xxs_emaonly | 3 | 161 | 153 | 0.6929 |
| nnskd_mobilevit_xxs_emaonly | 4 | 165 | 163 | 0.956 |
| nnskd_mobilevit_xxs_gen2 | 0 | 116 | 117 | 1 |
| nnskd_mobilevit_xxs_gen2 | 1 | 111 | 91 | 0.1811 |
| nnskd_mobilevit_xxs_gen2 | 2 | 110 | 108 | 0.946 |
| nnskd_mobilevit_xxs_gen2 | 3 | 109 | 125 | 0.3268 |
| nnskd_mobilevit_xxs_gen2 | 4 | 128 | 128 | 1 |
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
| nnskd_mobilevit_xxs_v2 | 0 | 196 | 133 | 0.0006091 |
| nnskd_mobilevit_xxs_v2 | 1 | 193 | 124 | 0.0001265 |
| nnskd_mobilevit_xxs_v2 | 2 | 197 | 140 | 0.002237 |
| nnskd_mobilevit_xxs_v2 | 3 | 186 | 142 | 0.01745 |
| nnskd_mobilevit_xxs_v2 | 4 | 216 | 144 | 0.0001744 |
| nnskd_mobilevit_xxs_v3 | 0 | 134 | 119 | 0.3788 |
| nnskd_mobilevit_xxs_v3 | 1 | 135 | 99 | 0.02193 |
| nnskd_mobilevit_xxs_v3 | 2 | 98 | 123 | 0.1062 |
| nnskd_mobilevit_xxs_v3 | 3 | 110 | 117 | 0.6905 |
| nnskd_mobilevit_xxs_v3 | 4 | 95 | 119 | 0.1157 |
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
