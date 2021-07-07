# lenet_quant

---

model-name: lenet_quant

backbone-name: lenet_quant

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: mnist

accuracy: 98

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/lenet_quant>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/lenetquant_ascend_v120_mnist_official_cv_bs32_acc98/lenetquant_ascend_v120_mnist_official_cv_bs32_acc98.ckpt>
    asset-sha256: c40195e4343cf2a6a22fef712c03d3a7faf5407d9fda473b273f38a1da6f635d

license: Apache2.0

summary: lenet_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of lenet_quant from the MindSpore model zoo on Gitee at model_zoo/official/cv/lenet_quant.

lenet_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/lenet_quant](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/lenet_quant/Readme_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/lenetquant_v1.2_mnist"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Y.Lecun, L.Bottou, Y.Bengio, P.Haffner. Gradient-Based Learning Applied to Document Recognition. *Proceedings of the IEEE*. 1998.
