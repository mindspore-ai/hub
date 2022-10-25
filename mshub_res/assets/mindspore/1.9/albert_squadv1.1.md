# albert

---

model-name: albert

backbone-name: albert

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: squadv1.1

evaluation: exactmatch80.88 | F1score88.71

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/albert>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/albert_ascend_v190_squadv1.1_research_nlp_exactmatch80.88_F1score88.71.ckpt>
    asset-sha256: c60cc45a88fbf85bac9bc4bc3edced7d31281511bd6f70c6e13fb3ccc8e2ec09

license: Apache2.0

summary: albert is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of albert from the MindSpore model zoo on Gitee at research/nlp/albert.

albert is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/albert](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/albert/README.md).

All parameters in the module are trainable.

## Citation

1. [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/pdf/1909.11942.pdf)
2. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
