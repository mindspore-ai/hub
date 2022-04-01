# mobilenetv1

---

model-name: mobilenetv1

backbone-name: mobilenetv1

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: cifar10

evaluation: top1acc93.17 | top5acc99.81

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/mobilenetv1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/mobilenetv1_ascend_v160_cifar10_official_cv_top1acc93.17_top5acc99.81.ckpt>
    asset-sha256: 88aa89d6183c7268981ca7b0f4f7e17b851a1e0c4870a852f81252ae3a4b5057

license: Apache2.0

summary: mobilenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv1 from the MindSpore model zoo on Gitee at official/cv/mobilenetv1.

mobilenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/mobilenetv1](https://gitee.com/mindspore/models/blob/r1.6/official/cv/mobilenetv1/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/mobilenetv1_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Howard A G , Zhu M , Chen B , et al. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications[J]. 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
