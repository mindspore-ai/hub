# RCAN

---

model-name: RCAN

backbone-name: RCAN

module-type: cv-super_resolution

fine-tunable: True

model-version: 1.8

train-dataset: DIV2K

evaluation: PSNR38.26 | SSIM0.9614

author: MindSpore team

update-time: 2022-08-08

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/RCAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/rcan_ascend_v180_div2k_research_cv_PSNR38.26_SSIM0.9614.ckpt>
    asset-sha256: f75418c61a5daa58c3e3499ad0551033bf3a1cce217054c7e01ab42615977286

license: Apache2.0

summary: RCAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of RCAN from the MindSpore model zoo on Gitee at research/cv/RCAN.

RCAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/RCAN](https://gitee.com/mindspore/models/blob/r1.8/research/cv/RCAN/README.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
