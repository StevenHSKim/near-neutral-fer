"""NN-SKD: Near-Neutral Self-Knowledge Distillation (proposed model, spec §8).

Training graph
    x -> backbone -> [S2 (s8), S3 (s16), S4 (s32)]
         student  : GAP(S4) -> FC                          -> z_S   (the deployed path)
         aux heads: S2 -> 1x1 conv+BN+ReLU -> GAP -> FC     -> z_2
                    S3 -> 1x1 conv+BN+ReLU -> GAP -> FC     -> z_3
         LGF teacher: lateral 1x1 on S2/S3/S4 -> resample to S3 res -> concat -> 1x1 fuse ->
                    SE (channel) + spatial attention -> DW-sep 3x3 -> F_T -> GAP -> FC -> z_T
         adapters : 1x1 conv on S3 and S4 (-> fuse_ch) whose spatial attention maps mimic A(F_T)
Inference graph: backbone -> GAP(S4) -> FC only. Everything else is training-only, so Params/FLOPs
at inference equal the plain backbone (see `inference_parameters()` / `export_student()`).
"""
import torch
import torch.nn.functional as F
from torch import nn

from nnfer.models import register
from nnfer.models.backbones import get_backbone


def conv_bn_relu(cin, cout, k=1, s=1, groups=1):
    return nn.Sequential(nn.Conv2d(cin, cout, k, s, k // 2, groups=groups, bias=False), nn.BatchNorm2d(cout), nn.ReLU(inplace=True))


class SEBlock(nn.Module):
    def __init__(self, ch, r=8):
        super().__init__()
        self.fc = nn.Sequential(nn.Linear(ch, ch // r), nn.ReLU(inplace=True), nn.Linear(ch // r, ch), nn.Sigmoid())

    def forward(self, x):
        return x * self.fc(x.mean((2, 3)))[:, :, None, None]


class SpatialGate(nn.Module):
    def __init__(self, k=7):
        super().__init__()
        self.conv = nn.Conv2d(2, 1, k, padding=k // 2, bias=False)

    def forward(self, x):
        s = torch.cat([x.mean(1, keepdim=True), x.amax(1, keepdim=True)], 1)
        return x * torch.sigmoid(self.conv(s))


class LGFTeacher(nn.Module):
    """Local-Global Fusion teacher: fuses S2/S3/S4 at S3 resolution -> F_T (fuse_ch) and logits z_T."""

    def __init__(self, channels, fuse_ch, num_classes):
        super().__init__()
        c2, c3, c4 = channels
        self.lat2 = conv_bn_relu(c2, fuse_ch)
        self.lat3 = conv_bn_relu(c3, fuse_ch)
        self.lat4 = conv_bn_relu(c4, fuse_ch)
        self.fuse = conv_bn_relu(3 * fuse_ch, fuse_ch)
        self.se = SEBlock(fuse_ch)
        self.sg = SpatialGate()
        self.refine = nn.Sequential(conv_bn_relu(fuse_ch, fuse_ch, 3, groups=fuse_ch), conv_bn_relu(fuse_ch, fuse_ch))
        self.fc = nn.Linear(fuse_ch, num_classes)

    def forward(self, feats):
        s2, s3, s4 = feats
        h, w = s3.shape[-2:]
        f2 = F.adaptive_avg_pool2d(self.lat2(s2), (h, w))
        f3 = self.lat3(s3)
        f4 = F.interpolate(self.lat4(s4), size=(h, w), mode="bilinear", align_corners=False)
        f = self.fuse(torch.cat([f2, f3, f4], 1))
        f = self.refine(self.sg(self.se(f)))
        return f, self.fc(f.mean((2, 3)))


class AuxHead(nn.Module):
    def __init__(self, cin, mid, num_classes):
        super().__init__()
        self.body = conv_bn_relu(cin, mid)
        self.fc = nn.Linear(mid, num_classes)

    def forward(self, x):
        return self.fc(self.body(x).mean((2, 3)))


def attention_map(f):
    """Normalised spatial attention (AT-style): mean over channels of f², flattened, L2-normalised."""
    a = f.pow(2).mean(1).flatten(1)
    return F.normalize(a, dim=1)


class NNSKD(nn.Module):
    def __init__(self, backbone: str, num_classes: int, pretrained: bool = True, fuse_ch: int = 128,
                 aux_heads: bool = True, teacher: bool = True, feat_stages=(3, 4), infer_head: str = "student",
                 dropout: float = 0.0):
        super().__init__()
        self.backbone, ch = get_backbone(backbone, pretrained)
        c2, c3, c4 = ch
        self.drop = nn.Dropout(dropout)
        self.fc = nn.Linear(c4, num_classes)
        self.use_aux, self.use_teacher = aux_heads, teacher
        self.feat_stages = tuple(feat_stages) if teacher else ()
        self.infer_head = infer_head
        if aux_heads:
            self.aux2 = AuxHead(c2, fuse_ch, num_classes)
            self.aux3 = AuxHead(c3, fuse_ch, num_classes)
        if teacher:
            self.teacher = LGFTeacher(ch, fuse_ch, num_classes)
            self.adapters = nn.ModuleDict({str(s): conv_bn_relu({3: c3, 4: c4}[s], fuse_ch) for s in self.feat_stages})

    # ---- inference-only pieces -------------------------------------------------
    def student_logits(self, feats):
        return self.fc(self.drop(feats[-1].mean((2, 3))))

    def inference_parameters(self):
        yield from self.backbone.parameters()
        yield from self.fc.parameters()

    def export_student(self) -> nn.Module:
        """Plain module (backbone -> GAP -> FC) for ONNX export / latency."""
        parent = self

        class Student(nn.Module):
            def __init__(s):
                super().__init__()
                s.backbone, s.fc = parent.backbone, parent.fc

            def forward(s, x):
                return s.fc(s.backbone(x)[-1].mean((2, 3)))

        return Student()

    # ---- forward -----------------------------------------------------------------
    def forward(self, x):
        feats = self.backbone(x)
        if not self.training:
            if self.infer_head == "teacher" and self.use_teacher:
                return self.teacher(feats)[1]
            return self.student_logits(feats)
        out = {"logits": self.student_logits(feats)}
        if self.use_aux:
            out["aux_logits"] = [self.aux2(feats[0]), self.aux3(feats[1])]
        if self.use_teacher:
            f_t, z_t = self.teacher(feats)
            out["teacher_logits"] = z_t
            out["teacher_att"] = attention_map(f_t)
            h, w = f_t.shape[-2:]
            atts = []
            for s in self.feat_stages:
                a = self.adapters[str(s)](feats[s - 2])
                if a.shape[-2:] != (h, w):
                    a = F.interpolate(a, size=(h, w), mode="bilinear", align_corners=False)
                atts.append(attention_map(a))
            out["student_atts"] = atts
        return out


def _make(backbone):
    def builder(num_classes: int, pretrained: bool = True, **kw) -> nn.Module:
        return NNSKD(backbone, num_classes, pretrained, **kw)
    builder.__name__ = f"nnskd_{backbone}"
    return builder


for _bb in ("shufflenetv2", "efficientface", "mobilenetv3s", "mobilenetv1", "mobilevit_xxs"):
    register(f"nnskd_{_bb}")(_make(_bb))


# Plain-backbone baselines (= NN-SKD with every training-only module removed; ablation row (a)).
def _plain(backbone):
    def builder(num_classes: int, pretrained: bool = True, **kw) -> nn.Module:
        kw.update(aux_heads=False, teacher=False)
        return NNSKD(backbone, num_classes, pretrained, **kw)
    builder.__name__ = backbone
    return builder


for _bb in ("shufflenetv2", "mobilenetv3s"):
    register(_bb)(_plain(_bb))
