# Pix2Pix

---

model-name: Pix2Pix

backbone-name: Pix2Pix

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: maps

evaluation: -

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/Pix2Pix>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/pix2pix_ascend_v170_maps_research_cv.ckpt>
    asset-sha256: 39aa394d029b5c8b727c8c478fb14ffd48f11564a8b395e9b123ea28e2a8f324

license: Apache2.0

summary: Pix2Pix is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Pix2Pix from the MindSpore model zoo on Gitee at research/cv/Pix2Pix.

Pix2Pix is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Pix2Pix](https://gitee.com/mindspore/models/blob/r1.7/research/cv/Pix2Pix/README.md).

All parameters in the module are trainable.

## Citation

Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. "Image-to-Image Translation with Conditional Adversarial Networks", in CVPR 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
