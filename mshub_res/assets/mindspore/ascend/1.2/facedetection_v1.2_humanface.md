# FaceDetection

---

model-name: FaceDetection

backbone-name: FaceDetection

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: humanface

accuracy: 77

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/FaceDetection>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/facedetection_ascend_v120_humanface_research_cv_bs64_acc77/facedetection_ascend_v120_humanface_research_cv_bs64_acc77.ckpt>
    asset-sha256: 87963ecf35cc27f1edf7f56f68f7e22a5395e159d165d8dd70fa9245973a8755

license: Apache2.0

summary: FaceDetection is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceDetection from the MindSpore model zoo on Gitee at model_zoo/research/cv/FaceDetection.

FaceDetection is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/FaceDetection](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/FaceDetection/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/facedetection_v1.2_humanface"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Joseph Redmon, Ali Farhadi, YOLOv3: An Incremental Improvement.
