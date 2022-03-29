# centernet_resnet50_v1

---

model-name: centernet_resnet50_v1

backbone-name: centernet_resnet50_v1

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: coco2017

evaluation: mAP30.8

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/centernet_resnet50_v1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/centernetresnet50v1_ascend_v130_coco2017_research_cv_mAP30.8.ckpt>
    asset-sha256: a3bf9973d423847b59a2fc56d17e630650e95fb6862019c29b9a7bb92268c962

license: Apache2.0

summary: centernet_resnet50_v1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of centernet_resnet50_v1 from the MindSpore model zoo on Gitee at research/cv/centernet_resnet50_v1.

centernet_resnet50_v1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/centernet_resnet50_v1](https://gitee.com/mindspore/models/blob/r1.3/research/cv/centernet_resnet50_v1/README.md).

All parameters in the module are trainable.

## Citation

Objects as Points. 2019. Xingyi Zhou(UT Austin) and Dequan Wang(UC Berkeley) and Philipp Krahenbuhl(UT Austin)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
