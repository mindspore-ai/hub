# convnext

---

model-name: convnext

backbone-name: convnext

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: imagenet2012

evaluation: top1acc82.2 | top5acc95.74

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/convnext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/convnext_ascend_v180_imagenet2012_research_cv_top1acc82.2_top5acc95.74.ckpt>
    asset-sha256: 7e8a1d654ffc135c0d73865e1d292c60bf31a9acfaaaf7a02bf094fb68419ab1

license: Apache2.0

summary: convnext is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of convnext from the MindSpore model zoo on Gitee at research/cv/convnext.

convnext is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/convnext](https://gitee.com/mindspore/models/blob/r1.8/research/cv/convnext/README_CN.md).

All parameters in the module are trainable.

## Citation

A ConvNet for the 2020s

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
