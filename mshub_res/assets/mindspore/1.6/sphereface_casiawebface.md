# sphereface

---

model-name: sphereface

backbone-name: sphereface

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: casiawebface

evaluation: acc98.48

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/sphereface>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/sphereface_ascend_v160_casiawebface_official_cv_acc98.48.ckpt>
    asset-sha256: e81a805c60de07ab293fb14a3d59d393fd76198169263e35dcc99150c73089a3

license: Apache2.0

summary: sphereface is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of sphereface from the MindSpore model zoo on Gitee at official/cv/sphereface.

sphereface is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/sphereface](https://gitee.com/mindspore/models/blob/r1.6/official/cv/sphereface/README.md).

All parameters in the module are trainable.

## Citation

Weiyang Liu, Yandong Wen, Zhiding Yu, Ming Li, Bhiksha Raj, Le Song."SphereFace: Deep Hypersphere Embedding for Face Recognition."*Proceedings of the IEEE conference on computer vision and pattern recognition*.2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
