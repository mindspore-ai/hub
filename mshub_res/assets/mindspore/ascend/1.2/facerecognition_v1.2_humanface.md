# FaceRecognition

---

model-name: FaceRecognition

backbone-name: FaceRecognition

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: humanface

accuracy: 93

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/FaceRecognition>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/facerecognition_ascend_v120_humanface_research_cv_bs192_acc93/facerecognition_ascend_v120_humanface_research_cv_bs192_acc93.ckpt>
    asset-sha256: 540e6be3f8d3a0c5b0261b59dda2775dca4405b1f9643307c919fa2a38b286eb

license: Apache2.0

summary: FaceRecognition is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceRecognition from the MindSpore model zoo on Gitee at model_zoo/research/cv/FaceRecognition.

FaceRecognition is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/FaceRecognition](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/FaceRecognition/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/facerecognition_v1.2_humanface"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"
