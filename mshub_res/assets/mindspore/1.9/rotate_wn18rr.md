# rotate

---

model-name: rotate

backbone-name: rotate

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: wn18rr

evaluation: MRR47 | MR3340 | HITS@1acc42 | HITS@3acc49 | HITS@10acc57

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/rotate>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/rotate_ascend_v190_wn18rr_research_nlp_MRR47_MR3340_HITS@1acc42_HITS@3acc49_HITS@10acc57.ckpt>
    asset-sha256: d78bb8cb987c632060262a5de793fbb6c27dbc17241bd343e2d0a15fa3b76609

license: Apache2.0

summary: rotate is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of rotate from the MindSpore model zoo on Gitee at research/nlp/rotate.

rotate is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/rotate](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/rotate/README_CN.md).

All parameters in the module are trainable.

## Citation

Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, Jian Tang: RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
