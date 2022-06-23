# ernie

---

model-name: ernie

backbone-name: ernie

module-type: nlp

fine-tunable: True

model-version: 1.7

train-dataset: xnli

evaluation: acc77.94

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/nlp/ernie>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/ernie_ascend_v170_xnli_official_nlp_acc77.94.ckpt>
    asset-sha256: 79d087714879644a1698eeccba138a7e84f9bb5a534f239fea7acfa61914bfa9

license: Apache2.0

summary: ernie is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of ernie from the MindSpore model zoo on Gitee at official/nlp/ernie.

ernie is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/ernie](https://gitee.com/mindspore/models/blob/r1.7/official/nlp/ernie/README_CN.md).

All parameters in the module are trainable.

## Citation

[ERNIE: Enhanced Representation through Knowledge Integration](https://arxiv.org/abs/1904.09223): Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Xuyi Chen, Han Zhang, Xin Tian, Danxiang Zhu, Hao Tian, Hua Wu.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
