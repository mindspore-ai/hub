# hypertext

---

model-name: hypertext

backbone-name: hypertext

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: TNEWS

evaluation: acc81.39

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/hypertext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/hypertext_ascend_v190_tnews_research_nlp_acc81.39.ckpt>
    asset-sha256: 93e49a8deda35b34715cc33da91e027e5cfa895e36d721e74868eb533eb9d5cc

license: Apache2.0

summary: hypertext is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of hypertext from the MindSpore model zoo on Gitee at research/nlp/hypertext.

hypertext is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/hypertext](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/hypertext/README_CN.md).

All parameters in the module are trainable.

## Citation

[HyperText: Endowing FastText with Hyperbolic Geometry](https://arxiv.org/abs/2010.16143)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
