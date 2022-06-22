# stpm

---

model-name: stpm

backbone-name: stpm

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: mvtecadhazelnut

evaluation: imagelevel100.0 | pixellevel98.81

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/stpm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/stpm_ascend_v170_mvtecadhazelnut_research_cv_imagelevel100.0_pixellevel98.81.ckpt>
    asset-sha256: 6ae5243a962b7335fe6f6a61368d61c574a204d6fd43325c50b350f1392a4d5c

license: Apache2.0

summary: stpm is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of stpm from the MindSpore model zoo on Gitee at research/cv/stpm.

stpm is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/stpm](https://gitee.com/mindspore/models/blob/r1.7/research/cv/stpm/README.md).

All parameters in the module are trainable.

## Citation

Wang G ,  Han S ,  Ding E , et al. Student-Teacher Feature Pyramid Matching for Unsupervised Anomaly Detection[J].  2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
