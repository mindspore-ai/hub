# augvit

---

model-name: augvit

backbone-name: augvit

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cifar10

evaluation: acc98.0

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/augvit>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/augvit_ascend_v190_cifar10_research_cv_acc98.0.ckpt>
    asset-sha256: f0e7b7b07ae7bfce70fb0fa3eed51814d4e90f420a9281bc2b49069e4deeffa4

license: Apache2.0

summary: augvit is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of augvit from the MindSpore model zoo on Gitee at research/cv/augvit.

augvit is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/augvit](https://gitee.com/mindspore/models/blob/r1.9/research/cv/augvit/readme.md).

All parameters in the module are trainable.

## Citation

Yehui Tang, Kai Han, Chang Xu, An Xiao, Yiping Deng, Chao Xu, Yunhe Wang. Augmented Shortcuts for Vision Transformers. NeurIPS 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
