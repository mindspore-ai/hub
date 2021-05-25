# Yolov4

---

model-name: yolov4_cspdarknet53

backbone-name: cspdarknet53

module-type: cv-object_detection

fine-tunable: True

input-shape: [608, 608, 3]

model-version: 1.1

train-dataset: coco2017

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/yolov4>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1
asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/yolov4_ascend_v111_coco2017_offical_cv_bs8_map41/yolov4_ascend_v111_coco2017_offical_cv_bs8_map41.ckpt>
    asset-sha256: 149e54d3813888ded43f01aacccb92e3355e061ea211d53917d35d48ec03a82e

license: Apache2.0

summary: yolov4_darknet53 used to do object detection

---

## Introduction

This MindSpore Hub model uses the implementation of yolov4 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov4.

yolov4 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov4](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/yolov4/README.MD).

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

model = "mindspore/ascend/1.1/yolov4_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
