# yolov3_darknet53

---

model-name: yolov3_darknet53

backbone-name: darknet53

module-type: cv-object_detection

fine-tunable: True

input-shape: [608, 608, 3]

model-version: 1.1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/yolov3_darknet53>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/yolov3darknet53_ascend_v111_coco2014_offical_cv_bs32_acc31/yolov3darknet53_ascend_v111_coco2014_offical_cv_bs32_acc31.ckpt>
    asset-sha256: ec7941e96a0a253de4bb29adc8d3e3bc66ca252ff8c3db62f3ac2a3cafe94efb

license: Apache2.0

summary: yolov3_darknet53 used to do object detection

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_darknet53 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_darknet53.

yolov3_darknet53 supports 10 different input shapes for improving accuracy. More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/cv/yolov3_darknet53](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/yolov3_darknet53/README.md).

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

model = "mindspore/ascend/1.1/yolov3_darknet53_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
