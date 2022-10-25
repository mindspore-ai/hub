# resnet50

---

model-name: resnet50

backbone-name: resnet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc76.97 | top5acc93.44

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/resnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/resnet50_ascend_v190_imagenet2012_official_cv_top1acc76.97_top5acc93.44.ckpt>
    asset-sha256: 41c1479844f6f848d4caf902cf940ebe4727df559495ed45885892fc55a2738f

license: Apache2.0

summary: resnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet from the MindSpore model zoo on Gitee at official/cv/resnet.

resnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/resnet](https://gitee.com/mindspore/models/blob/r1.9/official/cv/resnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/resnet50_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)
2. [Squeeze-and-Excitation Networks](https://arxiv.org/pdf/1709.01507.pdf)
3. [Bag of Tricks for Image Classification with Convolutional Neural Networks](https://arxiv.org/pdf/1812.01187.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
