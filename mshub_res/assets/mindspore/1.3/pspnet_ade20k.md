# PSPNet

---

model-name: PSPNet

backbone-name: PSPNet

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: ade20k

evaluation: miou41.57 | allacc79.71

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/PSPNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/pspnet_ascend_v130_ade20k_research_cv_miou41.57_allacc79.71.ckpt>
    asset-sha256: 2eacbc1c5b10f6bc5ca9b5c8ac3799c12a2b888ae66cf701ecf3e80ba3008d6f

license: Apache2.0

summary: PSPNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of PSPNet from the MindSpore model zoo on Gitee at research/cv/PSPNet.

PSPNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/PSPNet](https://gitee.com/mindspore/models/blob/r1.3/research/cv/PSPNet/README.md).

All parameters in the module are trainable.

## Citation

[paper](https://arxiv.org/abs/1612.01105) from CVPR2017

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
