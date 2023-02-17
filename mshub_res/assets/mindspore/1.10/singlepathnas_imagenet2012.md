# single_path_nas

---

model-name: single_path_nas

backbone-name: single_path_nas

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: imagenet2012

evaluation: top1acc74.22 | top5acc91.73

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/single_path_nas>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/singlepathnas_ascend_v1100_imagenet2012_research_cv_top1acc74.22_top5acc91.73.ckpt>
    asset-sha256: 692cfdf824de2958ed92ffc178c9e55738ecd6c60a474e7d76ec99a4f0aa15ae

license: Apache2.0

summary: single_path_nas is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of single_path_nas from the MindSpore model zoo on Gitee at research/cv/single_path_nas.

single_path_nas is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/single_path_nas](https://gitee.com/mindspore/models/blob/r1.10/research/cv/single_path_nas/README.md).

All parameters in the module are trainable.

## Citation

[Single-Path NAS: Designing Hardware-Efficient ConvNets in less than 4 Hours](https://arxiv.org/pdf/1904.02877.pdf)
## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
