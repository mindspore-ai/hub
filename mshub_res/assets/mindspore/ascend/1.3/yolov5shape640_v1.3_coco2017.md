# yolov5

---

model-name: yolov5s

backbone-name: yolov5

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: coco2017

accuracy: 36.6

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/yolov5>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/yolov5shape640_ascend_v130_coco2017_official_cv_bs8_acc36.6/yolov5shape640_ascend_v130_coco2017_official_cv_bs8_acc36.6.ckpt>
    asset-sha256: 9e17460882efdf587ee451fcc401d4359f0d1f31eb40825a59c339e65e1ca89b

license: Apache2.0

summary: yolov5 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov5 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov5.

yolov5 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov5](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/yolov5/README.md).

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
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/yolov5shape640_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
