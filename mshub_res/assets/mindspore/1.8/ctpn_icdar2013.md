# ctpn

---

model-name: ctpn

backbone-name: ctpn

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: icdar2013

evaluation: precision90 | recall86 | Fmeasure88

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/ctpn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/ctpn_ascend_v180_icdar2013_official_cv_precision90_recall86_Fmeasure88.ckpt>
    asset-sha256: a1cfaecc174c435683a889aef141e6edcb5b35535666f683c7f57d35c827565a

license: Apache2.0

summary: ctpn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ctpn from the MindSpore model zoo on Gitee at official/cv/ctpn.

ctpn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/ctpn](https://gitee.com/mindspore/models/blob/r1.8/official/cv/ctpn/README.md).

All parameters in the module are trainable.

## Citation

Zhi Tian, Weilin Huang, Tong He, Pan He, Yu Qiao, "Detecting Text in Natural Image with Connectionist Text Proposal Network", ArXiv, vol. abs/1609.03605, 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
