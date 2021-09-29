# yolov3_darknet53_quant

---

model-name: yolov3_darknet53_quant

backbone-name: darknet53_quant

module-type: cv-object_detection

fine-tunable: True

input-shape: [608, 608, 3]

model-version: 1

author: MindSpore team

update-time: 2020-09-19

repo-link: <https://gitee.com/mindspore/models/tree/master/official/cv/yolov3_darknet53_quant>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: yolov3_darknet53_quant used to do object detection, and reduce the size of the weight and improve the low-bit computing performance.

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_darknet53_quant from the MindSpore model zoo on Gitee at model_zoo/official/cv/yolov3_darknet53_quant.

yolov3_darknet53_quant supports 10 different input shapes for improving accuracy. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/models/blob/master/official/cv/yolov3_darknet53_quant/README.md).

All parameters in the module are trainable.

## Citation

1. Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.
2. Krishnamoorthi R. Quantizing deep convolutional networks for efficient inference: A whitepaper. arXiv preprint arXiv:1806.08342, 2018
