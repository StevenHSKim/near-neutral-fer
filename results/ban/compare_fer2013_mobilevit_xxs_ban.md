# fer2013: mobilevit_xxs_ban vs each counterpart (seed-paired)

Positive Δ favours the proposed model (for FNR/ECE the sign is flipped so that positive is still better).

## Acc (`test.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.44 | 0.0020 | 0.0163 | 0.0625 | 3.19 |
| microexpnet | 5 | +19.21 | 0.0000 | 0.0000 | 0.0625 | 24.75 |
| mobilevit_xxs | 5 | +0.76 | 0.0183 | 0.0916 | 0.0679 | 1.72 |
| nnskd_mobilevit_xxs | 5 | +1.39 | 0.0040 | 0.0283 | 0.0625 | 2.65 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.53 | 0.1110 | 0.2220 | 0.1875 | 0.91 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.73 | 0.0207 | 0.0916 | 0.0625 | 1.66 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.50 | 0.1885 | 0.2220 | 0.3125 | 0.71 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.94 | 0.0129 | 0.0772 | 0.0625 | 1.91 |
| pattlite | 5 | +1.54 | 0.0005 | 0.0048 | 0.0625 | 4.53 |
| resnet18 | 5 | +1.01 | 0.0504 | 0.1511 | 0.1250 | 1.24 |

## Macro-F1 (`test.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.69 | 0.0080 | 0.0479 | 0.0625 | 2.20 |
| microexpnet | 5 | +29.04 | 0.0000 | 0.0000 | 0.0625 | 25.18 |
| mobilevit_xxs | 5 | +0.86 | 0.0613 | 0.2452 | 0.1250 | 1.15 |
| nnskd_mobilevit_xxs | 5 | +2.09 | 0.0062 | 0.0435 | 0.0625 | 2.36 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.93 | 0.1451 | 0.4353 | 0.1875 | 0.81 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.17 | 0.0047 | 0.0380 | 0.0625 | 2.54 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.88 | 0.2032 | 0.4353 | 0.3125 | 0.68 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.46 | 0.0017 | 0.0156 | 0.0625 | 3.33 |
| pattlite | 5 | +1.63 | 0.0279 | 0.1396 | 0.0625 | 1.51 |
| resnet18 | 5 | +0.68 | 0.1998 | 0.4353 | 0.3125 | 0.69 |

## NN-4 F1 (`test.near_neutral_macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.21 | 0.0101 | 0.0886 | 0.0625 | 2.05 |
| microexpnet | 5 | +39.37 | 0.0000 | 0.0000 | 0.0625 | 21.60 |
| mobilevit_xxs | 5 | +1.19 | 0.0962 | 0.4811 | 0.1250 | 0.97 |
| nnskd_mobilevit_xxs | 5 | +2.81 | 0.0098 | 0.0886 | 0.0625 | 2.07 |
| nnskd_mobilevit_xxs_banlgf | 5 | +1.34 | 0.1345 | 0.4811 | 0.1875 | 0.84 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.59 | 0.0105 | 0.0886 | 0.0625 | 2.03 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.22 | 0.2591 | 0.5182 | 0.3125 | 0.59 |
| nnskd_mobilevit_xxs_v3 | 5 | +2.00 | 0.0125 | 0.0886 | 0.0625 | 1.93 |
| pattlite | 5 | +1.76 | 0.1173 | 0.4811 | 0.1250 | 0.89 |
| resnet18 | 5 | +0.75 | 0.3905 | 0.5182 | 0.6250 | 0.43 |

## FNR (`test.fnr`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +0.93 | 0.0777 | 0.2966 | 0.1250 | 1.06 |
| microexpnet | 5 | +4.37 | 0.0001 | 0.0006 | 0.0625 | 7.90 |
| mobilevit_xxs | 5 | +0.57 | 0.0051 | 0.0462 | 0.0625 | 2.49 |
| nnskd_mobilevit_xxs | 5 | +0.81 | 0.1121 | 0.2966 | 0.1250 | 0.91 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.84 | 0.0315 | 0.1888 | 0.0625 | 1.45 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.05 | 0.0467 | 0.2334 | 0.0625 | 1.27 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.03 | 0.0111 | 0.0775 | 0.0625 | 2.00 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.17 | 0.0059 | 0.0469 | 0.0625 | 2.39 |
| pattlite | 5 | +0.61 | 0.1059 | 0.2966 | 0.1250 | 0.93 |
| resnet18 | 5 | +0.78 | 0.0741 | 0.2966 | 0.0679 | 1.07 |

