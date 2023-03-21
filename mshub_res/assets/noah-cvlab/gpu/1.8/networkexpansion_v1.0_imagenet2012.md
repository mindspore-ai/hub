# NetworkExpansion

---

model-name: NetworkExpansion

backbone-name: vit

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: imagenet2012

accuracy: vit-base: 81.5

author: Noah's Ark Lab

update-time: 2023-3-8

vit-repo-link: https://gitee.com/mindspore/models/tree/master/official/cv/VIT

user-id: Noah's Ark Lab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.8

asset:

- file-format: ckpt

  asset-link: https://download.mindspore.cn/models/r1.8/depth_expansion_vit_base_gpu_v180_imagenet2012_research_cv_top1acc81.5.ckpt

license: Apache2.0

summary: Model checkpoint for CVPR 2023 paper "Network Expansion For Practical Training Acceleration"

---

## Introduction

This MindSpore Hub model uses the implementation of vit model from the MindSpore model zoo on above repo link.

## Citation

1. Ning Ding, Yehui Tang, Kai Han, Chao Xu, Yunhe Wang. **Network Expansion For Practical Training Acceleration**. CVPR 2023.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.