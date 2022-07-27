# dgcn

---

model-name: dgcn

backbone-name: dgcn

module-type: gnn

fine-tunable: True

model-version: 1.8

train-dataset: cora

evaluation: acc82.8

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/gnn/dgcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/dgcn_ascend_v180_cora_research_gnn_acc82.8.ckpt>
    asset-sha256: a1b1bfb3d76afdcb4a19751db7ecb246c9fb736bca08b1231bf681d10a2cf368

license: Apache2.0

summary: dgcn is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of dgcn from the MindSpore model zoo on Gitee at research/gnn/dgcn.

dgcn is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [research/gnn/dgcn](https://gitee.com/mindspore/models/blob/r1.8/research/gnn/dgcn/readme_CN.md).

All parameters in the module are trainable.

## Citation

Dual Graph Convolutional Networks for Graph-Based Semi-Supervised Classification[C]// the 2018 World Wide Web Conference. 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
