# maskrcnn_mobilenetv1

---

model-name: maskrcnn_mobilenetv1

backbone-name: maskrcnn_mobilenetv1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: coco2017

accuracy: 22

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/maskrcnn_mobilenetv1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/maskrcnnmobilenetv1_ascend_v120_coco2017_official_cv_bs2_bboxacc22_segmacc15/maskrcnnmobilenetv1_ascend_v1120_coco2017_official_cv_bs2_bboxacc22_segmacc15.ckpt>
    asset-sha256: 24b7da5bdca127b0c646adb873029a34d0b6be7c561de6f8e99bb6bccfc0f8db

license: Apache2.0

summary: maskrcnn_mobilenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of maskrcnn_mobilenetv1 from the MindSpore model zoo on Gitee at model_zoo/official/cv/maskrcnn_mobilenetv1.

maskrcnn_mobilenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/maskrcnn_mobilenetv1](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/maskrcnn_mobilenetv1/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/maskrcnnmobilenetv1_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Georgia Gkioxari, Piotr Dollar and Ross Girshick. "MaskRCNN"
