# ICNet

---

model-name: ICNet

backbone-name: ICNet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: cityscapes

evaluation: avgmiou69.4

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/ICNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/icnet_ascend_v170_cityscapes_research_cv_avgmiou69.4.ckpt>
    asset-sha256: 2a16822fefb0627b455c73a57321a9da24e2483b11487e173bcdc6c07841d867

license: Apache2.0

summary: ICNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ICNet from the MindSpore model zoo on Gitee at research/cv/ICNet.

ICNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ICNet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/ICNet/README.md).

All parameters in the module are trainable.

## Citation

[paper](https://arxiv.org/abs/1704.08545) from ECCV2018

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
