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
