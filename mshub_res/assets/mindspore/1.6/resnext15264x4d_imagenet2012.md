# resnext152_64x4d

---

model-name: resnext152_64x4d

backbone-name: resnext152_64x4d

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc79.94 | top5acc94.66

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/resnext152_64x4d>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/resnext15264x4d_ascend_v160_imagenet2012_research_cv_top1acc79.94_top5acc94.66.ckpt>
    asset-sha256: 8045c5d89d7d2fbc0019bd4f519aba5e57e4d0d2a8fb55906718374b9a0792f0

license: Apache2.0

summary: resnext152_64x4d is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnext152_64x4d from the MindSpore model zoo on Gitee at research/cv/resnext152_64x4d.

resnext152_64x4d is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/resnext152_64x4d](https://gitee.com/mindspore/models/blob/r1.6/research/cv/resnext152_64x4d/README.md).

All parameters in the module are trainable.

## Citation

Xie S, Girshick R, Dollár, Piotr, et al. Aggregated Residual Transformations for Deep Neural Networks. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
