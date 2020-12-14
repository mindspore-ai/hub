# UNET2D

---

model-name: unet2d

backbone-name: unet

module-type: cv-image-segmentation

fine-tunable: True

input-shape: [388, 388, 3]

model-version: 1

dice_coeff: 0.908

author: MindSpore team

update-time: 2020-09-22

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/unet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: unet used to 2D image segmentation of ISBI challenge

---

## Introduction

This MindSpore Hub model uses the implementation of Unet2D from the MindSpore model zoo on Gitee at model_zoo/official/cv/unet.

This model has been trained on ISBI Challenge using the code published on Gitee.

All parameters in the module are trainable.

## Usage

Refer to the readme description and code of modelzoo for specific usage:
<https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/cv/unet/README.md>

## Citation

Paper: Olaf Ronneberger, Philipp Fischer, Thomas Brox. "U-Net: Convolutional Networks for Biomedical Image Segmentation." *conditionally accepted at MICCAI 2015*. 2015.
