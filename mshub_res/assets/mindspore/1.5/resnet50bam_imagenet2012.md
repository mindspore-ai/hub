# resnet50_bam

---

model-name: resnet50_bam

backbone-name: resnet50_bam

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: imagenet2012

evaluation: top1acc75.9 | top5acc92.4

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/resnet50_bam>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/resnet50bam_ascend_v150_imagenet2012_research_cv_top1acc75.9_top5acc92.4.ckpt>
    asset-sha256: 4e1c0f5b06ec9a2909ed999c850b6b9b2bd60eefcad16a2bc4569b800e754e20

license: Apache2.0

summary: resnet50_bam is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet50_bam from the MindSpore model zoo on Gitee at research/cv/resnet50_bam.

resnet50_bam is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/resnet50_bam](https://gitee.com/mindspore/models/blob/r1.5/research/cv/resnet50_bam/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
