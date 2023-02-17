# efficientnet-b0

---

model-name: efficientnet-b0

backbone-name: efficientnet-b0

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: imagenet2012

evaluation: top1acc76.48 | top5acc93.08

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/efficientnet-b0>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/efficientnetb0_ascend_v1100_imagenet2012_research_cv_top1acc76.48_top5acc93.08.ckpt>
    asset-sha256: 729e24f509546b149120624ed7577274ba9ed26ba06d1a88e11989ac1c9df344

license: Apache2.0

summary: efficientnet-b0 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet-b0 from the MindSpore model zoo on Gitee at research/cv/efficientnet-b0.

efficientnet-b0 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/efficientnet-b0](https://gitee.com/mindspore/models/blob/r1.10/research/cv/efficientnet-b0/README_CN.md).

All parameters in the module are trainable.

## Citation

[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/pdf/1905.11946.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
