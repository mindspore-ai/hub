# IPT

---

model-name: IPT

backbone-name: IPT

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: cbsd68

evaluation: acc29.9

author: MindSpore team

update-time: 2022-04-27

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/IPT>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/ipt_denoise50_ascend_v150_cbsd68_research_cv_acc29.9.ckpt>
    asset-sha256: 7a068947e15267d2adce390121b7463b9acdd8a0ce498d5bd0892fcb3bca7096

license: Apache2.0

summary: IPT is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of IPT from the MindSpore model zoo on Gitee at research/cv/IPT.

IPT is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/IPT](https://gitee.com/mindspore/models/blob/r1.5/research/cv/IPT/README.md).

All parameters in the module are trainable.

## Citation

Hanting Chen, Yunhe Wang, Tianyu Guo, Chang Xu, Yiping Deng, Zhenhua Liu, Siwei Ma, Chunjing Xu, Chao Xu, and Wen Gao. "Pre-trained image processing transformer". CVPR 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
