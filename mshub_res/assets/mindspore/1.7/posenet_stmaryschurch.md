# posenet

---

model-name: posenet

backbone-name: posenet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: stmaryschurch

evaluation: 2.0m | 5.93d

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/cv/posenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/posenet_ascend_v170_stmaryschurch_official_cv_2.0m_5.93d.ckpt>
    asset-sha256: ae1db1bd49928839b6c295fbe50115ca43860c02c46b0542103e66a944c44e33

license: Apache2.0

summary: posenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of posenet from the MindSpore model zoo on Gitee at official/cv/posenet.

posenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/posenet](https://gitee.com/mindspore/models/blob/r1.7/official/cv/posenet/README_CN.md).

All parameters in the module are trainable.

## Citation

Kendall A, Grimes M, Cipolla R. "PoseNet: A convolutional network for real-time 6-dof camera relocalization."*In IEEE International Conference on Computer Vision (pp. 2938–2946), 2015.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
