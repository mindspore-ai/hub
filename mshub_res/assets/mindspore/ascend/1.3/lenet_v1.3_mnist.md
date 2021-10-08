# lenet

---

model-name: lenet

backbone-name: lenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: mnist

accuracy: 98.49

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/lenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/lenet_ascend_v130_mnist_official_cv_bs32_acc98.49/lenet_ascend_v130_mnist_official_cv_bs32_acc98.49.ckpt>
    asset-sha256: f0734abb1f74d3e4d96ed9baf3fd6f17596943d58cbb17509506fae4518fceef

license: Apache2.0

summary: lenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of lenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/lenet.

lenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/lenet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/lenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/lenet_v1.3_mnist"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Y.Lecun, L.Bottou, Y.Bengio, P.Haffner. Gradient-Based Learning Applied to Document Recognition. *Proceedings of the IEEE*. 1998.
