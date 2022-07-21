# c3d

---

model-name: c3d

backbone-name: c3d

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: ucf101

evaluation: top1acc79.51

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/c3d>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/c3d_ascend_v180_ucf101_official_cv_top1acc79.51.ckpt>
    asset-sha256: 44e707636ce4ada89ee1f97ce1fecbe1a0373b7dfe21a6d711c1db827676002f

license: Apache2.0

summary: c3d is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of c3d from the MindSpore model zoo on Gitee at official/cv/c3d.

c3d is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/c3d](https://gitee.com/mindspore/models/blob/r1.8/official/cv/c3d/README.md).

All parameters in the module are trainable.

## Citation

Learning Spatiotemporal Features with 3D Convolutional Networks

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
