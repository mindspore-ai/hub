# renas

---

model-name: renas

backbone-name: renas

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: cifar10

evaluation: acc94.1

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/renas>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/renas_ascend_v180_cifar10_research_cv_acc94.1.ckpt>
    asset-sha256: 5d5add9adef4f3792facb6d018a2905986c6381a61a97c5be049e5936a125e5f

license: Apache2.0

summary: renas is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of renas from the MindSpore model zoo on Gitee at research/cv/renas.

renas is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/renas](https://gitee.com/mindspore/models/blob/r1.8/research/cv/renas/Readme.md).

All parameters in the module are trainable.

## Citation

Yixing Xu, Yunhe Wang, Kai Han, Yehui Tang, Shangling Jui, Chunjing Xu, Chang Xu. ReNAS: Relativistic Evaluation of Neural Architecture Search. Submitted to CVPR 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
