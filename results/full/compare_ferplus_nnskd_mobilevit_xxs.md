# ferplus: nnskd_mobilevit_xxs vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.52 | 0.1370 | 0.5480 | 0.1875 | 0.83 |
| microexpnet | 5 | +14.90 | 0.0000 | 0.0000 | 0.0625 | 53.71 |
| mobilevit_xxs | 5 | -0.17 | 0.5868 | 1.0000 | 0.6250 | -0.26 |
| pattlite | 5 | +0.30 | 0.5355 | 1.0000 | 0.6250 | 0.30 |
| resnet18 | 5 | -0.03 | 0.8820 | 1.0000 | 0.6250 | -0.07 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.38 | 0.8182 | 1.0000 | 0.6250 | -0.11 |
| microexpnet | 5 | +30.29 | 0.0000 | 0.0000 | 0.0625 | 14.37 |
| mobilevit_xxs | 5 | -0.43 | 0.7635 | 1.0000 | 1.0000 | -0.14 |
| pattlite | 5 | +3.57 | 0.2662 | 1.0000 | 0.3125 | 0.58 |
| resnet18 | 5 | -0.55 | 0.6528 | 1.0000 | 1.0000 | -0.22 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -1.18 | 0.4597 | 1.0000 | 0.6250 | -0.37 |
| microexpnet | 5 | +41.76 | 0.0000 | 0.0000 | 0.0625 | 16.20 |
| mobilevit_xxs | 5 | -0.32 | 0.8031 | 1.0000 | 1.0000 | -0.12 |
| pattlite | 5 | +1.42 | 0.5986 | 1.0000 | 0.6250 | 0.26 |
| resnet18 | 5 | -1.18 | 0.3780 | 1.0000 | 0.4375 | -0.44 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.77 | 0.3073 | 1.0000 | 0.4375 | 0.52 |
| microexpnet | 5 | +17.27 | 0.0000 | 0.0000 | 0.0625 | 16.74 |
| mobilevit_xxs | 5 | +0.42 | 0.4879 | 1.0000 | 0.6250 | 0.34 |
| pattlite | 5 | +0.69 | 0.3491 | 1.0000 | 0.3125 | 0.47 |
| resnet18 | 5 | +0.50 | 0.4278 | 1.0000 | 0.4375 | 0.39 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.19 | 0.7409 | 1.0000 | 0.8125 | 0.16 |
| microexpnet | 5 | +0.06 | 0.8094 | 1.0000 | 0.7055 | 0.12 |
| mobilevit_xxs | 5 | -0.55 | 0.3932 | 1.0000 | 0.6250 | -0.43 |
| pattlite | 5 | -0.19 | 0.6771 | 1.0000 | 0.6250 | -0.20 |
| resnet18 | 5 | -0.59 | 0.5560 | 1.0000 | 0.4375 | -0.29 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.69 | 0.0577 | 0.2307 | 0.1250 | 1.18 |
| microexpnet | 5 | +11.33 | 0.0000 | 0.0000 | 0.0625 | 18.42 |
| mobilevit_xxs | 5 | +0.01 | 0.9710 | 1.0000 | 1.0000 | 0.02 |
| pattlite | 5 | +0.42 | 0.3824 | 1.0000 | 0.3125 | 0.44 |
| resnet18 | 5 | +0.06 | 0.8069 | 1.0000 | 0.8125 | 0.12 |

## NN-sub Acc@.3 (`test.nn_subset_acc@0.3`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +1.18 | 0.6392 | 1.0000 | 0.6250 | 0.23 |
| microexpnet | 5 | +31.37 | 0.0001 | 0.0007 | 0.0625 | 6.46 |
| mobilevit_xxs | 5 | -0.59 | 0.8243 | 1.0000 | 0.8125 | -0.11 |
| pattlite | 5 | +0.59 | 0.8400 | 1.0000 | 0.8539 | 0.10 |
| resnet18 | 5 | +0.59 | 0.8537 | 1.0000 | 0.8125 | 0.09 |

## NN-sub F1@.3 (`test.nn_subset_macro_f1@0.3`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -2.53 | 0.4530 | 0.9134 | 0.6250 | -0.37 |
| microexpnet | 5 | +27.51 | 0.0003 | 0.0017 | 0.0625 | 5.08 |
| mobilevit_xxs | 5 | -3.43 | 0.3045 | 0.9134 | 0.3125 | -0.53 |
| pattlite | 5 | -2.55 | 0.6145 | 0.9134 | 0.8125 | -0.24 |
| resnet18 | 5 | -3.49 | 0.1663 | 0.6653 | 0.1875 | -0.76 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.02 | 0.0053 | 0.0263 | 0.0625 | -2.47 |
| microexpnet | 5 | +0.02 | 0.0095 | 0.0382 | 0.0625 | 2.09 |
| mobilevit_xxs | 5 | -0.01 | 0.0484 | 0.0968 | 0.0625 | -1.26 |
| pattlite | 5 | -0.01 | 0.0144 | 0.0432 | 0.0625 | -1.85 |
| resnet18 | 5 | -0.01 | 0.1628 | 0.1628 | 0.3125 | -0.76 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 199 | 181 | 0.3832 |
| efficientface | 1 | 199 | 209 | 0.656 |
| efficientface | 2 | 208 | 165 | 0.02952 |
| efficientface | 3 | 176 | 172 | 0.8723 |
| efficientface | 4 | 208 | 171 | 0.06429 |
| microexpnet | 0 | 686 | 166 | 9.103e-76 |
| microexpnet | 1 | 652 | 135 | 5.184e-82 |
| microexpnet | 2 | 699 | 162 | 3.768e-80 |
| microexpnet | 3 | 682 | 154 | 5.585e-80 |
| microexpnet | 4 | 706 | 167 | 1.621e-79 |
| mobilevit_xxs | 0 | 145 | 168 | 0.2136 |
| mobilevit_xxs | 1 | 148 | 183 | 0.06149 |
| mobilevit_xxs | 2 | 154 | 161 | 0.7354 |
| mobilevit_xxs | 3 | 170 | 150 | 0.2882 |
| mobilevit_xxs | 4 | 167 | 153 | 0.4675 |
| pattlite | 0 | 207 | 160 | 0.01623 |
| pattlite | 1 | 166 | 208 | 0.03386 |
| pattlite | 2 | 190 | 193 | 0.9186 |
| pattlite | 3 | 207 | 172 | 0.08059 |
| pattlite | 4 | 193 | 177 | 0.4355 |
| resnet18 | 0 | 174 | 184 | 0.6344 |
| resnet18 | 1 | 207 | 211 | 0.8834 |
| resnet18 | 2 | 175 | 182 | 0.7509 |
| resnet18 | 3 | 188 | 164 | 0.2202 |
| resnet18 | 4 | 198 | 206 | 0.7277 |
