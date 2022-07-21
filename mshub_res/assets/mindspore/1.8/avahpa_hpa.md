# AVA_hpa

---

model-name: AVA_hpa

backbone-name: AVA_hpa

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: hpa

evaluation: macroF1acc70.05 | microF1acc77.97 | auc94.23

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/AVA_hpa>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/avahpa_ascend_v180_hpa_research_cv_macroF1acc70.05_microF1acc77.97_auc94.23.ckpt>
    asset-sha256: 50d6c1d61a750a3524076c1088bda669d492713a6b8be9d71dd9c6b5e2656102

license: Apache2.0

summary: AVA_hpa is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of AVA_hpa from the MindSpore model zoo on Gitee at research/cv/AVA_hpa.

AVA_hpa is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/AVA_hpa](https://gitee.com/mindspore/models/blob/r1.8/research/cv/AVA_hpa/README.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
