# east

---

model-name: east

backbone-name: east

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: icdar2015

evaluation: acc81.25

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/cv/east>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/east_ascend_v170_icdar2015_official_cv_acc81.25.ckpt>
    asset-sha256: 4fa8a1a81a9d49db853cb483b2763e06219726158a8db96dcccbcd36d5d9ee52

license: Apache2.0

summary: east is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of east from the MindSpore model zoo on Gitee at official/cv/east.

east is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/east](https://gitee.com/mindspore/models/blob/r1.7/official/cv/east/README.md).

All parameters in the module are trainable.

## Citation

Xinyu Zhou, Cong Yao, He Wen, Yuzhi Wang, Shuchang Zhou, Weiran He, and Jiajun Liang Megvii Technology Inc., Beijing, China, Published in CVPR 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
