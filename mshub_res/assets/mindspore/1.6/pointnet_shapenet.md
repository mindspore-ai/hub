# pointnet

---

model-name: pointnet

backbone-name: pointnet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: shapenet

evaluation: acc86.96

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/pointnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/pointnet_ascend_v160_shapenet_research_cv_acc86.96.ckpt>
    asset-sha256: 5ec22ef8af05c86a4e2c69db7da097c8d2d337455ad42065e54dcc1ada9b77ed

license: Apache2.0

summary: pointnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of pointnet from the MindSpore model zoo on Gitee at research/cv/pointnet.

pointnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/pointnet](https://gitee.com/mindspore/models/blob/r1.6/research/cv/pointnet/README.md).

All parameters in the module are trainable.

## Citation

Qi, Charles R., et al. "PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation" arXiv preprint arXiv:1612.00593 (2017).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
