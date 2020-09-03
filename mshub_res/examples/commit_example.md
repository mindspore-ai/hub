# [model-name]

---

model-name: [] <required>

backbone-name: [] <required>

module-type: [audio/cv/nlp/recommend] e.g. cv-classification <required>

> CV: classification, object_detection, tracking, image_generation, image_denoise, super_resolution, image_enhancement, instance_segmentation, semantic_segmentation, panoptic_segmentation, keypoint_detection, face_recognition, metric_learning, video, 3d, medical, anomaly_detection, pose_estimation, OCR, other
>
> NLP:
>
> Audio:
>
> Recommend:
>
> Other:

fine-tunable: [True/False] <required>

input-shape: [224, 224, 3] <required>

model-version: [1.0] <required>

train-dataset: [imagenet/coco/...] <required>

accuracy: []<optional>



author: [] <required>

update-time: [date-time] <required>

repo-link: [link] <required>

user-id: [] <required>



file-format: [mindir/ckpt/onnx/air] <required>

used-for: [inference/extract-feature/transfer-learning] <required>

featured-image: [path_to_image] <optional>

train-backend: [cpu/gpu/ascend] <required>

infer-backend: [cpu/gpu/ascend] <optional>

mindspore-version: [0.6] <required>


allow-cache-ckpt: [True/False] # will try to optimize the model to run in mobile devices, default False

assets
  -
    file-format: [ckpt/geir/air/onnx] <required>
    asset-link: []  <required>
    asset_sha256: [] <required>
  -
    file-format: [ckpt/mindir/air/onnx] <optional>
    asset-link: []  <optional>
    asset_sha256: [] <optional>
  -
    ...

asset-link: [] <required>

asset_sha256: <required>



license: [Apache2.0] <required>

summary: [Description of the model， one line description] <required>

---


## Introduction

[Detailed Description of the model]

## Usage

## Citation

## Change Log
