# TCN

---

model-name: TCN

backbone-name: TCN

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: addingproblem

evaluation: acc1.72e-05

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/TCN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/tcn_ascend_v160_addingproblem_research_cv_acc1.72e-05.ckpt>
    asset-sha256: 5c84192038bee4aeb986576803a28a0807e5bdd58c9a4fb1bac7a1506c6e06c3

license: Apache2.0

summary: TCN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of TCN from the MindSpore model zoo on Gitee at research/cv/TCN.

TCN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/TCN](https://gitee.com/mindspore/models/blob/r1.6/research/cv/TCN/README.md).

All parameters in the module are trainable.

## Citation

An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
