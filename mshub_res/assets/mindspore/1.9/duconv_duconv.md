# duconv

---

model-name: duconv

backbone-name: duconv

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: duconv

evaluation: F1score31.71

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/duconv>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/duconv_ascend_v190_duconv_official_nlp_F1score31.71.ckpt>
    asset-sha256: f952f93f26fe7f889b3e03d1d2be438ad6083baa3d6618f042133c904baf694a

license: Apache2.0

summary: duconv is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of duconv from the MindSpore model zoo on Gitee at official/nlp/duconv.

duconv is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/duconv](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/duconv/README_CN.md).

All parameters in the module are trainable.

## Citation

Wu W, Guo Z, Zhou X, et al. Proactive human-machine conversation with explicit conversation goals[J]. arXiv preprint arXiv:1906.05572, 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
