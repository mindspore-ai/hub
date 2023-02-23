# swin_transformer

---

model-name: swin_transformer

backbone-name: swin_transformer

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: ImageNet2012

evaluation: top1acc81.1 | top5acc95.36

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/swin_transformer>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/swintransformer_ascend_v1100_imagenet2012_research_cv_top1acc81.1_top5acc95.36.ckpt>
    asset-sha256: a8fdb2425f316d07f903c7c5084b6e5961705996253d3155e0fd1b92d6e47158

license: Apache2.0

summary: swin_transformer is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of swin_transformer from the MindSpore model zoo on Gitee at research/cv/swin_transformer.

swin_transformer is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/swin_transformer](https://gitee.com/mindspore/models/blob/r1.10/research/cv/swin_transformer/README_CN.md).

All parameters in the module are trainable.

## Citation

[Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/pdf/2103.14030.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
