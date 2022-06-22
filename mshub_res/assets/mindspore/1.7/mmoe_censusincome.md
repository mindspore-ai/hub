# mmoe

---

model-name: mmoe

backbone-name: mmoe

module-type: recommend

fine-tunable: True

model-version: 1.7

train-dataset: censusincome

evaluation: incomeauc100 | maritalauc100

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/recommend/mmoe>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/mmoe_ascend_v170_censusincome_research_recommend_incomeauc100_maritalauc100.ckpt>
    asset-sha256: 882ff75c70f07637e809b3c68461cb3a665cb8e7b3f2ad60623e8ab2a0460127

license: Apache2.0

summary: mmoe is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of mmoe from the MindSpore model zoo on Gitee at research/recommend/mmoe.

mmoe is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [research/recommend/mmoe](https://gitee.com/mindspore/models/blob/r1.7/research/recommend/mmoe/README_CN.md).

All parameters in the module are trainable.

## Citation

modeling-task-relationships-in-multi-task-learning-with-multi-gate-mixture-

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
