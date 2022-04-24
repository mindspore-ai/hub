# ecolite

---

model-name: ecolite

backbone-name: ecolite

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: ucf101

evaluation: top1acc87.4 | top5acc97.7

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/ecolite>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/ecolite_ascend_v160_ucf101_research_cv_top1acc87.4_top5acc97.7.ckpt>
    asset-sha256: ba146887f2080fb0c6a1548f6a2764d5e62325a119118713726fe9b3fce4b91e

license: Apache2.0

summary: ecolite is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ecolite from the MindSpore model zoo on Gitee at research/cv/ecolite.

ecolite is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ecolite](https://gitee.com/mindspore/models/blob/r1.6/research/cv/ecolite/README_CN.md).

All parameters in the module are trainable.

## Citation

Mohammadreza Zolfaghari, Kamaljeet Singh, Thomas Brox."ECO: Efficient Convolutional Network forOnline Video Understanding"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
