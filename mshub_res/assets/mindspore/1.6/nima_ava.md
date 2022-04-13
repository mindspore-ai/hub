# nima

---

model-name: nima

backbone-name: nima

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: ava

evaluation: SRCC72

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/nima>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/nima_ascend_v160_ava_official_cv_SRCC72.ckpt>
    asset-sha256: 8bffc3b6182d3ae4e4c3e0375f939f857ae8a651a81ab06f136d467a4f0fc5eb

license: Apache2.0

summary: nima is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of nima from the MindSpore model zoo on Gitee at official/cv/nima.

nima is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/nima](https://gitee.com/mindspore/models/blob/r1.6/official/cv/nima/README.md).

All parameters in the module are trainable.

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun."Deep Residual Learning for Image Recognition"
2. H. Talebi and P. Milanfar, "NIMA: Neural Image Assessment"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
