# UNET2D

---

model-name: unet2d

backbone-name: unet

module-type: cv-semantic_segmentation

fine-tunable: True

input-shape: [388, 388, 3]

model-version: 1

dice_coeff: 0.908

author: MindSpore team

update-time: 2020-09-22

repo-link: <https://gitee.com/mindspore/models/tree/master/official/cv/unet>

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
<https://gitee.com/mindspore/models/blob/master/official/cv/unet/README.md>

## Citation

Paper: Olaf Ronneberger, Philipp Fischer, Thomas Brox. "U-Net: Convolutional Networks for Biomedical Image Segmentation." *conditionally accepted at MICCAI 2015*. 2015.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.