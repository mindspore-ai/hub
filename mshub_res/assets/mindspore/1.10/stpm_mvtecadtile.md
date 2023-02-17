# stpm

---

model-name: stpm

backbone-name: stpm

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: MVtecAD_tile

evaluation: image-level98.67 | pixel-level95.76

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/stpm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/stpm_ascend_v1100_mvtecadtile_research_cv_image-level98.67_pixel-level95.76.ckpt>
    asset-sha256: 6d47e6f1f857f7e2f987c5981bc2b2d6e092849125c0fd4247fbffbb584d59dd

license: Apache2.0

summary: stpm is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of stpm from the MindSpore model zoo on Gitee at research/cv/stpm.

stpm is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/stpm](https://gitee.com/mindspore/models/blob/r1.10/research/cv/stpm/README.md).

All parameters in the module are trainable.

## Citation

[Student-Teacher Feature Pyramid Matching for Unsupervised Anomaly Detection](https://arxiv.org/pdf/2103.04257v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