## Neu-Recall (`test.neutral_recall`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.14 | 0.2429 | 1.0000 | 0.3125 | 0.61 |
| microexpnet | 5 | +16.49 | 0.0001 | 0.0012 | 0.0625 | 6.58 |
| mobilevit_xxs | 5 | +0.06 | 0.8941 | 1.0000 | 0.6250 | 0.06 |
| nnskd_mobilevit_xxs | 5 | -0.16 | 0.9013 | 1.0000 | 1.0000 | -0.06 |
| nnskd_mobilevit_xxs_banlgf | 5 | -0.70 | 0.6339 | 1.0000 | 0.8125 | -0.23 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.06 | 0.9593 | 1.0000 | 1.0000 | 0.02 |
| nnskd_mobilevit_xxs_gen2 | 5 | -1.21 | 0.1070 | 0.7277 | 0.1250 | -0.93 |
| nnskd_mobilevit_xxs_v3 | 5 | -1.47 | 0.1040 | 0.7277 | 0.1250 | -0.94 |
| pattlite | 5 | +2.91 | 0.0310 | 0.2483 | 0.1250 | 1.46 |
| resnet18 | 5 | +1.95 | 0.0210 | 0.1894 | 0.0625 | 1.65 |

## Neu-F1 (`test.neutral_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +2.78 | 0.0318 | 0.1908 | 0.0625 | 1.45 |
| microexpnet | 5 | +16.87 | 0.0000 | 0.0002 | 0.0625 | 9.91 |
| mobilevit_xxs | 5 | +0.93 | 0.0956 | 0.4780 | 0.1250 | 0.97 |
| nnskd_mobilevit_xxs | 5 | +1.15 | 0.1270 | 0.5079 | 0.1875 | 0.86 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.87 | 0.2574 | 0.7721 | 0.3125 | 0.59 |
| nnskd_mobilevit_xxs_emaonly | 5 | +1.64 | 0.0177 | 0.1245 | 0.0625 | 1.74 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.85 | 0.2959 | 0.7721 | 0.4375 | 0.54 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.91 | 0.2920 | 0.7721 | 0.3125 | 0.54 |
| pattlite | 5 | +2.77 | 0.0074 | 0.0663 | 0.0625 | 2.25 |
| resnet18 | 5 | +2.43 | 0.0156 | 0.1245 | 0.0625 | 1.81 |

## ECE (`test.ece`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | -0.01 | 0.2089 | 0.4178 | 0.4375 | -0.67 |
| microexpnet | 5 | +0.04 | 0.0001 | 0.0013 | 0.0625 | 6.46 |
| mobilevit_xxs | 5 | +0.00 | 0.0942 | 0.3769 | 0.1250 | 0.98 |
| nnskd_mobilevit_xxs | 5 | +0.01 | 0.1157 | 0.3769 | 0.1875 | 0.90 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.01 | 0.0479 | 0.2874 | 0.1250 | 1.26 |
| nnskd_mobilevit_xxs_emaonly | 5 | +0.00 | 0.4102 | 0.4178 | 0.6250 | 0.41 |
| nnskd_mobilevit_xxs_gen2 | 5 | +0.01 | 0.0092 | 0.0738 | 0.0625 | 2.11 |
| nnskd_mobilevit_xxs_v3 | 5 | +0.01 | 0.0137 | 0.0961 | 0.0625 | 1.88 |
| pattlite | 5 | +0.01 | 0.0581 | 0.2903 | 0.1250 | 1.18 |
| resnet18 | 5 | +0.03 | 0.0006 | 0.0056 | 0.0625 | 4.36 |

## CK+ Acc (`ckplus.acc`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.17 | 0.0124 | 0.1118 | 0.0625 | 1.93 |
| microexpnet | 5 | +20.88 | 0.0000 | 0.0001 | 0.0625 | 12.46 |
| mobilevit_xxs | 5 | -0.19 | 0.8037 | 1.0000 | 0.8125 | -0.12 |
| nnskd_mobilevit_xxs | 5 | +1.12 | 0.2178 | 1.0000 | 0.3125 | 0.65 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.17 | 0.8829 | 1.0000 | 0.8125 | 0.07 |
| nnskd_mobilevit_xxs_emaonly | 5 | -1.06 | 0.5108 | 1.0000 | 0.6250 | -0.32 |
| nnskd_mobilevit_xxs_gen2 | 5 | +1.66 | 0.1715 | 1.0000 | 0.1875 | 0.74 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.25 | 0.1075 | 0.7522 | 0.1875 | 0.92 |
| pattlite | 5 | +1.86 | 0.3694 | 1.0000 | 0.6250 | 0.45 |
| resnet18 | 5 | +5.83 | 0.0149 | 0.1190 | 0.0625 | 1.83 |

## CK+ F1 (`ckplus.macro_f1`)

| vs | n | Δ mean | t-test p | Holm p | Wilcoxon p | Cohen's d |
|---|---|---|---|---|---|---|
| efficientface | 5 | +3.78 | 0.0239 | 0.2154 | 0.0625 | 1.58 |
| microexpnet | 5 | +24.39 | 0.0000 | 0.0004 | 0.0625 | 8.85 |
| mobilevit_xxs | 5 | -0.43 | 0.6691 | 1.0000 | 0.8125 | -0.21 |
| nnskd_mobilevit_xxs | 5 | +0.92 | 0.5466 | 1.0000 | 0.6250 | 0.29 |
| nnskd_mobilevit_xxs_banlgf | 5 | +0.89 | 0.4275 | 1.0000 | 0.4375 | 0.39 |
| nnskd_mobilevit_xxs_emaonly | 5 | -0.10 | 0.9357 | 1.0000 | 0.8125 | -0.04 |
| nnskd_mobilevit_xxs_gen2 | 5 | +2.37 | 0.0972 | 0.6806 | 0.3125 | 0.96 |
| nnskd_mobilevit_xxs_v3 | 5 | +1.76 | 0.1507 | 0.9039 | 0.1875 | 0.79 |
| pattlite | 5 | +2.77 | 0.2756 | 1.0000 | 0.4375 | 0.56 |
| resnet18 | 5 | +6.01 | 0.0245 | 0.2154 | 0.0625 | 1.57 |

