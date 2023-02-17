# ManiDP

---

model-name: ManiDP

backbone-name: ManiDP

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: cifar10

evaluation: acc92.0

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/ManiDP>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/manidp_ascend_v1100_cifar10_research_cv_acc92.0.ckpt>
    asset-sha256: 3ba6e1e064231e5afd7bb776c52442a9bacb4e48195c9c93d1f7e4c3ddc279eb

license: Apache2.0

summary: ManiDP is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ManiDP from the MindSpore model zoo on Gitee at research/cv/ManiDP.

ManiDP is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ManiDP](https://gitee.com/mindspore/models/blob/r1.10/research/cv/ManiDP/README.md).

All parameters in the module are trainable.

## Citation

[Manifold Regularized Dynamic Network Pruning](https://arxiv.org/pdf/2103.05861.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
