# retinanet_resnet101

---

model-name: retinanet_resnet101

backbone-name: retinanet_resnet101

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: coco2017

evaluation: mAP36.72

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/retinanet_resnet101>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/retinanetresnet101_ascend_v1100_coco2017_research_cv_mAP36.72.ckpt>
    asset-sha256: 7ca7b5844809cdaaf9a880c02b80205414321e2ada8272827bb0e1fb5d42d107

license: Apache2.0

summary: retinanet_resnet101 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of retinanet_resnet101 from the MindSpore model zoo on Gitee at research/cv/retinanet_resnet101.

retinanet_resnet101 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/retinanet_resnet101](https://gitee.com/mindspore/models/blob/r1.10/research/cv/retinanet_resnet101/README.md).

All parameters in the module are trainable.

## Citation

[Focal Loss for Dense Object Detection](https://arxiv.org/pdf/1708.02002.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
