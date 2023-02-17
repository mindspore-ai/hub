# proxylessnas

---

model-name: proxylessnas

backbone-name: proxylessnas

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: imagenet2012

evaluation: top1acc74.77 | top5acc92.25

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/proxylessnas>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/proxylessnas_ascend_v1100_imagenet2012_research_cv_top1acc74.77_top5acc92.25.ckpt>
    asset-sha256: f4c61970d728594a3125339c9da9e8232d6fd8bf758747793b55881dd915ad21

license: Apache2.0

summary: proxylessnas is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of proxylessnas from the MindSpore model zoo on Gitee at research/cv/proxylessnas.

proxylessnas is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/proxylessnas](https://gitee.com/mindspore/models/blob/r1.10/research/cv/proxylessnas/README.md).

All parameters in the module are trainable.

## Citation

[ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware](https://arxiv.org/pdf/1812.00332v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
