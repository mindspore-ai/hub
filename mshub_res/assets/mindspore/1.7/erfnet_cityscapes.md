# erfnet

---

model-name: erfnet

backbone-name: erfnet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: cityscapes

evaluation: acc70.73

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/cv/erfnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/erfnet_ascend_v170_cityscapes_official_cv_acc70.73.ckpt>
    asset-sha256: c356bab8810edfd54b6b9817eb37bdb6fb034e00da29f7a62ca9394aa58a05cc

license: Apache2.0

summary: erfnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of erfnet from the MindSpore model zoo on Gitee at official/cv/erfnet.

erfnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/erfnet](https://gitee.com/mindspore/models/blob/r1.7/official/cv/erfnet/README_CN.md).

All parameters in the module are trainable.

## Citation

1. E. Romera, J. M. Alvarez, L. M. Bergasa and R. Arroyo."ERFNet: Efficient Residual Factorized ConvNet for Real-time Semantic Segmentation"
2. A. Paszke, A. Chaurasia, S. Kim, and E. Culurciello."ENet: A deep neural network architecture for real-time semantic segmentation."

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
