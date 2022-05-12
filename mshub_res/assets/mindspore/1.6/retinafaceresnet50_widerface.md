# retinaface

---

model-name: retinaface

backbone-name: retinaface

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: widerface

evaluation: easy94.89 | medium93.36 | hard84.13

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/retinaface>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/retinafaceresnet50_ascend_v160_widerface_research_cv_easy94.89_medium93.36_hard84.13.ckpt>
    asset-sha256: 95d218806b032412451a7e7fd1982c59a80be42d7926020e6e4f0e561b0d7b1f

license: Apache2.0

summary: retinaface is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of retinaface from the MindSpore model zoo on Gitee at research/cv/retinaface.

retinaface is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/retinaface](https://gitee.com/mindspore/models/blob/r1.6/research/cv/retinaface/README_CN.md).

All parameters in the module are trainable.

## Citation

Jiankang Deng, Jia Guo, Yuxiang Zhou, Jinke Yu, Irene Kotsia, Stefanos Zafeiriou. "RetinaFace: Single-stage Dense Face Localisation in the Wild". 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
