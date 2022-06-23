# vnet

---

model-name: vnet

backbone-name: vnet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: promise2012

evaluation: dice85 | hausdorffdistance10

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/vnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/vnet_ascend_v170_promise2012_research_cv_dice85_hausdorffdistance10.ckpt>
    asset-sha256: 6afc96e827a5ced76fbe95f93f02dbfea6be024d3261eb4f335e1897b07c8ad9

license: Apache2.0

summary: vnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vnet from the MindSpore model zoo on Gitee at research/cv/vnet.

vnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/vnet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/vnet/README_CN.md).

All parameters in the module are trainable.

## Citation

F Milletari, Navab N, Ahmadi S A. V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation[C]// 2016 Fourth International Conference on 3D Vision (3DV). IEEE, 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
