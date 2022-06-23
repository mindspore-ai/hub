# HRNetW48_cls

---

model-name: HRNetW48_cls

backbone-name: HRNetW48_cls

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: imagenet2012

evaluation: top1acc79 | top5acc94

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/HRNetW48_cls>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/hrnetw48cls_ascend_v170_imagenet2012_research_cv_top1acc79_top5acc94.ckpt>
    asset-sha256: 0ec1995df080ee801a33c6e9d659a4d3e2e677c642bf318ab96e3230b83fdca1

license: Apache2.0

summary: HRNetW48_cls is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of HRNetW48_cls from the MindSpore model zoo on Gitee at research/cv/HRNetW48_cls.

HRNetW48_cls is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/HRNetW48_cls](https://gitee.com/mindspore/models/blob/r1.7/research/cv/HRNetW48_cls/README_CN.md).

All parameters in the module are trainable.

## Citation

Deep High-Resolution Representation Learning for Visual Recognition. Jingdong Wang, Ke Sun, Tianheng Cheng, Borui Jiang, Chaorui Deng, Yang Zhao, Dong Liu, Yadong Mu, Mingkui Tan, Xinggang Wang, Wenyu Liu, Bin Xiao.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
