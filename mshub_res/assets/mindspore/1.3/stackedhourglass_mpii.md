# StackedHourglass

---

model-name: StackedHourglass

backbone-name: StackedHourglass

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: mpii

evaluation: acc87.7

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/StackedHourglass>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/stackedhourglass_ascend_v130_mpii_research_cv_acc87.7.ckpt>
    asset-sha256: 61919979915eb5083883e241aa92585b55a8c09f44f5f36c9e18022af6e9f6d6

license: Apache2.0

summary: StackedHourglass is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of StackedHourglass from the MindSpore model zoo on Gitee at research/cv/StackedHourglass.

StackedHourglass is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/StackedHourglass](https://gitee.com/mindspore/models/blob/r1.3/research/cv/StackedHourglass/README_CN.md).

All parameters in the module are trainable.

## Citation

Stacked Hourglass Networks for Human Pose Estimation

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
