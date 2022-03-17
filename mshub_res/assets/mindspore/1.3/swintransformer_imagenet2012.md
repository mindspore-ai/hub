# swin_transformer

---

model-name: swin_transformer

backbone-name: swin_transformer

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: imagenet2012

evaluation: top1acc80.96 | top5acc95.37

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/swin_transformer>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/swintransformer_ascend_v130_imagenet2012_research_cv_top1acc80.96_top5acc95.37.ckpt>
    asset-sha256: fe17613c1195629274edb22f92fc0704ddd02a20df8bd7e100afbb443d854e7e

license: Apache2.0

summary: swin_transformer is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of swin_transformer from the MindSpore model zoo on Gitee at research/cv/swin_transformer.

swin_transformer is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/swin_transformer](https://gitee.com/mindspore/models/blob/r1.3/research/cv/swin_transformer/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
