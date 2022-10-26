# tbnet

---

model-name: tbnet

backbone-name: tbnet

module-type: recommend

fine-tunable: True

model-version: 1.9

train-dataset: steam

evaluation: auc81.00

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/recommend/tbnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/tbnet_ascend_v190_steam_official_recommend_auc81.00.ckpt>
    asset-sha256: cdbffba3bef0b9c76d790ec1fe782ffc06f31c27cdc2de29347f2a53561ae9f2

license: Apache2.0

summary: tbnet is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of tbnet from the MindSpore model zoo on Gitee at official/recommend/tbnet.

tbnet is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [official/recommend/tbnet](https://gitee.com/mindspore/models/blob/r1.9/official/recommend/tbnet/README.md).

All parameters in the module are trainable.

## Citation

[Tower Bridge Net (TB-Net): Bidirectional Knowledge Graph Aware Embedding Propagation for Explainable Recommender Systems]()

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
