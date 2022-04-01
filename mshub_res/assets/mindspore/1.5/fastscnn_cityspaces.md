# fastscnn

---

model-name: fastscnn

backbone-name: fastscnn

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: cityspaces

evaluation: acc54

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/fastscnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/fastscnn_ascend_v150_cityspaces_official_cv_acc54.ckpt>
    asset-sha256: 74f4e5fb01d4ae9384fa9cd5da5f92fbc804cade3c8d0df608f41998af0e1889

license: Apache2.0

summary: fastscnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of fastscnn from the MindSpore model zoo on Gitee at official/cv/fastscnn.

fastscnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/fastscnn](https://gitee.com/mindspore/models/blob/r1.5/official/cv/fastscnn/README_CN.md).

All parameters in the module are trainable.

## Citation

Poudel R , Liwicki S , Cipolla R . Fast-SCNN: Fast Semantic Segmentation Network[J]. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
