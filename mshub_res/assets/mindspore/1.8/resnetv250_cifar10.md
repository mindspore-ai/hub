# resnetv2

---

model-name: resnetv2

backbone-name: resnetv2

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: cifar10

evaluation: top1acc95.2

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/resnetv2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/resnetv250_ascend_v180_cifar10_research_cv_top1acc95.2.ckpt>
    asset-sha256: d88993343168c69ee523052b7cd605fd0c7cb426dff6f033d7e2be068d05a9a3

license: Apache2.0

summary: resnetv2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnetv2 from the MindSpore model zoo on Gitee at research/cv/resnetv2.

resnetv2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/resnetv2](https://gitee.com/mindspore/models/blob/r1.8/research/cv/resnetv2/README_CN.md).

All parameters in the module are trainable.

## Citation

Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Identity Mappings in Deep Residual Networks"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
