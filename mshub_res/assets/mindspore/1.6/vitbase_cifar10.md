# vit_base

---

model-name: vit_base

backbone-name: vit_base

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: cifar10

evaluation: acc98.71

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/vit_base>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/vitbase_ascend_v160_cifar10_research_cv_acc98.71.ckpt>
    asset-sha256: 86646358bde1d63ce8a073ea0543f3cea94e95e1752ea621cb3c66a4b101a678

license: Apache2.0

summary: vit_base is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vit_base from the MindSpore model zoo on Gitee at research/cv/vit_base.

vit_base is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/vit_base](https://gitee.com/mindspore/models/blob/r1.6/research/cv/vit_base/README_CN.md).

All parameters in the module are trainable.

## Citation

Dosovitskiy, A. , Beyer, L. , Kolesnikov, A. , Weissenborn, D. , & Houlsby, N.. (2020). An image is worth 16x16 words: transformers for image recognition at scale.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
