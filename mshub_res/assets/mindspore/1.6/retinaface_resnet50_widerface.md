# retinaface_resnet50

---

model-name: retinaface_resnet50

backbone-name: retinaface_resnet50

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: widerface

evaluation: easy94.97 | medium93.89 | hard82.27

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/retinaface_resnet50>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/retinaface_resnet50_ascend_v160_widerface_official_cv_easy94.97_medium93.89_hard82.27.ckpt>
    asset-sha256: d7a67c8289bec78788b5ab625f006b8d74992c77c25310ec5a9dd0e16722e2aa

license: Apache2.0

summary: retinaface_resnet50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of retinaface_resnet50 from the MindSpore model zoo on Gitee at official/cv/retinaface_resnet50.

retinaface_resnet50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/retinaface_resnet50](https://gitee.com/mindspore/models/blob/r1.6/official/cv/retinaface_resnet50/README.md).

All parameters in the module are trainable.

## Citation

Jiankang Deng, Jia Guo, Yuxiang Zhou, Jinke Yu, Irene Kotsia, Stefanos Zafeiriou. "RetinaFace: Single-stage Dense Face Localisation in the Wild". 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
