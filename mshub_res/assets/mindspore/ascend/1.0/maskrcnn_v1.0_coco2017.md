# Mask R-CNN

---

model-name: maskrcnn

backbone-name: ResNet-50

module-type: cv

fine-tunable: True

input-shape: [2, 3, 768, 1280]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-23

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/maskrcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: maskrcnn used to do instance segmentation.

---

## Introduction

This MindSpore Hub model uses the implementation of Mask R-CNN Model from the MindSpore model zoo on Gitee at model_zoo/official/cv/maskrcnn.

This model has been trained on coco2017 using the code published on Gitee.
All Parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
<https://gitee.com/mindspore/mindspore/tree/r1.0/model_zoo/official/cv/maskrcnn>

## Citation

Paper: Kaiming He, Georgia Gkioxari, Piotr Dollar, Ross Girshick, Facebook AI Research (FAIR). Mask R-CNN.
