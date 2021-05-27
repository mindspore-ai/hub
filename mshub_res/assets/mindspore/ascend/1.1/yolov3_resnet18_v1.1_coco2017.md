# yolov3_resnet18

---

model-name: yolov3_resnet18

backbone-name: resnet18

module-type: cv-object_detection

fine-tunable: True

input-shape: [352, 640, 3]

model-version: 1.1

train-dataset: coco2017

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/yolov3_resnet18>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/yolov3resnet18_ascend_v111_coco2017_offical_cv_bs32_acc86/yolov3resnet18_ascend_v111_coco2017_offical_cv_bs32_acc86.ckpt>
    asset-sha256: 07309d5f3b9a8475362029bc74cf3a143586693f9882d7eed16f5fc3aaa0e49c

license: Apache2.0

summary: yolov3_resnet18 with the shape 352 * 640 for object detection

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_resnet18 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_resnet18.

yolov3_resnet18 is a one-stage object detection network. More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/cv/yolov3_resnet18](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/yolov3_resnet18/README.md).

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

model = "mindspore/ascend/1.1/yolov3_resnet18_v1.1_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
