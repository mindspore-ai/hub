# FaceAttribute

---

model-name: FaceAttribute

backbone-name: FaceAttribute

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: fairface_rwmfd

evaluation: age49 | gender90 | mask99

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/FaceAttribute>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/faceattribute_ascend_v190_fairface_rwmfd_research_cv_age49_gender90_mask99.ckpt>
    asset-sha256: 6301d259829abf1fc2fcd1cf537b411ff6ab4aaf31fa9abf0d0160b7f08bde3c

license: Apache2.0

summary: FaceAttribute is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceAttribute from the MindSpore model zoo on Gitee at research/cv/FaceAttribute.

FaceAttribute is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/FaceAttribute](https://gitee.com/mindspore/models/blob/r1.9/research/cv/FaceAttribute/README.md).

All parameters in the module are trainable.

## Citation

[Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
