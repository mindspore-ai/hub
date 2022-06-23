# centernet

---

model-name: centernet

backbone-name: centernet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: coco2017

evaluation: mAP51.9 | AP50acc78.8 | AP75acc55.5 | medium44.5 | large63.9

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/centernet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/centernet_ascend_v170_coco2017_research_cv_mAP51.9_AP50acc78.8_AP75acc55.5_medium44.5_large63.9.ckpt>
    asset-sha256: 9c6fbfe8d3e47807d63f3c59726201bff036ddcdbb011a73e6276a4364a4c041

license: Apache2.0

summary: centernet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of centernet from the MindSpore model zoo on Gitee at research/cv/centernet.

centernet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/centernet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/centernet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/centernet_coco2017"
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
