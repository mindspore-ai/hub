# yolov4shape416

---

model-name: yolov4shape416

backbone-name: yolov4shape416

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: coco2017

accuracy: 11

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/yolov4>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/yolov4shape416_ascend_v120_coco2017_official_cv_bs8_acc11/yolov4shape416_ascend_v120_coco2017_official_cv_bs8_acc11.ckpt>
    asset-sha256: ac16697134e1a76a20395739e21139b89d29f739391389e56514a7af48da82d3

license: Apache2.0

summary: yolov4shape416 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov4shape416 from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov4shape416.

yolov4shape416 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov4shape416](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/yolov4/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/yolov4shape416_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
