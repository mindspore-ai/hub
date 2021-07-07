# yolov3_darknet53_quant

---

model-name: yolov3_darknet53_quant

backbone-name: yolov3_darknet53_quant

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: coco2014

accuracy: 29

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/yolov3_darknet53_quant>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/yolov3darknet53quant_ascend_v120_coco2014_official_cv_bs16_acc29/yolov3darknet53quant_ascend_v120_coco2014_official_cv_bs16_acc29.ckpt>
    asset-sha256: b57432ee3903b31466fa8dc0533ab54781190e9ec8b1e6bbe5d1c717e5dd868b

license: Apache2.0

summary: yolov3_darknet53_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_darknet53_quant from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_darknet53_quant.

yolov3_darknet53_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/yolov3_darknet53_quant](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/yolov3_darknet53_quant/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/yolov3darknet53quant_v1.2_coco2014"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. YOLOv3: An Incremental Improvement. Joseph Redmon, Ali Farhadi,
