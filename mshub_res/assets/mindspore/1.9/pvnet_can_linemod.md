# pvnet

---

model-name: pvnet

backbone-name: pvnet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: linemod

evaluation: 2Dprojection99.7 | add88.8

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/pvnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/pvnet_can_ascend_v190_linemod_official_cv_2Dprojection99.7_add88.8.ckpt>
    asset-sha256: 09a925f292a71174d5233bef059c445fb98f6d3e824413a301468931b0dce258

license: Apache2.0

summary: pvnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of pvnet from the MindSpore model zoo on Gitee at official/cv/pvnet.

pvnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/pvnet](https://gitee.com/mindspore/models/blob/r1.9/official/cv/pvnet/README.md).

All parameters in the module are trainable.

## Citation

Sida Peng, Y. Liu, Qixing Huang, Hujun Bao, Xiaowei Zhou."PVNet: Pixel-Wise Voting Network for 6DoF Pose Estimation."2018, 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
