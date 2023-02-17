# nas-fpn

---

model-name: nas-fpn

backbone-name: nas-fpn

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: coco2017

evaluation: mAP41.6

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/nas-fpn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/nasfpn_ascend_v1100_coco2017_research_cv_mAP41.6.ckpt>
    asset-sha256: 9f3d48be6e6e2aab0b908bc7d18b1dc4912ebc267d58c4f64992a9a387f9c539

license: Apache2.0

summary: nas-fpn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of nas-fpn from the MindSpore model zoo on Gitee at research/cv/nas-fpn.

nas-fpn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/nas-fpn](https://gitee.com/mindspore/models/blob/r1.10/research/cv/nas-fpn/README_CN.md).

All parameters in the module are trainable.

## Citation

[NAS-FPN: Learning Scalable Feature Pyramid Architecture for Object Detection](https://arxiv.org/pdf/1904.07392.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
