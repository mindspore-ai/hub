# dam

---

model-name: dam

backbone-name: dam

module-type: nlp

fine-tunable: True

model-version: 1.8

train-dataset: ubuntu

evaluation: R2@1acc93.8 | R10@1acc76.7 | R10@2acc87.4 | R10@5acc96.9

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/nlp/dam>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/dam_ascend_v180_ubuntu_research_nlp_R2@1acc93.8_R10@1acc76.7_R10@2acc87.4_R10@5acc96.9.ckpt>
    asset-sha256: dbe73ef2fa0982a908ae88dee4772f5a8201a1b63c8403bee75096c62b73a776

license: Apache2.0

summary: dam is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of dam from the MindSpore model zoo on Gitee at research/nlp/dam.

dam is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/dam](https://gitee.com/mindspore/models/blob/r1.8/research/nlp/dam/README.md).

All parameters in the module are trainable.

## Citation

Zhou, Xiangyang , et al. "Multi-Turn Response Selection for Chatbots with Deep Attention Matching Network." Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
