# octsqueeze

---

model-name: octsqueeze

backbone-name: octsqueeze

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: kitti

evaluation: no

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/octsqueeze>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/octsqueeze_ascend_v160_kitti_official_cv.ckpt>
    asset-sha256: 1c6aac507575e41940aa4da2c4ee23fd19864b0081310ecd804df371c475aace

license: Apache2.0

summary: octsqueeze is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of octsqueeze from the MindSpore model zoo on Gitee at official/cv/octsqueeze.

octsqueeze is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/octsqueeze](https://gitee.com/mindspore/models/blob/r1.6/official/cv/octsqueeze/README.md).

All parameters in the module are trainable.

## Citation

Huang L, Wang S, Wong K, Liu J, Urtasun R. Octsqueeze: Octree-structured entropy model for lidar compression. InProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 2020

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
