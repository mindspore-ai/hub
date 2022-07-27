# efficientnet-b3

---

model-name: efficientnet-b3

backbone-name: efficientnet-b3

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: imagenet2012

evaluation: top1acc80.37 | top5acc95.17

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/efficientnet-b3>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/efficientnetb3_ascend_v180_imagenet2012_research_cv_top1acc80.37_top5acc95.17.ckpt>
    asset-sha256: 7c7b1973e39709159893534e201ca9bda2d860b7370e74729e570f979135270f

license: Apache2.0

summary: efficientnet-b3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet-b3 from the MindSpore model zoo on Gitee at research/cv/efficientnet-b3.

efficientnet-b3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/efficientnet-b3](https://gitee.com/mindspore/models/blob/r1.8/research/cv/efficientnet-b3/README_CN.md).

All parameters in the module are trainable.

## Citation

Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
