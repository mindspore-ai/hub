# NFNet

---

model-name: NFNet

backbone-name: NFNet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc83.26

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/NFNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/nfnet_ascend_v190_imagenet2012_research_cv_top1acc83.26.ckpt>
    asset-sha256: 773b0098a124e13beaee3a14b3dfc09b73139cc185f11fc43d9d2124d6905c26

license: Apache2.0

summary: NFNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of NFNet from the MindSpore model zoo on Gitee at research/cv/NFNet.

NFNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/NFNet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/NFNet/README_CN.md).

All parameters in the module are trainable.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
