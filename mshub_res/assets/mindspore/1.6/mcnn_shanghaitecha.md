# MCNN

---

model-name: MCNN

backbone-name: MCNN

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: shanghaitecha

evaluation: MAE112.11

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/MCNN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/mcnn_ascend_v160_shanghaitecha_official_cv_MAE112.11.ckpt>
    asset-sha256: 4253dacb804e03a4f03100fe4a9c5eb6de1782f542a70d0840f183b7d758bcf7

license: Apache2.0

summary: MCNN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of MCNN from the MindSpore model zoo on Gitee at official/cv/MCNN.

MCNN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/MCNN](https://gitee.com/mindspore/models/blob/r1.6/official/cv/MCNN/README.md).

All parameters in the module are trainable.

## Citation

Yingying Zhang, Desen Zhou, Siqin Chen, Shenghua Gao, Yi Ma. Single-Image Crowd Counting via Multi-Column Convolutional Neural Network.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
