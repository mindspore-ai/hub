# tgcn

---

model-name: tgcn

backbone-name: tgcn

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: sztaxi

evaluation: acc71.56

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/tgcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/tgcn_ascend_v190_sztaxi_research_cv_acc71.56.ckpt>
    asset-sha256: 365eb16501de008890c90a723adf9a9f40995e40498b5d35ecd906119a56498c

license: Apache2.0

summary: tgcn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of tgcn from the MindSpore model zoo on Gitee at research/cv/tgcn.

tgcn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/tgcn](https://gitee.com/mindspore/models/blob/r1.9/research/cv/tgcn/README.md).

All parameters in the module are trainable.

## Citation

Zhao L, Song Y, Zhang C, et al. T-gcn: A temporal graph convolutional network for traffic prediction[J]. IEEE Transactions on Intelligent Transportation Systems, 2019, 21(9): 3848-3858.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
