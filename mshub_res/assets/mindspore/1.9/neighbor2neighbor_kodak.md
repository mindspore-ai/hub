# Neighbor2Neighbor

---

model-name: Neighbor2Neighbor

backbone-name: Neighbor2Neighbor

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: kodak

evaluation: PSNR32.0 | SSIM0.875

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/Neighbor2Neighbor>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/neighbor2neighbor_ascend_v190_kodak_research_cv_PSNR32.0_SSIM0.875.ckpt>
    asset-sha256: d99d97edf7e4d2544294da536e2b38d920aa67fec7697c5671d734c063bf7704

license: Apache2.0

summary: Neighbor2Neighbor is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Neighbor2Neighbor from the MindSpore model zoo on Gitee at research/cv/Neighbor2Neighbor.

Neighbor2Neighbor is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Neighbor2Neighbor](https://gitee.com/mindspore/models/blob/r1.9/research/cv/Neighbor2Neighbor/README_CN.md).

All parameters in the module are trainable.

## Citation

Huang T , Li S , Jia X , et al. Neighbor2Neighbor: Self-Supervised Denoising from Single Noisy Images[J]. 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