## McNemar (test set, per seed; n01 = proposed right & other wrong, n10 = reverse)

| vs | seed | n01 | n10 | p |
|---|---|---|---|---|
| efficientface | 0 | 317 | 271 | 0.06339 |
| efficientface | 1 | 377 | 265 | 1.127e-05 |
| efficientface | 2 | 369 | 284 | 0.0009972 |
| efficientface | 3 | 363 | 250 | 5.74e-06 |
| efficientface | 4 | 331 | 249 | 0.0007562 |
| microexpnet | 0 | 906 | 250 | 1.099e-87 |
| microexpnet | 1 | 951 | 243 | 2.802e-99 |
| microexpnet | 2 | 923 | 234 | 3.982e-97 |
| microexpnet | 3 | 925 | 255 | 1.404e-89 |
| microexpnet | 4 | 985 | 260 | 1.424e-99 |
| mobilevit_xxs | 0 | 178 | 146 | 0.08487 |
| mobilevit_xxs | 1 | 168 | 129 | 0.02729 |
| mobilevit_xxs | 2 | 186 | 158 | 0.1454 |
| mobilevit_xxs | 3 | 188 | 151 | 0.05039 |
| mobilevit_xxs | 4 | 153 | 153 | 1 |
| nnskd_mobilevit_xxs | 0 | 279 | 257 | 0.3644 |
| nnskd_mobilevit_xxs | 1 | 279 | 234 | 0.05195 |
| nnskd_mobilevit_xxs | 2 | 295 | 232 | 0.006862 |
| nnskd_mobilevit_xxs | 3 | 288 | 217 | 0.001812 |
| nnskd_mobilevit_xxs | 4 | 286 | 237 | 0.03573 |
| nnskd_mobilevit_xxs_banlgf | 0 | 243 | 252 | 0.7192 |
| nnskd_mobilevit_xxs_banlgf | 1 | 242 | 237 | 0.855 |
| nnskd_mobilevit_xxs_banlgf | 2 | 254 | 223 | 0.1695 |
| nnskd_mobilevit_xxs_banlgf | 3 | 251 | 208 | 0.04983 |
| nnskd_mobilevit_xxs_banlgf | 4 | 256 | 231 | 0.2768 |
| nnskd_mobilevit_xxs_emaonly | 0 | 236 | 217 | 0.3977 |
| nnskd_mobilevit_xxs_emaonly | 1 | 242 | 212 | 0.1734 |
| nnskd_mobilevit_xxs_emaonly | 2 | 260 | 231 | 0.2063 |
| nnskd_mobilevit_xxs_emaonly | 3 | 255 | 207 | 0.02866 |
| nnskd_mobilevit_xxs_emaonly | 4 | 229 | 224 | 0.851 |
| nnskd_mobilevit_xxs_gen2 | 0 | 237 | 249 | 0.6178 |
| nnskd_mobilevit_xxs_gen2 | 1 | 231 | 232 | 1 |
| nnskd_mobilevit_xxs_gen2 | 2 | 259 | 210 | 0.02656 |
| nnskd_mobilevit_xxs_gen2 | 3 | 244 | 207 | 0.08993 |
| nnskd_mobilevit_xxs_gen2 | 4 | 240 | 223 | 0.4572 |
| nnskd_mobilevit_xxs_v3 | 0 | 277 | 250 | 0.2574 |
| nnskd_mobilevit_xxs_v3 | 1 | 259 | 229 | 0.1892 |
| nnskd_mobilevit_xxs_v3 | 2 | 281 | 239 | 0.07208 |
| nnskd_mobilevit_xxs_v3 | 3 | 283 | 225 | 0.01137 |
| nnskd_mobilevit_xxs_v3 | 4 | 237 | 226 | 0.6422 |
| pattlite | 0 | 332 | 281 | 0.04335 |
| pattlite | 1 | 329 | 287 | 0.09847 |
| pattlite | 2 | 350 | 280 | 0.005934 |
| pattlite | 3 | 331 | 265 | 0.007704 |
| pattlite | 4 | 307 | 260 | 0.05329 |
| resnet18 | 0 | 281 | 287 | 0.8339 |
| resnet18 | 1 | 336 | 259 | 0.001811 |
| resnet18 | 2 | 325 | 288 | 0.1459 |
| resnet18 | 3 | 314 | 279 | 0.1626 |
| resnet18 | 4 | 306 | 267 | 0.1123 |
