# stpm

---

model-name: stpm

backbone-name: stpm

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: mvtecadtoothbrush

evaluation: imagelevel93.06 | pixellevel98.62

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/stpm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/stpm_ascend_v180_mvtecadtoothbrush_research_cv_imagelevel93.06_pixellevel98.62.ckpt>
    asset-sha256: 36bbf1cdf2ae91b923a0e1697bfdc227a67a57d2d5b47523087c72950f1046a2

license: Apache2.0

summary: stpm is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of stpm from the MindSpore model zoo on Gitee at research/cv/stpm.

stpm is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/stpm](https://gitee.com/mindspore/models/blob/r1.8/research/cv/stpm/README.md).

All parameters in the module are trainable.

## Citation

Wang G ,  Han S ,  Ding E , et al. Student-Teacher Feature Pyramid Matching for Unsupervised Anomaly Detection[J].  2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
