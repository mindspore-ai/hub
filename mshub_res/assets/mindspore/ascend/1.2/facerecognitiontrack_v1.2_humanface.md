# FaceRecognitionForTracking

---

model-name: FaceRecognitionForTracking

backbone-name: FaceRecognitionForTracking

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: humanface

accuracy: 63

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/FaceRecognitionForTracking>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/facerecognitiontrack_ascend_v120_humanface_research_cv_bs16_acc63/facerecognitiontrack_ascend_v120_humanface_research_cv_bs16_acc63.ckpt>
    asset-sha256: 251d88e0f33a4accc9aad7a3b17e6cb5271784ca2d3969cbaaef94a89cbd7b3f

license: Apache2.0

summary: FaceRecognitionForTracking is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceRecognitionForTracking from the MindSpore model zoo on Gitee at model_zoo/research/cv/FaceRecognitionForTracking.

FaceRecognitionForTracking is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/FaceRecognitionForTracking](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/FaceRecognitionForTracking/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/facerecognitiontrack_v1.2_humanface"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"
