# slowfast

---

model-name: slowfast

backbone-name: slowfast

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: ava2.2

evaluation: acc21.93

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/slowfast>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/slowfast_ascend_v1100_ava_research_cv_acc21.93.ckpt>
    asset-sha256: 6dda0a7a32ed1a21621e7793f4d7e2cd40b158b510ec4bc7f6f73a71e13e8aa9

license: Apache2.0

summary: slowfast is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of slowfast from the MindSpore model zoo on Gitee at research/cv/slowfast.

slowfast is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/slowfast](https://gitee.com/mindspore/models/blob/r1.10/research/cv/slowfast/README.md).

All parameters in the module are trainable.

## Citation

[SlowFast Networks for Video Recognition](https://arxiv.org/pdf/1812.03982.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
