# OCRNet

---

model-name: OCRNet

backbone-name: OCRNet

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: cityscapes

evaluation: mIoU81.0

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/OCRNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/ocrnet_ascend_v1100_cityscapes_research_cv_mIoU81.0.ckpt>
    asset-sha256: 7c48865ecfd4a2f8387514359f22a20f9268644b4b728673d6890ce0c7ec3c6b

license: Apache2.0

summary: OCRNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of OCRNet from the MindSpore model zoo on Gitee at research/cv/OCRNet.

OCRNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/OCRNet](https://gitee.com/mindspore/models/blob/r1.10/research/cv/OCRNet/README_CN.md).

All parameters in the module are trainable.

## Citation

[Segmentation Transformer: Object-Contextual Representations for Semantic Segmentation](https://arxiv.org/pdf/1909.11065.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
