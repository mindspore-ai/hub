# LightCNN

---

model-name: LightCNN

backbone-name: LightCNN

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: msceleb1m

evaluation: 100%-EER:98.73 | TRP@FAR=1%:98.53 | TRP@FAR=0.1%:95.6 | TRP@FAR=0%:83.6 | VR@FAR=0.1%:96.03 | DIR@FAR=1%:81.98

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/LightCNN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/lightcnn_ascend_v1100_msceleb1m_research_cv.ckpt>
    asset-sha256: ee35a8d90d29dfd8181f8a268491b6bf0d72953384306c738c3e999dd2034ac2

license: Apache2.0

summary: LightCNN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of LightCNN from the MindSpore model zoo on Gitee at research/cv/LightCNN.

LightCNN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/LightCNN](https://gitee.com/mindspore/models/blob/r1.10/research/cv/LightCNN/README_CN.md).

All parameters in the module are trainable.

## Citation

[A Light CNN for Deep Face Representation with Noisy Labels](https://arxiv.org/pdf/1511.02683.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
