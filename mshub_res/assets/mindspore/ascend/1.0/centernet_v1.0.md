# centernet

---

model-name: centernet

backbone-name: dla34

module-type: cv-multi-person_pose_detection

fine-tunable: True

input-shape: [512, 512, 3]

model-version: 1

author: MindSpore team

update-time: 2020-12-21

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/centernet>

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

CenterNet is an anchor-free detection network. Object is modeled as a single center point of its bounding box, and the detector uses keypoint estimation to find center points and regresses to all other object properties. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/centernet/README.md).

All parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
<https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/centernet>

## Citation

1. Xingyi Zhou, Dequan Wang, Philipp Krahenbuhl. Objects as Points. arXiv:1904.07850v2[cs.CV], 2019. 4.
