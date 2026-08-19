"""Class taxonomies shared by preprocessing, datasets and metrics.

RAF-DB official numbering is 1..7 = surprise, fear, disgust, happiness, sadness,
anger, neutral; we store label = number - 1.
FERPlus columns follow the official FERPlus_Label.csv order.
"""

RAFDB_CLASSES = ["surprise", "fear", "disgust", "happiness", "sadness", "anger", "neutral"]
FERPLUS_CLASSES = ["neutral", "happiness", "surprise", "sadness", "anger", "disgust", "fear", "contempt"]
FERPLUS_VOTE_COLUMNS = FERPLUS_CLASSES + ["unknown", "NF"]

# CK+48 (Kaggle csv) emotion strings -> RAF-DB index. Contempt has no RAF-DB counterpart.
CKPLUS_TO_RAFDB = {
    "anger": 5,
    "contempt": None,
    "disgust": 2,
    "fear": 1,
    "happy": 3,
    "happiness": 3,
    "sadness": 4,
    "sad": 4,
    "surprise": 0,
}

NEUTRAL_INDEX = {"rafdb": 6, "ferplus": 0}

# Classes most often confused with neutral (fixed a priori): sadness, fear, disgust, anger.
NEAR_NEUTRAL_CLASSES = {
    "rafdb": [4, 1, 2, 5],
    "ferplus": [3, 6, 5, 4],
}

NUM_CLASSES = {"rafdb": len(RAFDB_CLASSES), "ferplus": len(FERPLUS_CLASSES)}

# FER2013 csv emotion ids (0 Angry,1 Disgust,2 Fear,3 Happy,4 Sad,5 Surprise,6 Neutral) -> RAF-DB index
FER2013_TO_RAFDB = {0: 5, 1: 2, 2: 1, 3: 3, 4: 4, 5: 0, 6: 6}
# SFEW 2.0 emotion strings -> RAF-DB index
SFEW_TO_RAFDB = {"angry": 5, "disgust": 2, "fear": 1, "happy": 3, "neutral": 6, "sad": 4, "surprise": 0}

# Every dataset name -> the label space (taxonomy) its labels are expressed in.
LABEL_SPACE = {"rafdb": "rafdb", "ferplus": "ferplus", "ckplus": "rafdb", "fer2013": "rafdb", "sfew": "rafdb"}


def label_space(dataset: str) -> str:
    return LABEL_SPACE[dataset]
