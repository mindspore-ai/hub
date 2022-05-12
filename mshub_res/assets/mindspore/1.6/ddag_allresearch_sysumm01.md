# DDAG

---

model-name: DDAG

backbone-name: DDAG

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: sysumm01

evaluation: rank1acc53.99 | mAP52.17

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/DDAG>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/ddag_allresearch_ascend_v160_sysumm01_research_cv_rank1acc53.99_mAP52.17.ckpt>
    asset-sha256: 5851f957f62a2b28a980d0cfc6bcfd5d565d646e5af35798140cc5f310981a02

license: Apache2.0

summary: DDAG is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DDAG from the MindSpore model zoo on Gitee at research/cv/DDAG.

DDAG is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DDAG](https://gitee.com/mindspore/models/blob/r1.6/research/cv/DDAG/README.md).

All parameters in the module are trainable.

## Citation

*Dynamic Dual-Attentive Aggregation Learning for Visible-Infrared Person Re-Identification* in ECCV 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
