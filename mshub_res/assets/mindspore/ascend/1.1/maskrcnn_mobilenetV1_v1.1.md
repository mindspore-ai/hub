# Mask R-CNN

---

model-name: maskrcnn

backbone-name: Mobilenetv1

module-type: cv

fine-tunable: True

input-shape: [2, 3, 768, 1280]

model-version: 1.1

train-dataset: coco2017

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/maskrcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/maskrcnn_ascend_r111_coco2017_offical_cv_bs2_bbox36/maskrcnn_ascend_r111_coco2017_offical_cv_bs2_bbox36.8.ckpt>
    asset-sha256: 2c97e5c276e81f3630e4c736a7357acc42dc1c6f5f8ceb2093d76083b0e84e2d

license: Apache2.0

summary: maskrcnn used to do instance segmentation.

---

## Introduction

This MindSpore Hub model uses the implementation of maskrcnn from the MindSpore model zoo on Gitee at model_zoo/official/cv/maskrcnn.

maskrcnn is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/maskrcnn](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/maskrcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/maskrcnn_mobilenetv1_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper: Kaiming He, Georgia Gkioxari, Piotr Dollar, Ross Girshick, Facebook AI Research (FAIR). Mask R-CNN.
