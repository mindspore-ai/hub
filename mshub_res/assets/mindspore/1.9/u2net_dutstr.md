# u2net

---

model-name: u2net

backbone-name: u2net

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: dutstr

evaluation: acc99.05

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/u2net>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/u2net_ascend_v190_dutstr_research_cv_acc99.05.ckpt>
    asset-sha256: c3a725b159817161fc3dfd9d4a6758e3cda530ea0927be8d908262be3a88e86c

license: Apache2.0

summary: u2net is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of u2net from the MindSpore model zoo on Gitee at research/cv/u2net.

u2net is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/u2net](https://gitee.com/mindspore/models/blob/r1.9/research/cv/u2net/README.md).

All parameters in the module are trainable.

## Citation

[U2-Net: Going Deeper with Nested U-Structure for Salient Object Detection](https://arxiv.org/pdf/2005.09007.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
