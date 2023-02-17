# r2plus1d

---

model-name: r2plus1d

backbone-name: r2plus1d

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: ucf101

evaluation: acc96

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/r2plus1d>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/r2plus1d_ascend_v1100_ucf101_research_cv_acc96.ckpt>
    asset-sha256: 04bc87e418054af98902bb2c6d2470107e1ab952208230951670a597782ffac8

license: Apache2.0

summary: r2plus1d is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of r2plus1d from the MindSpore model zoo on Gitee at research/cv/r2plus1d.

r2plus1d is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/r2plus1d](https://gitee.com/mindspore/models/blob/r1.10/research/cv/r2plus1d/README_CN.md).

All parameters in the module are trainable.

## Citation

[A Closer Look at Spatiotemporal Convolutions for Action Recognition](https://arxiv.org/pdf/1711.11248v1.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
