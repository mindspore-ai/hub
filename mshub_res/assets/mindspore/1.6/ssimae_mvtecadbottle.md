# ssim-ae

---

model-name: ssim-ae

backbone-name: ssim-ae

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: mvtecadbottle

evaluation: ok98.4 | nok98.4 | avg96.4

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/ssim-ae>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/ssimae_ascend_v160_mvtecadbottle_official_cv_ok98.4_nok98.4_avg96.4.ckpt>
    asset-sha256: af7c607f44ddb8a921a72538308b071416da2d3639121e12bcd0b5725c9fce30

license: Apache2.0

summary: ssim-ae is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssim-ae from the MindSpore model zoo on Gitee at official/cv/ssim-ae.

ssim-ae is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/ssim-ae](https://gitee.com/mindspore/models/blob/r1.6/official/cv/ssim-ae/README_CN.md).

All parameters in the module are trainable.

## Citation

Improving Unsupervised Defect Segmentation by Applying Structural Similarity To Autoencoders

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
