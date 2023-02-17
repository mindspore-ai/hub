# HRNetW48_seg

---

model-name: HRNetW48_seg

backbone-name: HRNetW48_seg

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: cityscapes

evaluation: miou79.21

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/HRNetW48_seg>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/hrnetw48seg_ascend_v1100_cityscapes_research_cv_miou79.21.ckpt>
    asset-sha256: e36e05b484f8be0e4477261703853750205c38f7eb7cb1c034c990d360531e22

license: Apache2.0

summary: HRNetW48_seg is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of HRNetW48_seg from the MindSpore model zoo on Gitee at research/cv/HRNetW48_seg.

HRNetW48_seg is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/HRNetW48_seg](https://gitee.com/mindspore/models/blob/r1.10/research/cv/HRNetW48_seg/README_CN.md).

All parameters in the module are trainable.

## Citation

[High-Resolution Representations for Labeling Pixels and Regions](https://arxiv.org/pdf/1904.04514.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
