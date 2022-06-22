# dlinknet

---

model-name: dlinknet

backbone-name: dlinknet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: DeepGlobeRoadExtractionDataset

evaluation: acc98.14 | acccls89.39 | iou98.08

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/dlinknet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/dlinknet_ascend_v170_DeepGlobeRoadExtractionDataset_research_cv_acc98.14_acccls89.39_iou98.08.ckpt>
    asset-sha256: 102594a59fdc3d53c44aa2bd5573ca5a38a77697c2c7016221917b8f21e9834d

license: Apache2.0

summary: dlinknet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of dlinknet from the MindSpore model zoo on Gitee at research/cv/dlinknet.

dlinknet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/dlinknet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/dlinknet/README.md).

All parameters in the module are trainable.

## Citation

chen Zhou, Chuang Zhang, Ming Wu; Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, 2018, pp. 182-186

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
