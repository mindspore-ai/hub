# resnet50_bam

---

model-name: resnet50_bam

backbone-name: resnet50_bam

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: imagenet2012

evaluation: top1acc78.27 | top5acc93.99

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/resnet50_bam>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/resnet50bam_ascend_v1100_imagenet2012_research_cv_top1acc78.27_top5acc93.99.ckpt>
    asset-sha256: fe3222a85020953003c95132108d38e39923f71a0ab8a820a3946072fb591550

license: Apache2.0

summary: resnet50_bam is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet50_bam from the MindSpore model zoo on Gitee at research/cv/resnet50_bam.

resnet50_bam is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/resnet50_bam](https://gitee.com/mindspore/models/blob/r1.10/research/cv/resnet50_bam/README.md).

All parameters in the module are trainable.

## Citation

[BAM: Bottleneck Attention Module](https://arxiv.org/pdf/1807.06514v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
