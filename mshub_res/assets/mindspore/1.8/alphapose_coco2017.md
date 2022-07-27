# AlphaPose

---

model-name: AlphaPose

backbone-name: AlphaPose

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: coco2017

evaluation: acc71.86

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/AlphaPose>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/alphapose_ascend_v180_coco2017_research_cv_acc71.86.ckpt>
    asset-sha256: f8873c73702fb26bb7b8ae1fc877630d8b941057595fab4ddf56ff4ffd1c151e

license: Apache2.0

summary: AlphaPose is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of AlphaPose from the MindSpore model zoo on Gitee at research/cv/AlphaPose.

AlphaPose is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/AlphaPose](https://gitee.com/mindspore/models/blob/r1.8/research/cv/AlphaPose/README_CN.md).

All parameters in the module are trainable.

## Citation

Fang H S , Xie S , Tai Y W , et al. RMPE: Regional Multi-person Pose Estimation

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
