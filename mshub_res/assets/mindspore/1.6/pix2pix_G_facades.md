# Pix2Pix

---

model-name: Pix2Pix

backbone-name: Pix2Pix

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: facades

evaluation: -

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/Pix2Pix>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/pix2pix_G_ascend_v160_facades_research_cv.ckpt>
    asset-sha256: 185b0679425ec6ac60b1d393023ec7b3f0c760feaa49e7d2a23c157a96a25b8d

license: Apache2.0

summary: Pix2Pix is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Pix2Pix from the MindSpore model zoo on Gitee at research/cv/Pix2Pix.

Pix2Pix is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Pix2Pix](https://gitee.com/mindspore/models/blob/r1.6/research/cv/Pix2Pix/README.md).

All parameters in the module are trainable.

## Citation

Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. "Image-to-Image Translation with Conditional Adversarial Networks", in CVPR 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
