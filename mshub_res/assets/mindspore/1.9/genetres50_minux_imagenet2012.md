# GENet_Res50

---

model-name: GENet_Res50

backbone-name: GENet_Res50

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc77.76 | top5acc93.64

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/GENet_Res50>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/genetres50_minux_ascend_v190_imagenet2012_research_cv_top1acc77.76_top5acc93.64.ckpt>
    asset-sha256: 6b568bebdf808db1bdfd9d013bd45ecd132f5788275d4bd0a4b30884165015bd

license: Apache2.0

summary: GENet_Res50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of GENet_Res50 from the MindSpore model zoo on Gitee at research/cv/GENet_Res50.

GENet_Res50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/GENet_Res50](https://gitee.com/mindspore/models/blob/r1.9/research/cv/GENet_Res50/README_CN.md).

All parameters in the module are trainable.

## Citation

[Gather-Excite: Exploiting Feature Context in Convolutional Neural Networks](https://arxiv.org/pdf/1810.12348.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
