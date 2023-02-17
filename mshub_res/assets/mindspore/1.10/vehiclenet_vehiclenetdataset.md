# VehicleNet

---

model-name: VehicleNet

backbone-name: VehicleNet

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: vehiclenetdataset

evaluation: mAP83.71 | rank1acc94.34

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/VehicleNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/vehiclenet_ascend_v1100_vehiclenetdataset_research_cv_mAP83.71_rank1acc94.34.ckpt>
    asset-sha256: e38499b0dbc409d74bfd266533b7d3c3f0ee020811fb3bf6c60869c82eb36028

license: Apache2.0

summary: VehicleNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of VehicleNet from the MindSpore model zoo on Gitee at research/cv/VehicleNet.

VehicleNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/VehicleNet](https://gitee.com/mindspore/models/blob/r1.10/research/cv/VehicleNet/README_CN.md).

All parameters in the module are trainable.

## Citation

[VehicleNet: Learning Robust Visual Representation for Vehicle Re-identification](https://arxiv.org/pdf/2004.06305.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
