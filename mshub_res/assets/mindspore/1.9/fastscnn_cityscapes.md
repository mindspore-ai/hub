# fastscnn

---

model-name: fastscnn

backbone-name: fastscnn

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cityscapes

evaluation: mIoU54.84

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/fastscnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fastscnn_ascend_v190_cityscapes_official_cv_mIoU54.84.ckpt>
    asset-sha256: 4529bc0f99b9c689a4ea097711374d1bf7d9146714d0042b8592575c71415139

license: Apache2.0

summary: fastscnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of fastscnn from the MindSpore model zoo on Gitee at official/cv/fastscnn.

fastscnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/fastscnn](https://gitee.com/mindspore/models/blob/r1.9/official/cv/fastscnn/README_CN.md).

All parameters in the module are trainable.

## Citation

[Fast-SCNN: Fast Semantic Segmentation Network](https://arxiv.org/pdf/1902.04502.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
