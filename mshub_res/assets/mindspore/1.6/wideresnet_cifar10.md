# wideresnet

---

model-name: wideresnet

backbone-name: wideresnet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: cifar10

evaluation: acc96.32

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/wideresnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/wideresnet_ascend_v160_cifar10_research_cv_acc96.32.ckpt>
    asset-sha256: 441c0aaa59b9e164be0666d5a318fc438532e7fd13730cfa0b6cb677a8217442

license: Apache2.0

summary: wideresnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wideresnet from the MindSpore model zoo on Gitee at research/cv/wideresnet.

wideresnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/wideresnet](https://gitee.com/mindspore/models/blob/r1.6/research/cv/wideresnet/README.md).

All parameters in the module are trainable.

## Citation

[Sergey Zagoruyko."Wide Residual Netwoks"](https://arxiv.org/pdf/1605.07146.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
