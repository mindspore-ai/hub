# ssdvgg16

---

model-name: ssdvgg16

backbone-name: ssdvgg16

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: coco2017

accuracy: 23

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/ssd>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ssdvgg16_ascend_v120_coco2017_official_cv_bs32_acc23/ssdvgg16_ascend_v120_coco2017_official_cv_bs32_acc23.ckpt>
    asset-sha256: 6d7e1bc721dc7d0c665aa64f15faf557eea0c430a8cd68323a5362f707a8e191

license: Apache2.0

summary: ssdvgg16 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssdvgg16 from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssdvgg16.

ssdvgg16 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/ssdvgg16](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/ssd/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/ssdvgg16_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
