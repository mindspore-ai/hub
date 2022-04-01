# dgcn

---

model-name: dgcn

backbone-name: dgcn

module-type: gnn

fine-tunable: True

model-version: 1.5

train-dataset: pubmed

evaluation: acc80.3

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/gnn/dgcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/dgcn_ascend_v150_pubmed_research_gnn_acc80.3.ckpt>
    asset-sha256: 76ea88b1ab45abbea81c99a6ae0eb5bb64da64f5bba04dbc5ae1a5c87e7de3fd

license: Apache2.0

summary: dgcn is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of dgcn from the MindSpore model zoo on Gitee at research/gnn/dgcn.

dgcn is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [research/gnn/dgcn](https://gitee.com/mindspore/models/blob/r1.5/research/gnn/dgcn/readme_CN.md).

All parameters in the module are trainable.

## Citation

Dual Graph Convolutional Networks for Graph-Based Semi-Supervised Classification[C]// the 2018 World Wide Web Conference. 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
