# PoseEstNet

---

model-name: PoseEstNet

backbone-name: PAMTRI

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: veir

evaluation: acc82.2

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/PAMTRI>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/poseestnet_ascend_v160_veir_research_cv_acc82.2.ckpt>
    asset-sha256: 34e7ca1eaccc6cbad0d3b150cddd80002c6ef5b7b54ca733f88c2e7bb3b585af

license: Apache2.0

summary: PAMTRI is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of PAMTRI from the MindSpore model zoo on Gitee at research/cv/PAMTRI.

PAMTRI is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/PAMTRI](https://gitee.com/mindspore/models/blob/r1.6/research/cv/PAMTRI/README.md).

All parameters in the module are trainable.

## Citation

Tang Z ,  Naphade M ,  Birchfield S , et al. PAMTRI: Pose-Aware Multi-Task Learning for Vehicle Re-Identification Using Highly Randomized Synthetic Data[J]. IEEE, 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
