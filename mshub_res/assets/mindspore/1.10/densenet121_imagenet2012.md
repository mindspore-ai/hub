# densenet121

---

model-name: densenet121

backbone-name: densenet

module-type: cv-classification

fine-tunable: True

model-version: 1.10

train-dataset: ImageNet2012

evaluation: top1acc75.13

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/densenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/densenet121_ascend_v1100_imagenet2012_official_cv_top1acc75.13.ckpt>
    asset-sha256: 25f1d54f9af1e010d1c16ca0bb3b5d126932dd60c8f758ba96f7c1b8b22d55a2

license: Apache2.0

summary: densenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of densenet from the MindSpore model zoo on Gitee at official/cv/densenet.

densenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/densenet](https://gitee.com/mindspore/models/blob/r1.10/official/cv/densenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/densenet121_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Densely Connected Convolutional Networks](https://arxiv.org/pdf/1608.06993.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
