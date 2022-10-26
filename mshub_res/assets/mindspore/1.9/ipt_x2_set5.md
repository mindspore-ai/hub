# IPT

---

model-name: IPT

backbone-name: IPT

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: set5

evaluation: acc38.3

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/IPT>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/ipt_x2_ascend_v190_set5_research_cv_acc38.3.ckpt>
    asset-sha256: b0faf955e2ed0a02a7f90dafac1af9f9eab2b657c4f373b5355a280e5c1f4403

license: Apache2.0

summary: IPT is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of IPT from the MindSpore model zoo on Gitee at research/cv/IPT.

IPT is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/IPT](https://gitee.com/mindspore/models/blob/r1.9/research/cv/IPT/README.md).

All parameters in the module are trainable.

## Citation

[Pre-Trained Image Processing Transformer](https://arxiv.org/pdf/2012.00364.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
