# yolov3_darknet53

---

model-name: yolov3_darknet53

backbone-name: yolov3_darknet53

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: coco2014

accuracy: 31.3

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/yolov3_darknet53>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/yolov3darknet53_ascend_v130_coco2014_official_cv_bs32_acc31.3/yolov3darknet53_ascend_v130_coco2014_official_cv_bs32_acc31.3.ckpt>
    asset-sha256: b85b72bff16a6cad1a71c768e48e500589f24715897d8b35ac743ae11faa07b3

license: Apache2.0

summary: yolov3_darknet53 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_darknet53 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_darknet53.

yolov3_darknet53 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov3_darknet53](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/yolov3_darknet53/README.md).

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

model = "mindspore/ascend/1.3/yolov3darknet53_v1.3_coco2014"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. YOLOv3: An Incremental Improvement. Joseph Redmon, Ali Farhadi,
