# AttentionCluster

---

model-name: AttentionCluster

backbone-name: AttentionCluster

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: mnist

evaluation: top1acc75.24 | top5acc95.45

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/AttentionCluster>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/attentioncluster_fc2natt64_ascend_v190_mnist_research_cv_top1acc75.24_top5acc95.45.ckpt>
    asset-sha256: 0fe1f04e7761c10bb41cce6fc0a2fe7c687787614ee534cb769606c14a8b6712

license: Apache2.0

summary: AttentionCluster is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of AttentionCluster from the MindSpore model zoo on Gitee at research/cv/AttentionCluster.

AttentionCluster is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/AttentionCluster](https://gitee.com/mindspore/models/blob/r1.9/research/cv/AttentionCluster/README_CN.md).

All parameters in the module are trainable.

## Citation

[Attention Clusters: Purely Attention Based Local Feature Integration for Video Classification](https://arxiv.org/abs/1711.09550)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
