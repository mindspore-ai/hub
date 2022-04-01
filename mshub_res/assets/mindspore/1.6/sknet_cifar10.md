# sknet

---

model-name: sknet

backbone-name: sknet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: cifar10

evaluation: acc94

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/sknet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/sknet_ascend_v160_cifar10_research_cv_acc94.ckpt>
    asset-sha256: 278db3c641d1be970d4fce82478f5e5b56f62ce4cbc8f122743a4093ba84014a

license: Apache2.0

summary: sknet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of sknet from the MindSpore model zoo on Gitee at research/cv/sknet.

sknet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/sknet](https://gitee.com/mindspore/models/blob/r1.6/research/cv/sknet/README.md).

All parameters in the module are trainable.

## Citation

Xiang Li, Wenhai Wang, Xiaolin Hu, Jian Yang. "Selective Kernel Networks"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
