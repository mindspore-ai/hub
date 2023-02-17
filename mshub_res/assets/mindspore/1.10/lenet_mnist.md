# lenet

---

model-name: lenet

backbone-name: lenet

module-type: cv-classification

fine-tunable: True

model-version: 1.10

train-dataset: Mnist

evaluation: acc98.05

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/lenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/lenet_ascend_v1100_mnist_official_cv_acc98.05.ckpt>
    asset-sha256: 44f26ea72e5bd8da4d8a75d230b67d28066d738df3c9d61c48460a0b0ee25902

license: Apache2.0

summary: lenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of lenet from the MindSpore model zoo on Gitee at official/cv/lenet.

lenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/lenet](https://gitee.com/mindspore/models/blob/r1.10/official/cv/lenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/lenet_mnist"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Gradient-based learning applied to document recognition](https://ieeexplore.ieee.org/document/726791)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
