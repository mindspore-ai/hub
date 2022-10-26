# ResnetV2_101

---

model-name: ResnetV2_101

backbone-name: resnetv2

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cifar10

evaluation: top1acc94.86 | top5acc99.8

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/resnetv2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/resnetv2101_ascend_v190_cifar10_research_cv_top1acc94.86_top5acc99.8.ckpt>
    asset-sha256: 48fef93340bf450fb7d22e056b1cdcd0b2a3487ca7ffac11485fbcfce5c459bd

license: Apache2.0

summary: resnetv2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnetv2 from the MindSpore model zoo on Gitee at research/cv/resnetv2.

resnetv2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/resnetv2](https://gitee.com/mindspore/models/blob/r1.9/research/cv/resnetv2/README_CN.md).

All parameters in the module are trainable.

## Citation

[Identity Mappings in Deep Residual Networks](https://arxiv.org/pdf/1603.05027.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
