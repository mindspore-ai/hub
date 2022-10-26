# U-GAT-IT

---

model-name: U-GAT-IT

backbone-name: U-GAT-IT

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: selfie2anime

evaluation: -

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/U-GAT-IT>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/ugatit_ascend_v190_selfie2anime_research_cv.ckpt>
    asset-sha256: f1b9815892e87eb040d86f2a0862819bbb7f3e84087aa430d2b6dae44160ff53

license: Apache2.0

summary: U-GAT-IT is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of U-GAT-IT from the MindSpore model zoo on Gitee at research/cv/U-GAT-IT.

U-GAT-IT is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/U-GAT-IT](https://gitee.com/mindspore/models/blob/r1.9/research/cv/U-GAT-IT/README.md).

All parameters in the module are trainable.

## Citation

[U-GAT-IT: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation](https://arxiv.org/pdf/1907.10830v4.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
