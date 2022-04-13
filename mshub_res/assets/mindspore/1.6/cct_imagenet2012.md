# cct

---

model-name: cct

backbone-name: cct

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc80.24 | top5acc94.93

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/cct>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/cct_ascend_v160_imagenet2012_research_cv_top1acc80.24_top5acc94.93.ckpt>
    asset-sha256: 7df9c4c1e9d190f289aadfe79fdbef5c330228b1694230eeedf552dc15188261

license: Apache2.0

summary: cct is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of cct from the MindSpore model zoo on Gitee at research/cv/cct.

cct is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/cct](https://gitee.com/mindspore/models/blob/r1.6/research/cv/cct/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
