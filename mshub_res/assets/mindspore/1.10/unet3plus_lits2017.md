# UNet3+

---

model-name: UNet3+

backbone-name: UNet3+

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: lits2017

evaluation: acc97.7

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/UNet3+>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/unet3plus_ascend_v1100_lits2017_research_cv_acc97.7.ckpt>
    asset-sha256: bcad7cb89d81da57d53b49928f6d0af96bb5d26552170bc4900402b8171d02b0

license: Apache2.0

summary: UNet3+ is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of UNet3+ from the MindSpore model zoo on Gitee at research/cv/UNet3+.

UNet3+ is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/UNet3+](https://gitee.com/mindspore/models/blob/r1.10/research/cv/UNet3+/README_CN.md).

All parameters in the module are trainable.

## Citation

[UNet 3+: A Full-Scale Connected UNet for Medical Image Segmentation](https://arxiv.org/pdf/2004.08790.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
