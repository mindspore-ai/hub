# PSPNet

---

model-name: PSPNet

backbone-name: PSPNet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: voc2012

evaluation: miou74.15 | allacc94.01

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/PSPNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/pspnet_ascend_v170_voc2012_research_cv_miou74.15_allacc94.01.ckpt>
    asset-sha256: 38ea9ed6abdeb1e3904df8d1a1fdb1690dfb5f41fca34bc3dd19fc9202cd1683

license: Apache2.0

summary: PSPNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of PSPNet from the MindSpore model zoo on Gitee at research/cv/PSPNet.

PSPNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/PSPNet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/PSPNet/README.md).

All parameters in the module are trainable.

## Citation

[paper](https://arxiv.org/abs/1612.01105) from CVPR2017

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
