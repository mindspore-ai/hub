# Auto-DeepLab

---

model-name: Auto-DeepLab

backbone-name: Auto-DeepLab

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cityscapes

evaluation: miou77.3

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/Auto-DeepLab>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/autodeeplab_1M_ascend_v190_cityscapes_research_cv_miou77.3.ckpt>
    asset-sha256: b9bfb8936a2ed1a258da8494cda3f988ba1f81dccdade79104d8db10f7d3a4c7

license: Apache2.0

summary: Auto-DeepLab is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Auto-DeepLab from the MindSpore model zoo on Gitee at research/cv/Auto-DeepLab.

Auto-DeepLab is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Auto-DeepLab](https://gitee.com/mindspore/models/blob/r1.9/research/cv/Auto-DeepLab/README.md).

All parameters in the module are trainable.

## Citation

[Auto-DeepLab: Hierarchical Neural Architecture Search for Semantic Image Segmentation](https://arxiv.org/pdf/1901.02985v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
