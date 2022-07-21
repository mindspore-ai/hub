# vgg16

---

model-name: vgg16

backbone-name: vgg16

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: cifar10

evaluation: acc93.44

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/vgg16>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/vgg16_ascend_v180_cifar10_official_cv_acc93.44.ckpt>
    asset-sha256: 0ad3742ac1e20bd06c50fe5bfce0d23e4df3e5baf976e360412093a23546f969

license: Apache2.0

summary: vgg16 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vgg16 from the MindSpore model zoo on Gitee at official/cv/vgg16.

vgg16 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/vgg16](https://gitee.com/mindspore/models/blob/r1.8/official/cv/vgg16/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/vgg16_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Simonyan K, zisserman A. Very Deep Convolutional Networks for Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
