# centernet

---

model-name: centernet

backbone-name: dla34

module-type: cv

fine-tunable: True

input-shape: [512, 512, 3]

model-version: 1

author: MindSpore team

update-time: 2020-12-21

repo-link: <https://gitee.com/mindspore/models/tree/master/research/cv/centernet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: centernet for multi-person pose detection

---

## Introduction

This MindSpore Hub model uses the implementation of centernet from the MindSpore model zoo on Gitee at model_zoo/research/cv/centernet.

CenterNet is an anchor-free detection network. Object is modeled as a single center point of its bounding box, and the detector uses keypoint estimation to find center points and regresses to all other object properties. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/models/tree/master/research/cv/centernet/README.md).

All parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
<https://gitee.com/mindspore/models/tree/master/research/cv/centernet>

## Citation

1. Xingyi Zhou, Dequan Wang, Philipp Krahenbuhl. Objects as Points. arXiv:1904.07850v2[cs.CV], 2019. 4.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.