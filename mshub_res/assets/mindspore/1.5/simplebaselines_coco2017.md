# simple_baselines

---

model-name: simple_baselines

backbone-name: simple_baselines

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: coco2017

evaluation: acc72.3

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/simple_baselines>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/simplebaselines_ascend_v150_coco2017_research_cv_acc72.3.ckpt>
    asset-sha256: 31ad53e844b3a5301b8663e9b228c4eecdb904494ab605a1e9886f3956fbd00c

license: Apache2.0

summary: simple_baselines is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simple_baselines from the MindSpore model zoo on Gitee at research/cv/simple_baselines.

simple_baselines is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/simple_baselines](https://gitee.com/mindspore/models/blob/r1.5/research/cv/simple_baselines/README_CN.md).

All parameters in the module are trainable.

## Citation

Bin Xiao, Haiping Wu, Yichen Wei."Simple baselines for human pose estimation and tracking"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
