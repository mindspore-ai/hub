# wdsr

---

model-name: wdsr

backbone-name: wdsr

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: div2k

evaluation: psnr35.35

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/wdsr>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/wdsr_ascend_v180_div2k_research_cv_psnr35.35.ckpt>
    asset-sha256: 2edcb77de7a0180158d2322f36454fa4a81701b1c9477f6380d8161a81a1e429

license: Apache2.0

summary: wdsr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wdsr from the MindSpore model zoo on Gitee at research/cv/wdsr.

wdsr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/wdsr](https://gitee.com/mindspore/models/blob/r1.8/research/cv/wdsr/README_CN.md).

All parameters in the module are trainable.

## Citation

1. Bee Lim, Sanghyun Son, Heewon Kim, Seungjun Nah, and Kyoung Mu Lee, "Enhanced Deep Residual Networks for Single Image Super-Resolution," *2nd NTIRE: New Trends in Image Restoration and Enhancement workshop and challenge on image super-resolution in conjunction with CVPR 2017.
2. Jiahui Yu, Yuchen Fan, Jianchao Yang, Ning Xu, Zhaowen Wang, Xinchao Wang, Thomas Huang, "Wide Activation for Efficient and Accurate Image Super-Resolution", arXiv preprint arXiv:1808.08718.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
