# proxylessnas

---

model-name: proxylessnas

backbone-name: proxylessnas

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc74.66 | top5acc92.08

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/proxylessnas>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/proxylessnas_ascend_v160_imagenet2012_research_cv_top1acc74.66_top5acc92.08.ckpt>
    asset-sha256: ee73221e47911a3c80c4d24e861205a6591c8b37ba0aa5b78e34444d4ab058b9

license: Apache2.0

summary: proxylessnas is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of proxylessnas from the MindSpore model zoo on Gitee at research/cv/proxylessnas.

proxylessnas is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/proxylessnas](https://gitee.com/mindspore/models/blob/r1.6/research/cv/proxylessnas/README.md).

All parameters in the module are trainable.

## Citation

Han Cai, Ligeng Zhu, Song Han. ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
