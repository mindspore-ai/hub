# AttentionCluster

---

model-name: AttentionCluster

backbone-name: AttentionCluster

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: mnist

evaluation: top1acc72.98 | top5acc94.83

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/AttentionCluster>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/attentioncluster_fc2natt8_ascend_v1100_mnist_research_cv_top1acc72.98_top5acc94.83.ckpt>
    asset-sha256: fb7dc3ea5eabe3977d32a3e6abfc41944d336456944ab4339e2360f6e0f1991b

license: Apache2.0

summary: AttentionCluster is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of AttentionCluster from the MindSpore model zoo on Gitee at research/cv/AttentionCluster.

AttentionCluster is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/AttentionCluster](https://gitee.com/mindspore/models/blob/r1.10/research/cv/AttentionCluster/README_CN.md).

All parameters in the module are trainable.

## Citation

[Attention Clusters: Purely Attention Based Local Feature Integration for Video Classification](https://arxiv.org/pdf/1711.09550.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
