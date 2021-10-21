# lenet_quant

---

model-name: lenet_quant

backbone-name: lenet_quant

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: mnist

accuracy: 98.79

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/lenet_quant>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/lenetquant_ascend_v130_mnist_official_cv_bs64_acc98.79/lenetquant_ascend_v130_mnist_official_cv_bs64_acc98.79.ckpt>
    asset-sha256: 92c14388fdf4ea90811de5031652b2e58570a5abf7c3653b0e958fb0e30f3546

license: Apache2.0

summary: lenet_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of lenet_quant from the MindSpore model zoo on Gitee at model_zoo/official/cv/lenet_quant.

lenet_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/lenet_quant](lenet_quant check readme link failed, now readmelink is https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/lenet_quant/Readme.md and https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/lenet_quant/Readme_CN.md).

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

model = "mindspore/ascend/1.3/lenetquant_v1.3_mnist"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Y.Lecun, L.Bottou, Y.Bengio, P.Haffner. Gradient-Based Learning Applied to Document Recognition. *Proceedings of the IEEE*. 1998.
