# rafdb: mobilevit_xxs_ban vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.60 | 0.0026 | 0.0419 | 0.0625 | 2.99 |
| microexpnet | 5 | +15.18 | 0.0000 | 0.0000 | 0.0625 | 19.83 |
| mobilevit_xxs | 5 | +0.48 | 0.1753 | 1.0000 | 0.1875 | 0.74 |
| mobilevit_xxs_recipe | 5 | +1.82 | 0.0135 | 0.1761 | 0.0625 | 1.88 |
| nnskd_mobilevit_xxs | 5 | -0.37 | 0.2118 | 1.0000 | 0.3125 | -0.66 |
| nnskd_mobilevit_xxs_aux | 5 | -0.14 | 0.3312 | 1.0000 | 0.4375 | -0.49 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.33 | 0.2734 | 1.0000 | 0.1875 | -0.57 |
| nnskd_mobilevit_xxs_ema | 5 | +1.01 | 0.0082 | 0.1174 | 0.0625 | 2.18 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.11 | 0.6298 | 1.0000 | 0.8125 | -0.23 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.34 | 0.3949 | 1.0000 | 0.4375 | -0.43 |
| nnskd_mobilevit_xxs_kd | 5 | -0.18 | 0.7081 | 1.0000 | 0.8125 | -0.18 |
| nnskd_mobilevit_xxs_nm | 5 | +0.78 | 0.1841 | 1.0000 | 0.3125 | 0.72 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.33 | 0.2422 | 1.0000 | 0.3125 | -0.61 |
| nnskd_mobilevit_xxs_v2 | 5 | +1.62 | 0.0078 | 0.1174 | 0.0625 | 2.21 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.40 | 0.3935 | 1.0000 | 0.6250 | -0.43 |
| pattlite | 5 | +0.51 | 0.1978 | 1.0000 | 0.3125 | 0.69 |
| resnet18 | 5 | +0.38 | 0.4399 | 1.0000 | 0.6250 | 0.38 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +4.86 | 0.0021 | 0.0340 | 0.0625 | 3.16 |
| microexpnet | 5 | +27.74 | 0.0001 | 0.0012 | 0.0625 | 7.55 |
| mobilevit_xxs | 5 | +0.95 | 0.0195 | 0.2532 | 0.0625 | 1.69 |
| mobilevit_xxs_recipe | 5 | +2.44 | 0.0210 | 0.2532 | 0.0625 | 1.65 |
| nnskd_mobilevit_xxs | 5 | -0.84 | 0.1659 | 1.0000 | 0.1875 | -0.76 |
| nnskd_mobilevit_xxs_aux | 5 | -0.14 | 0.8222 | 1.0000 | 1.0000 | -0.11 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.72 | 0.1041 | 1.0000 | 0.1250 | -0.94 |
| nnskd_mobilevit_xxs_ema | 5 | +1.35 | 0.0159 | 0.2229 | 0.0625 | 1.80 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.46 | 0.1769 | 1.0000 | 0.3125 | -0.73 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.91 | 0.0675 | 0.7428 | 0.1250 | -1.11 |
| nnskd_mobilevit_xxs_kd | 5 | -0.62 | 0.3482 | 1.0000 | 0.4375 | -0.47 |
| nnskd_mobilevit_xxs_nm | 5 | +1.16 | 0.2103 | 1.0000 | 0.3125 | 0.67 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.75 | 0.1391 | 1.0000 | 0.1875 | -0.82 |
| nnskd_mobilevit_xxs_v2 | 5 | +2.06 | 0.0060 | 0.0903 | 0.0625 | 2.38 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.99 | 0.1850 | 1.0000 | 0.1875 | -0.72 |
| pattlite | 5 | +1.03 | 0.1124 | 1.0000 | 0.0625 | 0.91 |
| resnet18 | 5 | +0.81 | 0.1464 | 1.0000 | 0.3125 | 0.80 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +6.16 | 0.0017 | 0.0278 | 0.0625 | 3.33 |
| microexpnet | 5 | +39.07 | 0.0002 | 0.0029 | 0.0625 | 6.08 |
| mobilevit_xxs | 5 | +1.27 | 0.0081 | 0.1209 | 0.0625 | 2.19 |
| mobilevit_xxs_recipe | 5 | +3.62 | 0.0252 | 0.3026 | 0.0625 | 1.56 |
| nnskd_mobilevit_xxs | 5 | -1.31 | 0.1804 | 1.0000 | 0.1875 | -0.72 |
| nnskd_mobilevit_xxs_aux | 5 | +0.10 | 0.9254 | 1.0000 | 1.0000 | 0.04 |
| nnskd_mobilevit_xxs_banlgf | 5 | -1.03 | 0.1142 | 0.9132 | 0.1250 | -0.90 |
| nnskd_mobilevit_xxs_ema | 5 | +2.04 | 0.0226 | 0.2943 | 0.0625 | 1.61 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.63 | 0.2807 | 1.0000 | 0.3125 | -0.56 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.47 | 0.0756 | 0.8314 | 0.0625 | -1.07 |
| nnskd_mobilevit_xxs_kd | 5 | -1.03 | 0.2707 | 1.0000 | 0.3125 | -0.57 |
| nnskd_mobilevit_xxs_nm | 5 | +1.51 | 0.2415 | 1.0000 | 0.3125 | 0.61 |
| nnskd_mobilevit_xxs_tinf | 5 | -1.04 | 0.2077 | 1.0000 | 0.1875 | -0.67 |
| nnskd_mobilevit_xxs_v2 | 5 | +3.14 | 0.0092 | 0.1292 | 0.0625 | 2.11 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.51 | 0.1806 | 1.0000 | 0.1250 | -0.72 |
| pattlite | 5 | +1.61 | 0.0866 | 0.8660 | 0.1250 | 1.01 |
| resnet18 | 5 | +1.20 | 0.0973 | 0.8759 | 0.1875 | 0.96 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.55 | 0.0219 | 0.3499 | 0.0625 | 1.63 |
| microexpnet | 5 | +8.92 | 0.0002 | 0.0035 | 0.0625 | 5.77 |
| mobilevit_xxs | 5 | -0.36 | 0.3914 | 1.0000 | 0.3125 | -0.43 |
| mobilevit_xxs_recipe | 5 | -0.49 | 0.4595 | 1.0000 | 0.4375 | -0.37 |
| nnskd_mobilevit_xxs | 5 | -0.46 | 0.5968 | 1.0000 | 0.8125 | -0.26 |
| nnskd_mobilevit_xxs_aux | 5 | -0.40 | 0.0928 | 1.0000 | 0.1250 | -0.98 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.25 | 0.6624 | 1.0000 | 0.6250 | 0.21 |
| nnskd_mobilevit_xxs_ema | 5 | +0.23 | 0.7936 | 1.0000 | 1.0000 | 0.13 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.49 | 0.4009 | 1.0000 | 0.4375 | -0.42 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.39 | 0.4857 | 1.0000 | 0.4375 | -0.34 |
| nnskd_mobilevit_xxs_kd | 5 | -0.03 | 0.9673 | 1.0000 | 1.0000 | -0.02 |
| nnskd_mobilevit_xxs_nm | 5 | -0.91 | 0.2697 | 1.0000 | 0.4375 | -0.57 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.41 | 0.6322 | 1.0000 | 0.8125 | -0.23 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.34 | 0.6784 | 1.0000 | 0.6250 | -0.20 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.70 | 0.1951 | 1.0000 | 0.3125 | -0.70 |
| pattlite | 5 | +0.24 | 0.2103 | 1.0000 | 0.3125 | 0.67 |
| resnet18 | 5 | +0.43 | 0.4266 | 1.0000 | 0.6250 | 0.40 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.38 | 0.3889 | 1.0000 | 0.4375 | 0.43 |
| microexpnet | 5 | +5.65 | 0.0143 | 0.2426 | 0.0625 | 1.86 |
| mobilevit_xxs | 5 | +1.59 | 0.3160 | 1.0000 | 0.3125 | 0.51 |
| mobilevit_xxs_recipe | 5 | +2.88 | 0.2327 | 1.0000 | 0.3125 | 0.63 |
| nnskd_mobilevit_xxs | 5 | +0.62 | 0.7226 | 1.0000 | 0.6250 | 0.17 |
| nnskd_mobilevit_xxs_aux | 5 | +0.09 | 0.9185 | 1.0000 | 0.7150 | 0.05 |
| nnskd_mobilevit_xxs_banlgf | 5 | -2.24 | 0.0311 | 0.4973 | 0.0625 | -1.46 |
| nnskd_mobilevit_xxs_ema | 5 | -0.50 | 0.7539 | 1.0000 | 0.6250 | -0.15 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.38 | 0.1417 | 1.0000 | 0.1875 | 0.82 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.09 | 0.9528 | 1.0000 | 0.8125 | -0.03 |
| nnskd_mobilevit_xxs_kd | 5 | -0.65 | 0.6925 | 1.0000 | 0.8125 | -0.19 |
| nnskd_mobilevit_xxs_nm | 5 | +4.15 | 0.0624 | 0.9364 | 0.0625 | 1.15 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.50 | 0.7786 | 1.0000 | 0.6250 | 0.13 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.76 | 0.7271 | 1.0000 | 0.8125 | 0.17 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.79 | 0.5621 | 1.0000 | 0.4652 | 0.28 |
| pattlite | 5 | +0.41 | 0.6507 | 1.0000 | 0.8125 | 0.22 |
| resnet18 | 5 | -0.18 | 0.8157 | 1.0000 | 1.0000 | -0.11 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +4.28 | 0.0007 | 0.0105 | 0.0625 | 4.30 |
| microexpnet | 5 | +14.12 | 0.0000 | 0.0001 | 0.0625 | 14.04 |
| mobilevit_xxs | 5 | +0.44 | 0.2467 | 1.0000 | 0.3125 | 0.61 |
| mobilevit_xxs_recipe | 5 | +1.05 | 0.2093 | 1.0000 | 0.3125 | 0.67 |
| nnskd_mobilevit_xxs | 5 | -0.28 | 0.5995 | 1.0000 | 0.8125 | -0.25 |
| nnskd_mobilevit_xxs_aux | 5 | -0.51 | 0.1889 | 1.0000 | 0.3125 | -0.71 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.92 | 0.2413 | 1.0000 | 0.3125 | -0.61 |
| nnskd_mobilevit_xxs_ema | 5 | +0.05 | 0.9099 | 1.0000 | 1.0000 | 0.05 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.11 | 0.7859 | 1.0000 | 0.6250 | 0.13 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.58 | 0.4017 | 1.0000 | 0.4375 | -0.42 |
| nnskd_mobilevit_xxs_kd | 5 | -0.40 | 0.6096 | 1.0000 | 0.4375 | -0.25 |
| nnskd_mobilevit_xxs_nm | 5 | +1.17 | 0.2177 | 1.0000 | 0.1875 | 0.65 |
| nnskd_mobilevit_xxs_tinf | 5 | -0.28 | 0.6505 | 1.0000 | 0.8125 | -0.22 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.00 | 0.9972 | 1.0000 | 0.8125 | -0.00 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.52 | 0.3832 | 1.0000 | 0.4375 | -0.44 |
| pattlite | 5 | +0.60 | 0.3435 | 1.0000 | 0.4375 | 0.48 |
| resnet18 | 5 | +0.51 | 0.4221 | 1.0000 | 0.6250 | 0.40 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.01 | 0.0110 | 0.1427 | 0.0625 | -2.00 |
| microexpnet | 5 | +0.11 | 0.0000 | 0.0005 | 0.0625 | 9.33 |
| mobilevit_xxs | 5 | -0.01 | 0.1827 | 1.0000 | 0.3125 | -0.72 |
| mobilevit_xxs_recipe | 5 | +0.15 | 0.0001 | 0.0019 | 0.0625 | 6.58 |
| nnskd_mobilevit_xxs | 5 | +0.00 | 0.2540 | 1.0000 | 0.3125 | 0.60 |
| nnskd_mobilevit_xxs_aux | 5 | +0.00 | 0.7971 | 1.0000 | 1.0000 | 0.12 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.01 | 0.0587 | 0.6459 | 0.1250 | 1.17 |
| nnskd_mobilevit_xxs_ema | 5 | +0.16 | 0.0000 | 0.0002 | 0.0625 | 11.77 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.00 | 0.3008 | 1.0000 | 0.3125 | -0.53 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.01 | 0.0176 | 0.2112 | 0.0625 | 1.74 |
| nnskd_mobilevit_xxs_kd | 5 | +0.01 | 0.1739 | 1.0000 | 0.3125 | 0.74 |
| nnskd_mobilevit_xxs_nm | 5 | +0.01 | 0.1565 | 1.0000 | 0.0625 | 0.78 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.00 | 0.4605 | 1.0000 | 0.6250 | 0.36 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.17 | 0.0002 | 0.0031 | 0.0625 | 5.69 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.01 | 0.1770 | 1.0000 | 0.3125 | 0.73 |
| pattlite | 5 | +0.00 | 0.6024 | 1.0000 | 0.6250 | 0.25 |
| resnet18 | 5 | -0.00 | 0.3436 | 1.0000 | 0.6250 | -0.48 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.95 | 0.2915 | 1.0000 | 0.3125 | 0.54 |
| microexpnet | 5 | +24.01 | 0.0000 | 0.0002 | 0.0625 | 11.51 |
| mobilevit_xxs | 5 | -1.25 | 0.1540 | 1.0000 | 0.1875 | -0.79 |
| mobilevit_xxs_recipe | 5 | -1.47 | 0.4941 | 1.0000 | 0.4375 | -0.34 |
| nnskd_mobilevit_xxs | 5 | +0.67 | 0.6948 | 1.0000 | 0.8125 | 0.19 |
| nnskd_mobilevit_xxs_aux | 5 | -1.04 | 0.3242 | 1.0000 | 0.4375 | -0.50 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.19 | 0.6927 | 1.0000 | 0.7150 | -0.19 |
| nnskd_mobilevit_xxs_ema | 5 | -1.64 | 0.0490 | 0.7837 | 0.1250 | -1.25 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.68 | 0.2649 | 1.0000 | 0.3125 | -0.58 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.39 | 0.6925 | 1.0000 | 1.0000 | 0.19 |
| nnskd_mobilevit_xxs_kd | 5 | +0.04 | 0.9565 | 1.0000 | 1.0000 | 0.03 |
| nnskd_mobilevit_xxs_nm | 5 | +0.52 | 0.7234 | 1.0000 | 0.8125 | 0.17 |
| nnskd_mobilevit_xxs_tinf | 5 | +0.78 | 0.6893 | 1.0000 | 0.8125 | 0.19 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.91 | 0.3778 | 1.0000 | 0.6250 | -0.44 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.75 | 0.2152 | 1.0000 | 0.3125 | -0.66 |
| pattlite | 5 | -0.28 | 0.8525 | 1.0000 | 1.0000 | -0.09 |
| resnet18 | 5 | +0.54 | 0.6973 | 1.0000 | 0.8125 | 0.19 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.64 | 0.1932 | 1.0000 | 0.3125 | 0.70 |
| microexpnet | 5 | +24.04 | 0.0000 | 0.0001 | 0.0625 | 12.96 |
| mobilevit_xxs | 5 | -1.43 | 0.1033 | 0.9298 | 0.0625 | -0.94 |
| mobilevit_xxs_recipe | 5 | -4.97 | 0.0420 | 0.4621 | 0.0625 | -1.32 |
| nnskd_mobilevit_xxs | 5 | -1.53 | 0.2235 | 1.0000 | 0.3125 | -0.64 |
| nnskd_mobilevit_xxs_aux | 5 | -2.01 | 0.0296 | 0.4060 | 0.0625 | -1.48 |
| nnskd_mobilevit_xxs_banlgf | 5 | -1.98 | 0.0290 | 0.4060 | 0.0625 | -1.49 |
| nnskd_mobilevit_xxs_ema | 5 | -3.35 | 0.0023 | 0.0367 | 0.0625 | -3.09 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.58 | 0.3651 | 1.0000 | 0.4375 | -0.46 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.35 | 0.2859 | 1.0000 | 0.3125 | -0.55 |
| nnskd_mobilevit_xxs_kd | 5 | -1.28 | 0.0613 | 0.6134 | 0.1250 | -1.15 |
| nnskd_mobilevit_xxs_nm | 5 | -1.08 | 0.4481 | 1.0000 | 0.6250 | -0.38 |
| nnskd_mobilevit_xxs_tinf | 5 | -1.53 | 0.3037 | 1.0000 | 0.4375 | -0.53 |
| nnskd_mobilevit_xxs_v2 | 5 | -4.75 | 0.0069 | 0.1036 | 0.0625 | -2.29 |
| nnskd_mobilevit_xxs_v3 | 5 | -3.03 | 0.0325 | 0.4060 | 0.0625 | -1.44 |
| pattlite | 5 | -1.79 | 0.2815 | 1.0000 | 0.3125 | -0.56 |
| resnet18 | 5 | +0.47 | 0.7022 | 1.0000 | 0.6250 | 0.18 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 271 | 192 | 0.0002802 |
| efficientface | 1 | 312 | 152 | 8.954e-14 |
| efficientface | 2 | 248 | 178 | 0.0008088 |
| efficientface | 3 | 288 | 158 | 7.696e-10 |
| efficientface | 4 | 284 | 171 | 1.315e-07 |
| microexpnet | 0 | 613 | 154 | 1.375e-65 |
| microexpnet | 1 | 608 | 138 | 3.677e-71 |
| microexpnet | 2 | 557 | 128 | 1.213e-64 |
| microexpnet | 3 | 631 | 141 | 9.272e-75 |
| microexpnet | 4 | 623 | 143 | 3.41e-72 |
| mobilevit_xxs | 0 | 133 | 125 | 0.6631 |
| mobilevit_xxs | 1 | 124 | 104 | 0.2082 |
| mobilevit_xxs | 2 | 140 | 135 | 0.8094 |
| mobilevit_xxs | 3 | 91 | 97 | 0.7155 |
| mobilevit_xxs | 4 | 124 | 78 | 0.001482 |
| mobilevit_xxs_recipe | 0 | 179 | 156 | 0.2293 |
| mobilevit_xxs_recipe | 1 | 198 | 139 | 0.001543 |
| mobilevit_xxs_recipe | 2 | 201 | 171 | 0.1326 |
| mobilevit_xxs_recipe | 3 | 212 | 118 | 2.563e-07 |
| mobilevit_xxs_recipe | 4 | 213 | 140 | 0.0001207 |
| nnskd_mobilevit_xxs | 0 | 167 | 207 | 0.04359 |
| nnskd_mobilevit_xxs | 1 | 157 | 155 | 0.9549 |
| nnskd_mobilevit_xxs | 2 | 167 | 178 | 0.5904 |
| nnskd_mobilevit_xxs | 3 | 169 | 179 | 0.6295 |
| nnskd_mobilevit_xxs | 4 | 171 | 169 | 0.9568 |
| nnskd_mobilevit_xxs_aux | 0 | 173 | 171 | 0.957 |
| nnskd_mobilevit_xxs_aux | 1 | 155 | 149 | 0.7743 |
| nnskd_mobilevit_xxs_aux | 2 | 177 | 191 | 0.498 |
| nnskd_mobilevit_xxs_aux | 3 | 152 | 165 | 0.5004 |
| nnskd_mobilevit_xxs_aux | 4 | 145 | 148 | 0.907 |
| nnskd_mobilevit_xxs_banlgf | 0 | 170 | 190 | 0.3166 |
| nnskd_mobilevit_xxs_banlgf | 1 | 155 | 156 | 1 |
| nnskd_mobilevit_xxs_banlgf | 2 | 177 | 161 | 0.4146 |
| nnskd_mobilevit_xxs_banlgf | 3 | 149 | 165 | 0.3973 |
| nnskd_mobilevit_xxs_banlgf | 4 | 132 | 162 | 0.09061 |
| nnskd_mobilevit_xxs_ema | 0 | 175 | 158 | 0.3806 |
| nnskd_mobilevit_xxs_ema | 1 | 202 | 155 | 0.01479 |
| nnskd_mobilevit_xxs_ema | 2 | 173 | 158 | 0.4416 |
| nnskd_mobilevit_xxs_ema | 3 | 186 | 149 | 0.04903 |
| nnskd_mobilevit_xxs_ema | 4 | 196 | 157 | 0.04297 |
| nnskd_mobilevit_xxs_emaonly | 0 | 148 | 175 | 0.1479 |
| nnskd_mobilevit_xxs_emaonly | 1 | 156 | 144 | 0.5254 |
| nnskd_mobilevit_xxs_emaonly | 2 | 153 | 157 | 0.8647 |
| nnskd_mobilevit_xxs_emaonly | 3 | 141 | 143 | 0.9527 |
| nnskd_mobilevit_xxs_emaonly | 4 | 153 | 149 | 0.863 |
| nnskd_mobilevit_xxs_gen2 | 0 | 154 | 195 | 0.03211 |
| nnskd_mobilevit_xxs_gen2 | 1 | 166 | 144 | 0.2329 |
| nnskd_mobilevit_xxs_gen2 | 2 | 156 | 165 | 0.6553 |
| nnskd_mobilevit_xxs_gen2 | 3 | 145 | 171 | 0.1595 |
| nnskd_mobilevit_xxs_gen2 | 4 | 154 | 152 | 0.9544 |
| nnskd_mobilevit_xxs_kd | 0 | 145 | 191 | 0.01397 |
| nnskd_mobilevit_xxs_kd | 1 | 157 | 160 | 0.9106 |
| nnskd_mobilevit_xxs_kd | 2 | 184 | 168 | 0.424 |
| nnskd_mobilevit_xxs_kd | 3 | 144 | 167 | 0.2121 |
| nnskd_mobilevit_xxs_kd | 4 | 174 | 145 | 0.1168 |
| nnskd_mobilevit_xxs_nm | 0 | 160 | 189 | 0.1338 |
| nnskd_mobilevit_xxs_nm | 1 | 209 | 146 | 0.0009727 |
| nnskd_mobilevit_xxs_nm | 2 | 190 | 161 | 0.1349 |
| nnskd_mobilevit_xxs_nm | 3 | 195 | 160 | 0.071 |
| nnskd_mobilevit_xxs_nm | 4 | 185 | 163 | 0.2603 |
| nnskd_mobilevit_xxs_tinf | 0 | 166 | 204 | 0.05427 |
| nnskd_mobilevit_xxs_tinf | 1 | 157 | 156 | 1 |
| nnskd_mobilevit_xxs_tinf | 2 | 172 | 175 | 0.9145 |
| nnskd_mobilevit_xxs_tinf | 3 | 167 | 180 | 0.5195 |
| nnskd_mobilevit_xxs_tinf | 4 | 170 | 168 | 0.9566 |
| nnskd_mobilevit_xxs_v2 | 0 | 198 | 175 | 0.2546 |
| nnskd_mobilevit_xxs_v2 | 1 | 223 | 152 | 0.0002894 |
| nnskd_mobilevit_xxs_v2 | 2 | 225 | 179 | 0.02505 |
| nnskd_mobilevit_xxs_v2 | 3 | 211 | 177 | 0.09374 |
| nnskd_mobilevit_xxs_v2 | 4 | 230 | 156 | 0.0001945 |
| nnskd_mobilevit_xxs_v3 | 0 | 169 | 194 | 0.2077 |
| nnskd_mobilevit_xxs_v3 | 1 | 188 | 150 | 0.044 |
| nnskd_mobilevit_xxs_v3 | 2 | 139 | 175 | 0.04808 |
| nnskd_mobilevit_xxs_v3 | 3 | 152 | 169 | 0.3719 |
| nnskd_mobilevit_xxs_v3 | 4 | 148 | 170 | 0.2389 |
| pattlite | 0 | 189 | 203 | 0.5115 |
| pattlite | 1 | 206 | 172 | 0.0895 |
| pattlite | 2 | 199 | 188 | 0.6113 |
| pattlite | 3 | 192 | 187 | 0.8372 |
| pattlite | 4 | 218 | 176 | 0.03874 |
| resnet18 | 0 | 167 | 201 | 0.08525 |
| resnet18 | 1 | 217 | 172 | 0.02556 |
| resnet18 | 2 | 198 | 201 | 0.9203 |
| resnet18 | 3 | 204 | 179 | 0.22 |
| resnet18 | 4 | 200 | 174 | 0.196 |
