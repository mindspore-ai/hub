# ctpn

---

model-name: ctpn

backbone-name: ctpn

module-type: cv-object_detection

fine-tunable: True

model-version: 1.10

train-dataset: ICDAR2013

evaluation: acc87.69

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/ctpn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/ctpn_pretrain_ascend_v1100_icdar2013_official_cv_acc87.69.ckpt>
    asset-sha256: 781e805fa3e5a56d43cf83127aff0caad6cb227b0c30176ee08c7f2ad36e9914

license: Apache2.0

summary: ctpn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ctpn from the MindSpore model zoo on Gitee at official/cv/ctpn.

ctpn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/ctpn](https://gitee.com/mindspore/models/blob/r1.10/official/cv/ctpn/README.md).

All parameters in the module are trainable.

## Citation

[Detecting Text in Natural Image with Connectionist Text Proposal Network](https://arxiv.org/pdf/1609.03605.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
