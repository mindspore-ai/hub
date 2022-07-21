# hypertext

---

model-name: hypertext

backbone-name: hypertext

module-type: nlp

fine-tunable: True

model-version: 1.8

train-dataset: tnews

evaluation: acc91.3

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/nlp/hypertext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/hypertext_ascend_v180_tnews_research_nlp_acc91.3.ckpt>
    asset-sha256: 704f893b690a8eb55f9ad4e4263eaed59890756e6f2a16674d0a5ffbbb3a674f

license: Apache2.0

summary: hypertext is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of hypertext from the MindSpore model zoo on Gitee at research/nlp/hypertext.

hypertext is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/hypertext](https://gitee.com/mindspore/models/blob/r1.8/research/nlp/hypertext/README_CN.md).

All parameters in the module are trainable.

## Citation

[HyperText: Endowing FastText with Hyperbolic Geometry](https://arxiv.org/abs/2010.16143)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
