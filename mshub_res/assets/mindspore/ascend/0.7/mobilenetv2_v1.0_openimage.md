# MobileNetV2

---

model-name: mobilenetV2

backbone-name: mobilenetV2

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: openimage

f1: 0.55



author: MindSpore team

update-time: 2020-09-10

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/mobilenetv2

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2_ascend.ckpt
    asset-sha256: 0ce485e2ed61602d8bf15332db9801f114e820c142744b18f02491879421ecb3

  -
    file-format: mindir
    asset-link: https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/mobilenetv2.mindir
    asset-sha256: aba47ddc769ffac130bcea855e9b3553e15e4ed83c716314fa15f546ebac9d45

license: Apache2.0

summary: mobilenetv2 used to classify 600 classes of openimage
---


## Introduction

This MindSpore Hub model uses the implementation of MobileNetV2 from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv2.

This model has been trained on openimage, and we use 600 class from [class table](https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from PIL import Image
import cv2

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/mobilenetv2_v1.0_openimage"

network = mshub.load(model, num_classes=601, include_top=True, activation="Sigmoid")
network.set_train(False)
```

## Citation

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.
