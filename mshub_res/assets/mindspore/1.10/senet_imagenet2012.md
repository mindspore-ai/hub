# SE-Net

---

model-name: SE-Net

backbone-name: SE-Net

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: imagenet2012

evaluation: top1acc77.75 | top5acc93.84

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/SE-Net>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/senet_ascend_v1100_imagenet2012_research_cv_top1acc77.75_top5acc93.84.ckpt>
    asset-sha256: 3abfaa11d0d9ef240641050df3a8c26a3e0f31e9484d10404a37246d7dc5f31c

license: Apache2.0

summary: SE-Net is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of SE-Net from the MindSpore model zoo on Gitee at research/cv/SE-Net.

SE-Net is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/SE-Net](https://gitee.com/mindspore/models/blob/r1.10/research/cv/SE-Net/README.md).

All parameters in the module are trainable.

## Citation

[Squeeze-and-Excitation Networks](https://arxiv.org/pdf/1709.01507.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
