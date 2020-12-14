# PSENET

---

model-name: psenet

backbone-name: resnet50

module-type: cv-text-detection

fine-tunable: True

input-shape: [1920, 1920, 3]

model-version: 1

hmean: 0.806

author: MindSpore team

update-time: 2020-09-22

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/psenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: psenet used to cv text detection of ICDAR2015

---

## Introduction

This MindSpore Hub model uses the implementation of PSENet from the MindSpore model zoo on Gitee at model_zoo/official/cv/psenet.

This model has been trained on ICDAR2015 using the code published on Gitee.

All parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
<https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/cv/psenet/README.md>

## Citation

Paper: Wenhai Wang, Enze Xie, Xiang Li, Wenbo Hou, Tong Lu, Gang Yu, Shuai Shao; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9336-9345
