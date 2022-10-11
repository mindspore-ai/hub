# efficientnet-b2

---

model-name: efficientnet-b2

backbone-name: efficientnet-b2

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc79.66 | top5acc94.82

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/efficientnet-b2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/efficientnetb2_ascend_v190_imagenet2012_research_cv_top1acc79.66_top5acc94.82.ckpt>
    asset-sha256: 717dd4ed2df8eb2b549649c4d69bbfb66f2876cc5ea11617557527a67ce49a33

license: Apache2.0

summary: efficientnet-b2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet-b2 from the MindSpore model zoo on Gitee at research/cv/efficientnet-b2.

efficientnet-b2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/efficientnet-b2](https://gitee.com/mindspore/models/blob/r1.9/research/cv/efficientnet-b2/README_CN.md).

All parameters in the module are trainable.

## Citation

Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
