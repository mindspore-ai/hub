# sdne

---

model-name: sdne

backbone-name: sdne

module-type: gnn

fine-tunable: True

model-version: 1.8

train-dataset: wiki

evaluation: mAP66.74

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/gnn/sdne>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/sdne_ascend_v180_wiki_research_gnn_mAP66.74.ckpt>
    asset-sha256: a86649be4a355ccc87952c18f9c8a0316004d7eb2e2ddf7c2882177537797236

license: Apache2.0

summary: sdne is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of sdne from the MindSpore model zoo on Gitee at research/gnn/sdne.

sdne is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [research/gnn/sdne](https://gitee.com/mindspore/models/blob/r1.8/research/gnn/sdne/README_CN.md).

All parameters in the module are trainable.

## Citation

Wang D ,  Cui P ,  Zhu W. Structural Deep Network Embedding[C]// Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. August 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
