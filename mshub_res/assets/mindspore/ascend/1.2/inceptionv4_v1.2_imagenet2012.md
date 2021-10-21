# inceptionv4

---

model-name: inceptionv4

backbone-name: inceptionv4

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 79

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/inceptionv4>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/inceptionv4_ascend_v120_imagenet2012_official_cv_bs128_top1acc79_top5acc94/inceptionv4_ascend_v120_imagenet2012_official_cv_bs128_top1acc79_top5acc94.ckpt>
    asset-sha256: da517828508f915ef06b3f33c45b8d52e0eaa019bbb86080de7f4beea30377f1

license: Apache2.0

summary: inceptionv4 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of inceptionv4 from the MindSpore model zoo on Gitee at model_zoo/official/cv/inceptionv4.

inceptionv4 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/inceptionv4](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/inceptionv4/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/inceptionv4_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi. Computer Vision and Pattern Recognition[J]. 2016.
