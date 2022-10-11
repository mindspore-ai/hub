# repvgg

---

model-name: repvgg

backbone-name: repvgg

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc72.60 | top5acc90.61

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/repvgg>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/repvgg_ascend_v190_imagenet2012_research_cv_top1acc72.60_top5acc90.61.ckpt>
    asset-sha256: dd09785c5b00c794cc150fee1409cc379b5cf166e869330fed0cfa9ac7d42953

license: Apache2.0

summary: repvgg is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of repvgg from the MindSpore model zoo on Gitee at research/cv/repvgg.

repvgg is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/repvgg](https://gitee.com/mindspore/models/blob/r1.9/research/cv/repvgg/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
