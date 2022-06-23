# dgu

---

model-name: dgu

backbone-name: dgu

module-type: nlp

fine-tunable: True

model-version: 1.7

train-dataset: udc

evaluation: R1acc82.14 | R2acc90.45 | R5acc97.75

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/nlp/dgu>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/dgu_ascend_v170_udc_official_nlp_R1acc82.14_R2acc90.45_R5acc97.75.ckpt>
    asset-sha256: ef323d57071720e70df35c28d0d8cffcfafdefdfe694ca4c39b21d013f2b8542

license: Apache2.0

summary: dgu is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of dgu from the MindSpore model zoo on Gitee at official/nlp/dgu.

dgu is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/dgu](https://gitee.com/mindspore/models/blob/r1.7/official/nlp/dgu/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
