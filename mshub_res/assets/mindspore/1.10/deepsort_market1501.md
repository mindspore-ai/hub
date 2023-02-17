# Deepsort

---

model-name: Deepsort

backbone-name: Deepsort

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: market1501

evaluation: MOTA51.8 | MOTP0.189 | MT210 | ML68 | IDs859 | FM1388 | FP19264 | FN33114

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/Deepsort>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/deepsort_ascend_v1100_market1501_official_cv_MOTA51.8_MOTP0.189_MT210_ML68_IDs859_FM1388_FP19264_FN33114.ckpt>
    asset-sha256: dc6c1db2b07eb12a59feb1727f7e1c0e2a4e4c7e8b441cdd26234e53912ae781

license: Apache2.0

summary: Deepsort is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Deepsort from the MindSpore model zoo on Gitee at official/cv/Deepsort.

Deepsort is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/Deepsort](https://gitee.com/mindspore/models/blob/r1.10/official/cv/Deepsort/README_CN.md).

All parameters in the module are trainable.

## Citation

[Simple Online and Realtime Tracking](https://arxiv.org/pdf/1602.00763.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
