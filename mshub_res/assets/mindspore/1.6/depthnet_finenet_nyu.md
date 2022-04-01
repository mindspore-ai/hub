# depthnet

---

model-name: depthnet

backbone-name: depthnet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: nyu

evaluation: delta1loss61.21 | delta2loss87.75 | delta3loss96.31 | absrelativeloss23.07 | sqrrelativeloss23.16 | rmselinearloss77.22 | rmselogloss27.36

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/depthnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/depthnet_finenet_ascend_v160_nyu_official_cv_delta1loss61.21_delta2loss87.75_delta3loss96.31_absrelativeloss23.07_sqrrelativeloss23.16_rmselinearloss77.22_rmselogloss27.36.ckpt>
    asset-sha256: b26f82f9bbff69ef9d0230814791f7ec8af371c1c8abc693154386c3347c78b4

license: Apache2.0

summary: depthnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of depthnet from the MindSpore model zoo on Gitee at official/cv/depthnet.

depthnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/depthnet](https://gitee.com/mindspore/models/blob/r1.6/official/cv/depthnet/README.md).

All parameters in the module are trainable.

## Citation

Depth Map Prediction from a Single Image using a Multi-Scale Deep Network. David Eigen, Christian Puhrsch, Rob Fergus.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
