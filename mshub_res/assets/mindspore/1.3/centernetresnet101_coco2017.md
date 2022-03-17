# centernet_resnet101

---

model-name: centernet_resnet101

backbone-name: centernet_resnet101

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: coco2017

evaluation: mAP33.9 | AP50acc52 | AP75acc36

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/centernet_resnet101>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/centernetresnet101_ascend_v130_coco2017_research_cv_mAP33.9_AP50acc52_AP75acc36.ckpt>
    asset-sha256: c8fe163020a1498f69b00317f6d6bd21a05dc47ddef3d36942a01aa575d92122

license: Apache2.0

summary: centernet_resnet101 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of centernet_resnet101 from the MindSpore model zoo on Gitee at research/cv/centernet_resnet101.

centernet_resnet101 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/centernet_resnet101](https://gitee.com/mindspore/models/blob/r1.3/research/cv/centernet_resnet101/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/centernetresnet101_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Objects as Points. 2019. Xingyi Zhou(UT Austin) and Dequan Wang(UC Berkeley) and Philipp Krahenbuhl(UT Austin)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
