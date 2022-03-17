# dlrm

---

model-name: dlrm

backbone-name: dlrm

module-type: recommend

fine-tunable: True

model-version: 1.3

train-dataset: criteo

evaluation: acc78.96

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/recommend/dlrm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/dlrm_ascend_v130_criteo_research_recommend_acc78.96.ckpt>
    asset-sha256: b4e9982c2c18458c30eee7cd2f791fd28e62244de12c45cef813940e418a89f4

license: Apache2.0

summary: dlrm is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of dlrm from the MindSpore model zoo on Gitee at research/recommend/dlrm.

dlrm is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [research/recommend/dlrm](https://gitee.com/mindspore/models/blob/r1.3/research/recommend/dlrm/README_CN.md).

All parameters in the module are trainable.

## Citation

Naumov M, Mudigere D, Shi H J M, et al. Deep learning recommendation model for personalization and recommendation systems[J]. arXiv preprint arXiv:1906.00091, 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
