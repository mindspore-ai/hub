# vnet

---

model-name: vnet

backbone-name: vnet

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: PROMISE 2012

evaluation: AvgDice87.49 | AvgHausdorffDistance10.54

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/vnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/vnet_ascend_v1100_promise2012_research_cv_AvgDice87.49_AvgHausdorffDistance10.54.ckpt>
    asset-sha256: 68654d1382eade1ebc6cbb70347c5448d4c9895bbf015dadbc781633c352233c

license: Apache2.0

summary: vnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vnet from the MindSpore model zoo on Gitee at research/cv/vnet.

vnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/vnet](https://gitee.com/mindspore/models/blob/r1.10/research/cv/vnet/README_CN.md).

All parameters in the module are trainable.

## Citation

[V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation](https://arxiv.org/pdf/1606.04797.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
