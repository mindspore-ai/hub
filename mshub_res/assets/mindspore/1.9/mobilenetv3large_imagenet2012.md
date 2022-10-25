# mobilenetv3_large

---

model-name: mobilenetv3_large

backbone-name: mobilenetv3_large

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: ImageNet2012

evaluation: top1acc74.55 | top5acc91.74

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/mobilenetv3_large>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/mobilenetv3large_ascend_v190_imagenet2012_research_cv_top1acc74.55_top5acc91.74.ckpt>
    asset-sha256: 7efc7976c2496db8d39366d4e6167a4b6ed543de88a3897be6f14dea8c160f65

license: Apache2.0

summary: mobilenetv3_large is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv3_large from the MindSpore model zoo on Gitee at research/cv/mobilenetv3_large.

mobilenetv3_large is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/mobilenetv3_large](https://gitee.com/mindspore/models/blob/r1.9/research/cv/mobilenetv3_large/README_CN.md).

All parameters in the module are trainable.

## Citation

[Searching for MobileNetV3](https://arxiv.org/pdf/1905.02244.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
