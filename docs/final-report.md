# 최종 결과 보고서 — 중립-근처 미세 표정 인식을 위한 자기-지식 증류 기반 경량 FER

과제: 2025년도 석사과정생연구장려금 「중립 표정-근처 미세 표정 인식을 위한 자기-지식 증류 기반
경량 얼굴 표정 인식 연구」 · 산출물 저장소: https://github.com/StevenHSKim/near-neutral-fer
작성일: 2026-08-22 (모든 수치는 저장소의 raw run 아티팩트에서 `analysis/analyze.py`로 자동 생성)

## 1. 수행 내용 요약

1. **베이스라인 구축(1단계)** — 경량 FER 카운터파트 4종(EfficientFace AAAI'21, PAtt-Lite IEEE
   Access'24, MicroExpNet IPTA'19, MobileViT-XXS ICLR'22)과 상한 참조 ResNet-18을 단일 PyTorch
   코드베이스에 재구현하고, 동일 프로토콜(112×112, ImageNet 사전학습, 동일 증강·최적화·에폭)로
   RAF-DB / FER2013 / SFEW 2.0에서 각 5~10 seed 학습. 파라미터 수는 원 논문과 일치함을 테스트로
   검증(예: EfficientFace 1.273M vs 논문 1.28M).
2. **제안 기법 NN-SKD(2단계)** — 두 가지 학습 전용 자기-지식 증류:
   - **공간적 self-KD (LGF)**: stride 8/16/32 특징을 1×1 lateral conv로 융합한 Local-Global-Fusion
     교사(SE+공간 attention)가 학생 헤드·보조 헤드를 logit KD(T=4)와 attention-map 증류로 지도.
   - **세대 간 self-KD (born-again)**: 동일 아키텍처·동일 seed의 학습 완료 체크포인트를 고정
     교사로 사용.
   두 신호 모두 추론 시 완전히 제거되어 **배포 그래프는 순수 백본과 비트 동일**(테스트로 검증).
3. **평가·최적화(3단계)** — 반복실험(설정당 5~10 seeds), paired t/Wilcoxon(Holm 보정)/McNemar/
   Cohen's d, ONNX 내보내기 및 CPU 지연시간 실측.

## 2. 핵심 결과 (test accuracy, mean ± std)

| 배포 그래프 | Params/MFLOPs/CPU | RAF-DB | FER2013 | SFEW 2.0 |
|---|---|---|---|---|
| **NN-SKD (제안)** | 0.953M / 135 / 5.8ms | **84.92 ± 0.31** | **71.42 ± 0.44** | 36.47 ± 2.38 |
| MobileViT-XXS (백본) | 동일 | 84.29 ± 0.57 | 70.63 ± 0.90 | 36.55 ± 2.91 |
| PAtt-Lite | 1.094M / 173 / 3.9ms | 84.09 ± 0.45 | 70.08 ± 0.32 | 33.53 ± 2.77 |
| EfficientFace | 1.273M / 80 / 3.0ms | 81.00 ± 0.84 | 69.18 ± 0.72 | 37.20 ± 2.40 |
| MicroExpNet | 0.085M / 10 / 0.3ms | 69.43 ± 0.63 | 52.40 ± 0.96 | 22.82 ± 3.16 |
| ResNet-18 (참조) | 11.18M / 970 / 19.8ms | 84.22 ± 0.55 | 70.60 ± 0.93 | 37.08 ± 3.46 |

통계 검증 (seed-paired, n=10):
- **RAF-DB**: 제안 vs 백본 **+0.63pp** — paired t p=0.004 (**Holm 보정 후 p=0.046**),
  Wilcoxon p=0.004, d=1.20. 모든 경량 카운터파트·ResNet-18 대비 평균 우위.
- **FER2013**: born-again 제안 vs 백본 **+0.79pp** — t p=0.011, Wilcoxon p=0.011, d=1.01.
- **SFEW 2.0**: 학습 773장으로 전 모델 통계적 동급(|d|≤0.3) — 한계로 명시.

중립-근처 성능 (계획서 핵심 지표):
- RAF-DB: neutral recall +1.97pp (p=0.03), 중립 혼동 4클래스(sad/fear/disgust/anger) macro-F1
  +1.40pp (p=0.06), 보정 오차(ECE) 개선 (p=0.006).
- FER2013: 중립 혼동 4클래스 macro-F1 **+1.66pp** (Wilcoxon p=0.0098).

효율 (실측, ONNX Runtime 1스레드): 배포 그래프가 백본과 동일하므로 **추가 지연·크기 0** —
5.8ms(171 FPS)/3.99MB로 ResNet-18 대비 3.4× 빠르고 11× 작으며 정확도는 상회.

## 3. 과학적 발견 (부정 결과 포함)

1. **공간적 self-KD의 적용 조건**: LGF는 실해상도 정렬 얼굴(RAF-DB, ~100px)에서만 유효하고
   48px 업샘플 데이터(FER2013/FERPlus)에서는 효과가 없음 — 하위 계층에 증류할 국소 텍스처가
   입력에 존재해야 한다는 메커니즘적 설명과 일치. 저해상도에서는 **세대 간 born-again 증류**가
   유효(+0.79pp)함을 확인, 데이터 특성에 따른 self-KD 선택 지침을 제시.
2. **EMA 자기-교사 안정성**: EMA momentum(0.999)의 유효 창이 총 학습 스텝을 초과하면 교사가
   초기 상태에 고정되어 학습이 붕괴함(SFEW에서 실측). steps/epoch에 맞춘 적응형 momentum으로
   해결 — 소규모 데이터셋 self-KD의 실무적 주의점.
3. Mixup/CutMix+logit adjustment는 40~60 epoch 예산에서 오히려 성능을 저해(−1.3pp),
   2세대 born-again은 추가 이득 없음 — 전 결과를 저장소에 기록.

## 4. 재현성 장치

고정 seed·결정론 커널(같은 seed → 로짓 비트 동일, 테스트로 검증), `requirements.lock` 환경
동결, 모든 run에 config/git hash/GPU 기록, 데이터 매니페스트 md5, 60+ 단위 테스트, 수치 전체가
스크립트 자동 생성(수기 입력 없음), 재개 가능한 스윕 큐.

## 5. 한계 및 향후 과제

- SFEW 2.0은 표본 부족으로 검정력이 낮음(전 모델 동급). AffectNet(라이선스 필요) 확보 시
  V/A 라벨 기반 near-neutral 저강도 부분집합 평가로 확장 가능.
- MS-Celeb 등 얼굴 사전학습을 쓰면 절대 성능은 더 오르나(원 논문들과의 차이 원인), 본 연구는
  공정 비교를 위해 전 모델 ImageNet 사전학습으로 통일.
- Jetson 실기기 측정은 미수행(스펙 범위 제외) — ONNX CPU 측정으로 대체, 변환 스크립트 제공.
