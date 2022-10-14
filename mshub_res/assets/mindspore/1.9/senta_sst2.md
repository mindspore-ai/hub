# senta

---

model-name: senta

backbone-name: senta

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: SST-2

evaluation: acc94.1

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/senta>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/senta_ascend_v190_sst2_research_nlp_acc94.1.ckpt>
    asset-sha256: 2e3612a195a63dce8fa4e91f73030eab7f70d87a47056f44a15ac9abbd05c1a2

license: Apache2.0

summary: senta is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of senta from the MindSpore model zoo on Gitee at research/nlp/senta.

senta is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/senta](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/senta/README_CN.md).

All parameters in the module are trainable.

## Citation

[SKEP: Sentiment Knowledge Enhanced Pre-training for Sentiment Analysis](https://arxiv.org/abs/2005.05635)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
