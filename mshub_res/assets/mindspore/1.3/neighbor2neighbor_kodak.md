# Neighbor2Neighbor

---

model-name: Neighbor2Neighbor

backbone-name: Neighbor2Neighbor

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: kodak

evaluation: PSNR32 | SSIM0.883

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/Neighbor2Neighbor>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/neighbor2neighbor_ascend_v130_kodak_research_cv_PSNR32_SSIM0.883.ckpt>
    asset-sha256: 6cfd9d193826c3a0c4d95fd5633171d438e28d1b4607c388434142ab161ee1cb

license: Apache2.0

summary: Neighbor2Neighbor is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Neighbor2Neighbor from the MindSpore model zoo on Gitee at research/cv/Neighbor2Neighbor.

Neighbor2Neighbor is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Neighbor2Neighbor](https://gitee.com/mindspore/models/blob/r1.3/research/cv/Neighbor2Neighbor/README_CN.md).

All parameters in the module are trainable.

## Citation

Huang T , Li S , Jia X , et al. Neighbor2Neighbor: Self-Supervised Denoising from Single Noisy Images[J]. 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
