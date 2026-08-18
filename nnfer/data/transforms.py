"""Shared augmentation / normalisation pipeline (spec §4) — identical for every model."""
from torchvision import transforms as T

IMAGENET_MEAN, IMAGENET_STD = (0.485, 0.456, 0.406), (0.229, 0.224, 0.225)


def build_transforms(train: bool, size: int = 112):
    norm = [T.ToTensor(), T.Normalize(IMAGENET_MEAN, IMAGENET_STD)]
    if not train:
        return T.Compose(norm)
    return T.Compose([
        T.RandomResizedCrop(size, scale=(0.8, 1.0)),
        T.RandomHorizontalFlip(),
        *norm,
        T.RandomErasing(p=0.5),
    ])
