# ADNet

---

model-name: ADNet

backbone-name: ADNet

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: vot2013vot2014

evaluation: acc70

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/ADNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/adnet_ascend_v130_vot2013vot2014_official_cv_acc70.ckpt>
    asset-sha256: a0c20d71945406fe3687d30a5f4d4011dd8eb7f846ca3d00ec2e0ea60324311e

license: Apache2.0

summary: ADNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ADNet from the MindSpore model zoo on Gitee at official/cv/ADNet.

ADNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/ADNet](https://gitee.com/mindspore/models/blob/r1.3/official/cv/ADNet/README_CN.md).

All parameters in the module are trainable.

## Citation

Sangdoo Yun（Seoul National University, South Korea）. "Action-Decision Networks for Visual Tracking with Deep Reinforcement Learning'. Presented at CVPR 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
