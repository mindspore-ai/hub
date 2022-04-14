# STGAN

---

model-name: STGAN

backbone-name: STGAN

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: celeba

evaluation: -

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/STGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/stgan_ascend_v150_celeba_research_cv.ckpt>
    asset-sha256: c73ce0878942c2b753f9c028c2d1bf000bb56af6fcfb45b70b62195016bc96be

license: Apache2.0

summary: STGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of STGAN from the MindSpore model zoo on Gitee at research/cv/STGAN.

STGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/STGAN](https://gitee.com/mindspore/models/blob/r1.5/research/cv/STGAN/README.md).

All parameters in the module are trainable.

## Citation

Liu M, Ding Y, Xia M, et al. STGAN: A Unified Selective Transfer Network for Arbitrary Image Attribute Editing[C]. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, 2019: 3668-3677.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
