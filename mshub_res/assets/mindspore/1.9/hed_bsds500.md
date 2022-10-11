# hed

---

model-name: hed

backbone-name: hed

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: bsds500

evaluation: ODS77.2

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/hed>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/hed_ascend_v190_bsds500_research_cv_ODS77.2.ckpt>
    asset-sha256: fad52b107d0e42f50b4331a36da3c733410a17840f31892a0498616da1dde8e9

license: Apache2.0

summary: hed is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of hed from the MindSpore model zoo on Gitee at research/cv/hed.

hed is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/hed](https://gitee.com/mindspore/models/blob/r1.9/research/cv/hed/README.md).

All parameters in the module are trainable.

## Citation

Saining Xie, Zhuowen Tu. Holistically-Nested Edge Detection. arXiv preprint arXiv:1504.06375, 2015.(https://arxiv.org/abs/1504.06375)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
