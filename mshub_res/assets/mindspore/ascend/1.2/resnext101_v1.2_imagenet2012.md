# resnext101

---

model-name: resnext101

backbone-name: resnext101

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 79

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnext101>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnext101_ascend_v120_imagenet2012_official_cv_bs128_topacc179_top5acc94/resnext101_ascend_v120_imagenet2012_official_cv_bs128_topacc179_top5acc94.ckpt>
    asset-sha256: cb16105b011854ffe8bf6a4acb9ad7271928b6d4124a4f2bf0a14cc60fc1836d

license: Apache2.0

summary: resnext101 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnext101 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnext101.

resnext101 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnext101](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnext101/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnext101_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, Kaiming He. Aggregated Residual Transformations for Deep Neural Networks.
