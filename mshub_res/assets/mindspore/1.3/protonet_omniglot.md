# ProtoNet

---

model-name: ProtoNet

backbone-name: ProtoNet

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: omniglot

evaluation: acc99.63

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/ProtoNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/protonet_ascend_v130_omniglot_research_cv_acc99.63.ckpt>
    asset-sha256: f2494972445dbe2c26d5d66dbe94cca5d047a6870aa28f5c42900c5e4562376a

license: Apache2.0

summary: ProtoNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ProtoNet from the MindSpore model zoo on Gitee at research/cv/ProtoNet.

ProtoNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ProtoNet](https://gitee.com/mindspore/models/blob/r1.3/research/cv/ProtoNet/README.md).

All parameters in the module are trainable.

## Citation

Prototypical Networks for Few-shot Learning

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
