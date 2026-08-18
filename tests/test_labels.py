from nnfer.data import labels as L


def test_rafdb_order_matches_official_numbering():
    assert L.RAFDB_CLASSES[6] == "neutral" and L.RAFDB_CLASSES[0] == "surprise"
    assert L.NEUTRAL_INDEX["rafdb"] == L.RAFDB_CLASSES.index("neutral")


def test_ferplus_order_matches_csv_columns():
    assert L.FERPLUS_CLASSES == ["neutral", "happiness", "surprise", "sadness", "anger", "disgust", "fear", "contempt"]
    assert L.NEUTRAL_INDEX["ferplus"] == 0
    assert L.FERPLUS_VOTE_COLUMNS[-2:] == ["unknown", "NF"]


def test_ckplus_mapping_targets_rafdb():
    assert L.CKPLUS_TO_RAFDB["contempt"] is None
    assert L.RAFDB_CLASSES[L.CKPLUS_TO_RAFDB["happy"]] == "happiness"
    assert L.RAFDB_CLASSES[L.CKPLUS_TO_RAFDB["sadness"]] == "sadness"


def test_near_neutral_classes_are_sad_fear_disgust_anger():
    for ds, names in (("rafdb", L.RAFDB_CLASSES), ("ferplus", L.FERPLUS_CLASSES)):
        assert sorted(names[i] for i in L.NEAR_NEUTRAL_CLASSES[ds]) == ["anger", "disgust", "fear", "sadness"]
        assert L.NUM_CLASSES[ds] == len(names)
