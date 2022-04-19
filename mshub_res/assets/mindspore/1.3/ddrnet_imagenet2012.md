# DDRNet

---

model-name: DDRNet

backbone-name: DDRNet

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: imagenet2012

evaluation: top1acc76.36 | top5acc93.24

author: MindSpore team

update-time: 2022-04-18

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/DDRNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/ddrnet_ascend_v130_imagenet2012_research_cv_top1acc76.36_top5acc93.24.ckpt>
    asset-sha256: 6acbc32e242e674a61b812adfb1a7972348e013f0c8bd0beccaeca0446305997

license: Apache2.0

summary: DDRNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DDRNet from the MindSpore model zoo on Gitee at research/cv/DDRNet.

DDRNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DDRNet](https://gitee.com/mindspore/models/blob/r1.3/research/cv/DDRNet/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
