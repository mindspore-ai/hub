# vit

---

model-name: vit

backbone-name: vit

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: imagenet2012

evaluation: acc74.17

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/cv/vit>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/vit_ascend_v170_imagenet2012_official_cv_acc74.17.ckpt>
    asset-sha256: c24895695e24c1cbb2deb12e4aeb43080cc4e420247cbbe571a70994a6366264

license: Apache2.0

summary: vit is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vit from the MindSpore model zoo on Gitee at official/cv/vit.

vit is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/vit](https://gitee.com/mindspore/models/blob/r1.7/official/cv/vit/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/vit_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby. 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
