# simclr

---

model-name: simclr

backbone-name: simclr

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: cifar10

evaluation: acc84.88

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/simclr>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/simclr_linearclassifier_ascend_v180_cifar10_official_cv_acc84.88.ckpt>
    asset-sha256: 9ce1b950db3edd388a5eeea42bb471de6baa3a3899749366119821bfd57d28c6

license: Apache2.0

summary: simclr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simclr from the MindSpore model zoo on Gitee at official/cv/simclr.

simclr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/simclr](https://gitee.com/mindspore/models/blob/r1.8/official/cv/simclr/README.md).

All parameters in the module are trainable.

## Citation

Ting Chen and Simon Kornblith and Mohammad Norouzi and Geoffrey Hinton. A Simple Framework for Contrastive Learning of Visual Representations. *arXiv preprint arXiv:2002.05709*. 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
