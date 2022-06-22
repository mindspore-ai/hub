# PDarts

---

model-name: PDarts

backbone-name: PDarts

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: cifar10

evaluation: top1acc96.81

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/PDarts>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/pdarts_ascend_v170_cifar10_research_cv_top1acc96.81.ckpt>
    asset-sha256: 3ac3efa85294f28763a69859e0812f16f8006261dbbc9cd42a9ed0b0589e0fdc

license: Apache2.0

summary: PDarts is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of PDarts from the MindSpore model zoo on Gitee at research/cv/PDarts.

PDarts is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/PDarts](https://gitee.com/mindspore/models/blob/r1.7/research/cv/PDarts/README_CN.md).

All parameters in the module are trainable.

## Citation

https://arxiv.org/pdf/1904.12760.pdf

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
