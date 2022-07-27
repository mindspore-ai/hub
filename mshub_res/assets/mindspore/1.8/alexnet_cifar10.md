# alexnet

---

model-name: alexnet

backbone-name: alexnet

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: cifar10

evaluation: acc89.38

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/alexnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/alexnet_ascend_v180_cifar10_official_cv_acc89.38.ckpt>
    asset-sha256: 84569e4934f9a49093d50ba43f851a761fb35a8dad72c991ae928e0646a261c7

license: Apache2.0

summary: alexnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of alexnet from the MindSpore model zoo on Gitee at official/cv/alexnet.

alexnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/alexnet](https://gitee.com/mindspore/models/blob/r1.8/official/cv/alexnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/alexnet_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Krizhevsky A, Sutskever I, Hinton G E. ImageNet Classification with Deep ConvolutionalNeural Networks. *Advances In Neural Information Processing Systems*. 2012.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
