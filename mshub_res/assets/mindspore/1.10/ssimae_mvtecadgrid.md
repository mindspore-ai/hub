# ssim-ae

---

model-name: ssim-ae

backbone-name: ssim-ae

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: MVtecAD_grid

evaluation: ok94.7 | nok94.7 | avg96.2

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/ssim-ae>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/ssimae_ascend_v1100_mvtecadgrid_official_cv_ok94.7_nok94.7_avg96.2.ckpt>
    asset-sha256: 8822a030df8d90cab05c4e3b0dd4865e32bf907ffa82174857be6752eaaf0440

license: Apache2.0

summary: ssim-ae is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssim-ae from the MindSpore model zoo on Gitee at official/cv/ssim-ae.

ssim-ae is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/ssim-ae](https://gitee.com/mindspore/models/blob/r1.10/official/cv/ssim-ae/README_CN.md).

All parameters in the module are trainable.

## Citation

[Improving Unsupervised Defect Segmentation by Applying Structural Similarity to Autoencoders](https://arxiv.org/pdf/1807.02011v3.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
