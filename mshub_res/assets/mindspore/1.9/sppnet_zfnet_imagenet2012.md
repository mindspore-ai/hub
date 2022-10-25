# SPPNet

---

model-name: SPPNet

backbone-name: SPPNet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: ImageNet2012

evaluation: top1acc64.58 | top5acc85.53

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/SPPNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/sppnet_zfnet_ascend_v190_imagenet2012_research_cv_top1acc64.58_top5acc85.53.ckpt>
    asset-sha256: 5e1ca8fb66ee195ee708f5c3d8ec3e1cc828c87ae664585a2a3e11dd35947b62

license: Apache2.0

summary: SPPNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of SPPNet from the MindSpore model zoo on Gitee at research/cv/SPPNet.

SPPNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/SPPNet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/SPPNet/README_CN.md).

All parameters in the module are trainable.

## Citation

[Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/pdf/1406.4729.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
