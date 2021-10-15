# faster_rcnn

---

model-name: faster_rcnn

backbone-name: faster_rcnn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: coco2017

accuracy: 64.3

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/faster_rcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/fasterrcnnresnet152_ascend_v130_coco2017_official_cv_bs2_acc64.3/fasterrcnnresnet152_ascend_v130_coco2017_official_cv_bs2_acc64.3.ckpt>
    asset-sha256: 8bdce4abb45407ae395369a8cb0c2c1e78694d136e5e7f6332a604ff7c2d8007

license: Apache2.0

summary: faster_rcnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of faster_rcnn from the MindSpore model zoo on Gitee at model_zoo/official/cv/faster_rcnn.

faster_rcnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/faster_rcnn](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/faster_rcnn/README.md).

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

model = "mindspore/ascend/1.3/fasterrcnnresnet152_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Ren S , He K , Girshick R , et al. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2015, 39(6).
