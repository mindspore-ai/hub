# efficientnet-b1

---

model-name: efficientnet-b1

backbone-name: efficientnet-b1

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc78.1 | top5acc94

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/efficientnet-b1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/efficientnetb1_ascend_v190_imagenet2012_research_cv_top1acc78.1_top5acc94.ckpt>
    asset-sha256: 49dec0aa32348a08ff7ef17b857c6d542809411469205dc1d478e130b8f8eb48

license: Apache2.0

summary: efficientnet-b1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet-b1 from the MindSpore model zoo on Gitee at research/cv/efficientnet-b1.

efficientnet-b1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/efficientnet-b1](https://gitee.com/mindspore/models/blob/r1.9/research/cv/efficientnet-b1/README_CN.md).

All parameters in the module are trainable.

## Citation

Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
