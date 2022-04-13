# relationnet

---

model-name: relationnet

backbone-name: relationnet

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: omniglot

evaluation: acc99.08

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/relationnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/relationnet_ascend_v150_omniglot_research_cv_acc99.08.ckpt>
    asset-sha256: b0a2b8a3864b71c719e63f7de3760cff36f75e456991c35371cea6ed0525179d

license: Apache2.0

summary: relationnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of relationnet from the MindSpore model zoo on Gitee at research/cv/relationnet.

relationnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/relationnet](https://gitee.com/mindspore/models/blob/r1.5/research/cv/relationnet/README.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
