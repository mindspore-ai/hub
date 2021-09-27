# yolov3_resnet18

---

model-name: yolov3_resnet18

backbone-name: yolov3_resnet18

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: coco2017

accuracy: 88.51

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/yolov3_resnet18>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/yolov3resnet18_ascend_v130_coco2017_official_cv_bs32_class0acc88.51_class0recall65.59_class1acc92.57_class1recall69.82/yolov3resnet18_ascend_v130_coco2017_official_cv_bs32_class0acc88.51_class0recall65.59_class1acc92.57_class1recall69.82.ckpt>
    asset-sha256: 87532719501410d5c50065231c1213b7ba36094f04db931795ed3fbeb7474dba

license: Apache2.0

summary: yolov3_resnet18 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_resnet18 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_resnet18.

yolov3_resnet18 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov3_resnet18](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/yolov3_resnet18/README.md).

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

model = "mindspore/ascend/1.3/yolov3resnet18_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
