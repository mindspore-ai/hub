# wdsr

---

model-name: wdsr

backbone-name: wdsr

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: DIV2K

evaluation: PSNR33.62

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/wdsr>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/wdsr_ascend_v1100_div2k_research_cv_PSNR33.62.ckpt>
    asset-sha256: 5afacb5bbd78341033284d7c9453b881c0732c13c711edc99c469f9d0a96f65a

license: Apache2.0

summary: wdsr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wdsr from the MindSpore model zoo on Gitee at research/cv/wdsr.

wdsr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/wdsr](https://gitee.com/mindspore/models/blob/r1.10/research/cv/wdsr/README_CN.md).

All parameters in the module are trainable.

## Citation

1. [Enhanced Deep Residual Networks for Single Image Super-Resolution](https://arxiv.org/pdf/1707.02921.pdf)
2. [Wide Activation for Efficient and Accurate Image Super-Resolution](https://arxiv.org/pdf/1808.08718.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
