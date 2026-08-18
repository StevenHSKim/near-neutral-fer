# Raw dataset layouts expected by `data/prepare_*.py`

Datasets are **not** redistributed here; obtain them from their authors.

| Dataset | Files |
|---|---|
| RAF-DB basic | `RAFDB/EmoLabel/list_patition_label.txt`, `RAFDB/Image/aligned/{train_XXXXX,test_XXXX}_aligned.jpg` |
| FERPlus | `FERPlus/FERPlus_Label.csv` (Usage, Image name, 10 vote columns), `FERPlus/FERPlus_Image/*.png` |
| CK+48 (Kaggle) | `CKPlus/ckplus_labels.csv` (image_name,label,emotion), `CKPlus/ckplus_images/*.png` |

Outputs (git-ignored) per dataset `<cache>/<ds>/`:
`<ds>_images.npy` (N,112,112,3 uint8), `<ds>_manifest.csv`, `<ds>_manifest.md5`.

Manifest columns: `path,label,split[,extra…]`. RAF-DB val = 10 % stratified hold-out of
official train (seed 0). FERPlus keeps all 10 vote counts, `neutral_share`, `total_votes`
and `near_neutral` (majority ≠ neutral & neutral_share ≥ 0.3). CK+48 labels are mapped to
RAF-DB indices (contempt dropped) and are `test` only.
