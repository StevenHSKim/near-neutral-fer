# sfew: nnskd_mobilevit_xxs_banlgf vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.92 | 0.5845 | 1.0000 | 0.8125 | -0.27 |
| microexpnet | 5 | +13.33 | 0.0026 | 0.0334 | 0.0625 | 3.00 |
| mobilevit_xxs | 5 | +0.73 | 0.6017 | 1.0000 | 0.6250 | 0.25 |
| mobilevit_xxs_ban | 5 | +0.68 | 0.3655 | 1.0000 | 0.4652 | 0.46 |
| mobilevit_xxs_recipe | 5 | +1.80 | 0.1713 | 1.0000 | 0.1875 | 0.74 |
| nnskd_mobilevit_xxs | 5 | -0.29 | 0.8681 | 1.0000 | 1.0000 | -0.08 |
| nnskd_mobilevit_xxs_ema | 5 | +0.88 | 0.6409 | 1.0000 | 0.8125 | 0.23 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.92 | 0.6027 | 1.0000 | 0.4375 | 0.25 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.05 | 0.9181 | 1.0000 | 1.0000 | 0.05 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.15 | 0.8875 | 1.0000 | 1.0000 | 0.07 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.10 | 0.9380 | 1.0000 | 1.0000 | 0.04 |
| pattlite | 5 | +2.63 | 0.1561 | 1.0000 | 0.1875 | 0.78 |
| resnet18 | 5 | -0.92 | 0.6162 | 1.0000 | 1.0000 | -0.24 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -1.34 | 0.4154 | 1.0000 | 0.8125 | -0.41 |
| microexpnet | 5 | +17.29 | 0.0018 | 0.0230 | 0.0625 | 3.32 |
| mobilevit_xxs | 5 | -0.11 | 0.9430 | 1.0000 | 0.8125 | -0.03 |
| mobilevit_xxs_ban | 5 | +0.19 | 0.8717 | 1.0000 | 0.8125 | 0.08 |
| mobilevit_xxs_recipe | 5 | -0.54 | 0.7227 | 1.0000 | 0.8125 | -0.17 |
| nnskd_mobilevit_xxs | 5 | -0.64 | 0.7544 | 1.0000 | 0.8125 | -0.15 |
| nnskd_mobilevit_xxs_ema | 5 | +0.00 | 0.9990 | 1.0000 | 0.8125 | 0.00 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.73 | 0.4815 | 1.0000 | 0.6250 | 0.35 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.69 | 0.3765 | 1.0000 | 0.4375 | -0.44 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.60 | 0.2858 | 1.0000 | 0.3125 | -0.55 |
| nnskd_mobilevit_xxs_v3 | 5 | -0.58 | 0.6870 | 1.0000 | 0.8125 | -0.19 |
| pattlite | 5 | +1.77 | 0.3888 | 1.0000 | 0.4375 | 0.43 |
| resnet18 | 5 | +0.07 | 0.9693 | 1.0000 | 0.8125 | 0.02 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -2.37 | 0.1108 | 1.0000 | 0.1250 | -0.91 |
| microexpnet | 5 | +10.13 | 0.0021 | 0.0278 | 0.0625 | 3.15 |
| mobilevit_xxs | 5 | -0.44 | 0.7496 | 1.0000 | 1.0000 | -0.15 |
| mobilevit_xxs_ban | 5 | -0.10 | 0.8730 | 1.0000 | 0.8125 | -0.08 |
| mobilevit_xxs_recipe | 5 | -1.89 | 0.3047 | 1.0000 | 0.1875 | -0.53 |
| nnskd_mobilevit_xxs | 5 | -1.94 | 0.1377 | 1.0000 | 0.1875 | -0.83 |
| nnskd_mobilevit_xxs_ema | 5 | +0.98 | 0.5798 | 1.0000 | 0.8125 | 0.27 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.98 | 0.4305 | 1.0000 | 0.4375 | 0.39 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.15 | 0.4453 | 1.0000 | 0.4375 | -0.38 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.85 | 0.4005 | 1.0000 | 0.4375 | -0.42 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.11 | 0.5573 | 1.0000 | 0.6250 | -0.29 |
| pattlite | 5 | +1.96 | 0.4410 | 1.0000 | 0.4375 | 0.38 |
| resnet18 | 5 | +0.25 | 0.8789 | 1.0000 | 1.0000 | 0.07 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.82 | 0.4950 | 1.0000 | 0.6250 | 0.34 |
| microexpnet | 5 | -10.52 | 0.0199 | 0.2590 | 0.0625 | -1.68 |
| mobilevit_xxs | 5 | -0.30 | 0.9169 | 1.0000 | 1.0000 | -0.05 |
| mobilevit_xxs_ban | 5 | -3.95 | 0.2361 | 1.0000 | 0.1875 | -0.62 |
| mobilevit_xxs_recipe | 5 | -3.10 | 0.4246 | 1.0000 | 0.4375 | -0.40 |
| nnskd_mobilevit_xxs | 5 | -1.28 | 0.6259 | 1.0000 | 0.6250 | -0.24 |
| nnskd_mobilevit_xxs_ema | 5 | +0.91 | 0.8123 | 1.0000 | 1.0000 | 0.11 |
| nnskd_mobilevit_xxs_emaonly | 5 | +5.23 | 0.3840 | 1.0000 | 0.6250 | 0.44 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.36 | 0.8919 | 1.0000 | 0.8125 | 0.06 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.40 | 0.5932 | 1.0000 | 0.7150 | -0.26 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.91 | 0.7864 | 1.0000 | 0.8125 | 0.13 |
| pattlite | 5 | +1.46 | 0.5549 | 1.0000 | 1.0000 | 0.29 |
| resnet18 | 5 | +6.08 | 0.0296 | 0.3557 | 0.0625 | 1.48 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -1.46 | 0.8306 | 1.0000 | 0.8125 | -0.10 |
| microexpnet | 5 | +40.24 | 0.0011 | 0.0141 | 0.0625 | 3.77 |
| mobilevit_xxs | 5 | +0.24 | 0.9541 | 1.0000 | 1.0000 | 0.03 |
| mobilevit_xxs_ban | 5 | +6.34 | 0.4901 | 1.0000 | 0.5930 | 0.34 |
| mobilevit_xxs_recipe | 5 | +8.78 | 0.1890 | 1.0000 | 0.3125 | 0.71 |
| nnskd_mobilevit_xxs | 5 | -1.71 | 0.7374 | 1.0000 | 0.8125 | -0.16 |
| nnskd_mobilevit_xxs_ema | 5 | -1.71 | 0.8522 | 1.0000 | 0.8125 | -0.09 |
| nnskd_mobilevit_xxs_emaonly | 5 | -5.37 | 0.5172 | 1.0000 | 0.4652 | -0.32 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.22 | 0.7837 | 1.0000 | 1.0000 | -0.13 |
| nnskd_mobilevit_xxs_v2 | 5 | +2.68 | 0.6077 | 1.0000 | 1.0000 | 0.25 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.95 | 0.6304 | 1.0000 | 0.6250 | -0.23 |
| pattlite | 5 | +7.56 | 0.3447 | 1.0000 | 0.2733 | 0.48 |
| resnet18 | 5 | -8.78 | 0.2370 | 1.0000 | 0.4375 | -0.62 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.34 | 0.9467 | 1.0000 | 1.0000 | 0.03 |
| microexpnet | 5 | +34.52 | 0.0036 | 0.0462 | 0.0625 | 2.75 |
| mobilevit_xxs | 5 | -0.38 | 0.8616 | 1.0000 | 0.6250 | -0.08 |
| mobilevit_xxs_ban | 5 | +2.37 | 0.6457 | 1.0000 | 0.6250 | 0.22 |
| mobilevit_xxs_recipe | 5 | +4.10 | 0.0756 | 0.9075 | 0.1250 | 1.07 |
| nnskd_mobilevit_xxs | 5 | -2.14 | 0.4093 | 1.0000 | 0.4375 | -0.41 |
| nnskd_mobilevit_xxs_ema | 5 | +0.69 | 0.8596 | 1.0000 | 1.0000 | 0.08 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.43 | 0.9179 | 1.0000 | 1.0000 | 0.05 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.27 | 0.8435 | 1.0000 | 1.0000 | -0.09 |
| nnskd_mobilevit_xxs_v2 | 5 | +0.84 | 0.7354 | 1.0000 | 1.0000 | 0.16 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.09 | 0.4759 | 1.0000 | 0.6250 | -0.35 |
| pattlite | 5 | +6.96 | 0.1412 | 1.0000 | 0.1875 | 0.82 |
| resnet18 | 5 | -0.82 | 0.8260 | 1.0000 | 0.6250 | -0.10 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.11 | 0.0043 | 0.0413 | 0.0625 | -2.61 |
| microexpnet | 5 | -0.31 | 0.0000 | 0.0005 | 0.0625 | -9.00 |
| mobilevit_xxs | 5 | -0.02 | 0.2894 | 1.0000 | 0.4375 | -0.55 |
| mobilevit_xxs_ban | 5 | -0.02 | 0.1887 | 0.9434 | 0.3125 | -0.71 |
| mobilevit_xxs_recipe | 5 | -0.10 | 0.0063 | 0.0444 | 0.0625 | -2.34 |
| nnskd_mobilevit_xxs | 5 | +0.00 | 0.7704 | 1.0000 | 1.0000 | 0.14 |
| nnskd_mobilevit_xxs_ema | 5 | -0.14 | 0.0045 | 0.0413 | 0.0625 | -2.57 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.08 | 0.1135 | 0.6807 | 0.1250 | -0.90 |
| nnskd_mobilevit_xxs_gen2 | 5 | -0.01 | 0.3841 | 1.0000 | 0.4375 | -0.44 |
| nnskd_mobilevit_xxs_v2 | 5 | -0.12 | 0.0002 | 0.0021 | 0.0625 | -6.00 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.00 | 0.8493 | 1.0000 | 0.6250 | 0.09 |
| pattlite | 5 | -0.12 | 0.0022 | 0.0242 | 0.0625 | -3.13 |
| resnet18 | 5 | -0.14 | 0.0041 | 0.0413 | 0.0625 | -2.64 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.59 | 0.6641 | 1.0000 | 1.0000 | 0.21 |
| microexpnet | 5 | +1.98 | 0.6527 | 1.0000 | 1.0000 | 0.22 |
| mobilevit_xxs | 5 | -2.31 | 0.6931 | 1.0000 | 0.6250 | -0.19 |
| mobilevit_xxs_ban | 5 | -2.44 | 0.5872 | 1.0000 | 1.0000 | -0.26 |
| mobilevit_xxs_recipe | 5 | -1.68 | 0.7619 | 1.0000 | 1.0000 | -0.15 |
| nnskd_mobilevit_xxs | 5 | -0.91 | 0.7955 | 1.0000 | 1.0000 | -0.12 |
| nnskd_mobilevit_xxs_ema | 5 | -1.27 | 0.7011 | 1.0000 | 0.8125 | -0.18 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.93 | 0.8353 | 1.0000 | 1.0000 | 0.10 |
| nnskd_mobilevit_xxs_gen2 | 5 | -2.29 | 0.6084 | 1.0000 | 0.6250 | -0.25 |
| nnskd_mobilevit_xxs_v2 | 5 | -2.91 | 0.2576 | 1.0000 | 0.3125 | -0.59 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.23 | 0.8189 | 1.0000 | 0.8125 | -0.11 |
| pattlite | 5 | +4.53 | 0.2772 | 1.0000 | 0.3125 | 0.56 |
| resnet18 | 5 | -9.23 | 0.0734 | 0.9545 | 0.1250 | -1.08 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.47 | 0.6765 | 1.0000 | 0.8125 | 0.20 |
| microexpnet | 5 | +5.86 | 0.0219 | 0.2631 | 0.0625 | 1.63 |
| mobilevit_xxs | 5 | -0.55 | 0.8910 | 1.0000 | 1.0000 | -0.07 |
| mobilevit_xxs_ban | 5 | +0.19 | 0.9575 | 1.0000 | 0.8125 | 0.03 |
| mobilevit_xxs_recipe | 5 | -0.18 | 0.9525 | 1.0000 | 1.0000 | -0.03 |
| nnskd_mobilevit_xxs | 5 | -1.84 | 0.1915 | 1.0000 | 0.3125 | -0.70 |
| nnskd_mobilevit_xxs_ema | 5 | -0.90 | 0.6486 | 1.0000 | 0.8125 | -0.22 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.14 | 0.4488 | 1.0000 | 0.6250 | 0.38 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.38 | 0.5143 | 1.0000 | 0.8125 | -0.32 |
| nnskd_mobilevit_xxs_v2 | 5 | -1.68 | 0.3193 | 1.0000 | 0.6250 | -0.51 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.47 | 0.8642 | 1.0000 | 1.0000 | 0.08 |
| pattlite | 5 | +2.28 | 0.4546 | 1.0000 | 0.6250 | 0.37 |
| resnet18 | 5 | -4.69 | 0.0071 | 0.0922 | 0.0625 | -2.27 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 63 | 55 | 0.5195 |
| efficientface | 1 | 54 | 51 | 0.8454 |
| efficientface | 2 | 44 | 67 | 0.03631 |
| efficientface | 3 | 52 | 67 | 0.1992 |
| efficientface | 4 | 53 | 45 | 0.4797 |
| microexpnet | 0 | 110 | 32 | 3.231e-11 |
| microexpnet | 1 | 102 | 32 | 1.041e-09 |
| microexpnet | 2 | 78 | 33 | 2.326e-05 |
| microexpnet | 3 | 95 | 49 | 0.0001572 |
| microexpnet | 4 | 95 | 60 | 0.006133 |
| mobilevit_xxs | 0 | 52 | 40 | 0.2513 |
| mobilevit_xxs | 1 | 51 | 44 | 0.5384 |
| mobilevit_xxs | 2 | 42 | 31 | 0.2416 |
| mobilevit_xxs | 3 | 48 | 46 | 0.9179 |
| mobilevit_xxs | 4 | 40 | 57 | 0.1038 |
| mobilevit_xxs_ban | 0 | 64 | 51 | 0.2631 |
| mobilevit_xxs_ban | 1 | 45 | 45 | 1 |
| mobilevit_xxs_ban | 2 | 39 | 41 | 0.9111 |
| mobilevit_xxs_ban | 3 | 41 | 37 | 0.7343 |
| mobilevit_xxs_ban | 4 | 41 | 42 | 1 |
| mobilevit_xxs_recipe | 0 | 61 | 44 | 0.118 |
| mobilevit_xxs_recipe | 1 | 50 | 37 | 0.198 |
| mobilevit_xxs_recipe | 2 | 41 | 50 | 0.4018 |
| mobilevit_xxs_recipe | 3 | 44 | 37 | 0.5052 |
| mobilevit_xxs_recipe | 4 | 53 | 44 | 0.4168 |
| nnskd_mobilevit_xxs | 0 | 37 | 34 | 0.8126 |
| nnskd_mobilevit_xxs | 1 | 45 | 23 | 0.01034 |
| nnskd_mobilevit_xxs | 2 | 24 | 27 | 0.7798 |
| nnskd_mobilevit_xxs | 3 | 24 | 42 | 0.03558 |
| nnskd_mobilevit_xxs | 4 | 31 | 41 | 0.2888 |
| nnskd_mobilevit_xxs_ema | 0 | 63 | 39 | 0.0223 |
| nnskd_mobilevit_xxs_ema | 1 | 52 | 56 | 0.773 |
| nnskd_mobilevit_xxs_ema | 2 | 34 | 47 | 0.1821 |
| nnskd_mobilevit_xxs_ema | 3 | 54 | 37 | 0.09295 |
| nnskd_mobilevit_xxs_ema | 4 | 39 | 45 | 0.5856 |
| nnskd_mobilevit_xxs_emaonly | 0 | 64 | 41 | 0.0313 |
| nnskd_mobilevit_xxs_emaonly | 1 | 55 | 52 | 0.8468 |
| nnskd_mobilevit_xxs_emaonly | 2 | 29 | 48 | 0.03954 |
| nnskd_mobilevit_xxs_emaonly | 3 | 50 | 46 | 0.7596 |
| nnskd_mobilevit_xxs_emaonly | 4 | 59 | 51 | 0.5047 |
| nnskd_mobilevit_xxs_gen2 | 0 | 28 | 29 | 1 |
| nnskd_mobilevit_xxs_gen2 | 1 | 37 | 42 | 0.653 |
| nnskd_mobilevit_xxs_gen2 | 2 | 34 | 32 | 0.9022 |
| nnskd_mobilevit_xxs_gen2 | 3 | 39 | 40 | 1 |
| nnskd_mobilevit_xxs_gen2 | 4 | 30 | 24 | 0.4966 |
| nnskd_mobilevit_xxs_v2 | 0 | 48 | 52 | 0.7644 |
| nnskd_mobilevit_xxs_v2 | 1 | 47 | 34 | 0.1821 |
| nnskd_mobilevit_xxs_v2 | 2 | 31 | 38 | 0.4704 |
| nnskd_mobilevit_xxs_v2 | 3 | 39 | 32 | 0.4767 |
| nnskd_mobilevit_xxs_v2 | 4 | 31 | 37 | 0.5446 |
| nnskd_mobilevit_xxs_v3 | 0 | 41 | 37 | 0.7343 |
| nnskd_mobilevit_xxs_v3 | 1 | 37 | 28 | 0.3211 |
| nnskd_mobilevit_xxs_v3 | 2 | 25 | 38 | 0.1299 |
| nnskd_mobilevit_xxs_v3 | 3 | 32 | 41 | 0.3492 |
| nnskd_mobilevit_xxs_v3 | 4 | 36 | 25 | 0.2 |
| pattlite | 0 | 65 | 53 | 0.3112 |
| pattlite | 1 | 67 | 47 | 0.07469 |
| pattlite | 2 | 52 | 38 | 0.1702 |
| pattlite | 3 | 52 | 65 | 0.2672 |
| pattlite | 4 | 76 | 55 | 0.08017 |
| resnet18 | 0 | 57 | 50 | 0.5621 |
| resnet18 | 1 | 62 | 57 | 0.714 |
| resnet18 | 2 | 35 | 66 | 0.002654 |
| resnet18 | 3 | 44 | 41 | 0.8284 |
| resnet18 | 4 | 50 | 53 | 0.8439 |
