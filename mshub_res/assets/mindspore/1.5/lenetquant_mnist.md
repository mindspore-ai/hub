# lenet_quant

---

model-name: lenet_quant

backbone-name: lenet_quant

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: mnist

evaluation: acc98.79

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/lenet_quant>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/lenetquant_ascend_v150_mnist_official_cv_acc98.79.ckpt>
    asset-sha256: 92c14388fdf4ea90811de5031652b2e58570a5abf7c3653b0e958fb0e30f3546

license: Apache2.0

summary: lenet_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of lenet_quant from the MindSpore model zoo on Gitee at official/cv/lenet_quant.

lenet_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/lenet_quant](https://gitee.com/mindspore/models/blob/r1.5/official/cv/lenet_quant/Readme.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/lenetquant_mnist"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Y.Lecun, L.Bottou, Y.Bengio, P.Haffner. Gradient-Based Learning Applied to Document Recognition. *Proceedings of the IEEE*. 1998.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
