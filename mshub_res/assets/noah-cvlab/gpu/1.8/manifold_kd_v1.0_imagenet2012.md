# Manifold KD

---

model-name: Manifold KD

backbone-name: vit/swin_transformer

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: imagenet2012

accuracy: vit-tiny: 76.18 / swin-tiny: 82.04

author: Noah's Ark Lab

update-time: 2022-10-11

vit-repo-link: https://gitee.com/mindspore/models/tree/master/official/cv/VIT

swin-repo-link: https://gitee.com/mindspore/models/tree/master/official/cv/SwinTransformer

user-id: Noah's Ark Lab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.8

asset:

- file-format: ckpt

  asset-link: https://download.mindspore.cn/models/r1.8/manifold_kd_deit_tiny_gpu_v180_imagenet2012_research_cv_top1acc76.18.ckpt

  asset-link: https://download.mindspore.cn/models/r1.8/manifold_kd_swin_tiny_gpu_v180_imagenet2012_research_cv_top1acc82.04.ckpt

license: Apache2.0

summary: Manifold knowledge distillation model for imagenet classification

---

## Introduction

This MindSpore Hub model uses the implementation of vit and swin transformer from the MindSpore model zoo on above repo link.

## Citation

1. Zhiwei Hao, Jianyuan Guo, Ding Jia, Kai Han, Yehui Tang, Chao Zhang, Han Hu, Yunhe Wang, [**Learning Efficient Vision Transformers via Fine-Grained Manifold Distillation**](https://arxiv.org/pdf/2107.01378.pdf), In **NeurIPS 2022**.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.