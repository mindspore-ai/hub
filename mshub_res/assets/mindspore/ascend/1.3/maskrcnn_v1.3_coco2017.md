# maskrcnn

---

model-name: maskrcnn

backbone-name: maskrcnn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: coco2017

accuracy: 88

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/maskrcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/maskrcnn_ascend_v130_coco2017_official_cv_bs2_bbox37.4_nsegm32.9/maskrcnn_ascend_v130_coco2017_official_cv_bs2_bbox37.4_nsegm32.9.ckpt>
    asset-sha256: 5fa5a1e12cf64538c26a984cd4e1cdd418a5629bfe15b265bb7b49536a6a8a99

license: Apache2.0

summary: maskrcnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of maskrcnn from the MindSpore model zoo on Gitee at model_zoo/official/cv/maskrcnn.

maskrcnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/maskrcnn](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/maskrcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/maskrcnn_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Georgia Gkioxari, Piotr Dollar and Ross Girshick. "MaskRCNN"
