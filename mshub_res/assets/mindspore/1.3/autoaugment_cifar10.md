# autoaugment

---

model-name: WRN

backbone-name: autoaugment

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: cifar10

evaluation: acc97.22

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/autoaugment>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/autoaugment_ascend_v130_cifar10_research_cv_acc97.22.ckpt>
    asset-sha256: 3dfbe4b3bfca01c359c016f09377eb157dfd3c569543e52f483b8b451b652d2d

license: Apache2.0

summary: autoaugment is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of autoaugment from the MindSpore model zoo on Gitee at research/cv/autoaugment.

autoaugment is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/autoaugment](https://gitee.com/mindspore/models/blob/r1.3/research/cv/autoaugment/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/autoaugment_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Cubuk, Ekin D., et al. "Autoaugment: Learning augmentation strategies from data." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
