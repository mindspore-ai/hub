# E-NET

---

model-name: E-NET

backbone-name: E-NET

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cityscapes

evaluation: miou58.73

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/E-NET>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/enet_ascend_v190_cityscapes_research_cv_miou58.73.ckpt>
    asset-sha256: df54727a2c67c490aee80378d160a07bc1644e9dc9af6b038139e3a28c943ce1

license: Apache2.0

summary: E-NET is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of E-NET from the MindSpore model zoo on Gitee at research/cv/E-NET.

E-NET is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/E-NET](https://gitee.com/mindspore/models/blob/r1.9/research/cv/E-NET/README_CN.md).

All parameters in the module are trainable.

## Citation

[ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation](https://arxiv.org/pdf/1606.02147.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
