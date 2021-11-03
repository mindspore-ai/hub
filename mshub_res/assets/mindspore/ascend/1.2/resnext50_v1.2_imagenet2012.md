# resnext50

---

model-name: resnext50

backbone-name: resnext50

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 78

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnext50>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnext50_ascend_v120_imagenet2012_official_cv_bs128_acc78/resnext50_ascend_v120_imagenet2012_official_cv_bs128_acc78.ckpt>
    asset-sha256: b2f0b3b4d0c94dad8cc7be45b7c9b17ce824e5f2f7ed2d7f7befceb130bc1c24

license: Apache2.0

summary: resnext50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnext50 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnext50.

resnext50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnext50](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnext50/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnext50_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Xie S, Girshick R, Dollár, Piotr, et al. Aggregated Residual Transformations for Deep Neural Networks. 2016.
