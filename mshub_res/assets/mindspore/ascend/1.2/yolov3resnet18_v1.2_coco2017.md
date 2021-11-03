# yolov3_resnet18

---

model-name: yolov3_resnet18

backbone-name: yolov3_resnet18

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: coco2017

accuracy: 86

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/yolov3_resnet18>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/yolov3resnet18_ascend_v120_coco2017_official_cv_bs32_acc86/yolov3resnet18_ascend_v120_coco2017_official_cv_bs32_acc86.ckpt>
    asset-sha256: 6de43507230c43a61210b1765549c44c69bef9a3cc0f8e317db68d3f1314e469

license: Apache2.0

summary: yolov3_resnet18 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_resnet18 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_resnet18.

yolov3_resnet18 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov3_resnet18](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/yolov3_resnet18/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/yolov3resnet18_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
