# IPT

---

model-name: IPT

backbone-name: IPT

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: set5

evaluation: acc34.8

author: MindSpore team

update-time: 2022-04-27

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/IPT>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/ipt_x3_ascend_v160_set5_research_cv_acc34.8.ckpt>
    asset-sha256: c2b5c241595018b0f937a4e723b3ae59cd7f5b8b44a2c4f7704032427e8e38e2

license: Apache2.0

summary: IPT is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of IPT from the MindSpore model zoo on Gitee at research/cv/IPT.

IPT is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/IPT](https://gitee.com/mindspore/models/blob/r1.6/research/cv/IPT/README.md).

All parameters in the module are trainable.

## Citation

Hanting Chen, Yunhe Wang, Tianyu Guo, Chang Xu, Yiping Deng, Zhenhua Liu, Siwei Ma, Chunjing Xu, Chao Xu, and Wen Gao. "Pre-trained image processing transformer". CVPR 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
