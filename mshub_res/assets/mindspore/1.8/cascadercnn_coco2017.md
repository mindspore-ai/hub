# CascadeRCNN

---

model-name: CascadeRCNN

backbone-name: CascadeRCNN

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: coco2017

evaluation: map37.3 | ap50acc55.5

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/CascadeRCNN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/cascadercnn_ascend_v180_coco2017_research_cv_map37.3_ap50acc55.5.ckpt>
    asset-sha256: 18204a922b382758a16cd57d30481a6f5c4d06aaabfe228aa3c8804521d2a019

license: Apache2.0

summary: CascadeRCNN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of CascadeRCNN from the MindSpore model zoo on Gitee at research/cv/CascadeRCNN.

CascadeRCNN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/CascadeRCNN](https://gitee.com/mindspore/models/blob/r1.8/research/cv/CascadeRCNN/README.md).

All parameters in the module are trainable.

## Citation

Cai Z, Vasconcelos N. Cascade r-cnn: Delving into high quality object detection[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2018: 6154-6162.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
