# ras

---

model-name: ras

backbone-name: ras

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: dutstrain

evaluation: ECSSD91 | DUTStest81 | DUTOMRON75 | HKUIS90

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/ras>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/ras_ascend_v130_dutstrain_research_cv_ECSSD91_DUTStest81_DUTOMRON75_HKUIS90.ckpt>
    asset-sha256: 01874ed4b95de1e7e08c304bbb8e1ef7158b6b9919f0217c8efdfe9b6c9eca5f

license: Apache2.0

summary: ras is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ras from the MindSpore model zoo on Gitee at research/cv/ras.

ras is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ras](https://gitee.com/mindspore/models/blob/r1.3/research/cv/ras/README.md).

All parameters in the module are trainable.

## Citation

Reverse Attention-Based Residual Network for Salient Object Detection

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
