# posenet

---

model-name: posenet

backbone-name: posenet

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: kingscollege

evaluation: 2.2m | 3.44d

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/posenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/posenet_ascend_v1100_kingscollege_official_cv_2.2m_3.44d.ckpt>
    asset-sha256: d882ceb3f8dc68db7064732e3a0da7b6c37766e054cf7ad60c049aef987331cc

license: Apache2.0

summary: posenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of posenet from the MindSpore model zoo on Gitee at official/cv/posenet.

posenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/posenet](https://gitee.com/mindspore/models/blob/r1.10/official/cv/posenet/README_CN.md).

All parameters in the module are trainable.

## Citation

[PoseNet: A Convolutional Network for Real-Time 6-DOF Camera Relocalization](https://arxiv.org/pdf/1505.07427.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
