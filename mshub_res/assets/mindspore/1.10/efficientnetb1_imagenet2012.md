# efficientnet-b1

---

model-name: efficientnet-b1

backbone-name: efficientnet-b1

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: ImageNet2012

evaluation: top1acc77.9 | top5acc93.93

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/efficientnet-b1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/efficientnetb1_ascend_v1100_imagenet2012_research_cv_top1acc77.9_top5acc93.93.ckpt>
    asset-sha256: 1cebde63145b7ea7f6685827e2db81160a4f8b0e174a11032e0a82244e25660f

license: Apache2.0

summary: efficientnet-b1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet-b1 from the MindSpore model zoo on Gitee at research/cv/efficientnet-b1.

efficientnet-b1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/efficientnet-b1](https://gitee.com/mindspore/models/blob/r1.10/research/cv/efficientnet-b1/README_CN.md).

All parameters in the module are trainable.

## Citation

[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/pdf/1905.11946.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
