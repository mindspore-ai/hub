# 3D_DenseNet

---

model-name: 3D_DenseNet

backbone-name: 3D_DenseNet

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: iseg2017

evaluation: acc92

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/3D_DenseNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/3ddensenet_ascend_v1100_iseg2017_research_cv_acc92.ckpt>
    asset-sha256: 81196ef44f3db51e3d22b69d01373c162639fa31362dd71388906fc307ccc3fe

license: Apache2.0

summary: 3D_DenseNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of 3D_DenseNet from the MindSpore model zoo on Gitee at research/cv/3D_DenseNet.

3D_DenseNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/3D_DenseNet](https://gitee.com/mindspore/models/blob/r1.10/research/cv/3D_DenseNet/README.md).

All parameters in the module are trainable.

## Citation

[Skip-connected 3D DenseNet for volumetric infant brain MRI segmentation](https://www.sciencedirect.com/science/article/abs/pii/S1746809419301946)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
