# ResNet50 Resiudal Distillation

---

model-name: plain-CNN-resnet50

backbone-name: resnet50

module-type: cv-classification

fine-tunable: False

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.9446

author: Noah CVLab

update-time: 2020-11-17

repo-link:

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-lite: true

mindspore-version: 1.0

asset:

- file-format: mslite
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/residual_distill_lite/residual_distill_res50_cifar10_bs_1_update.ms>
  asset-sha256: 449498ecf5201d46d4eaee2754d69db89b656573f4e74ab42a9f8597299bb63b

license: Apache2.0

summary: ResNet50-plain derived by resiudal distillation method, and is used to classify 10 classes of CIFAR-10

---

## Introduction

This MindSpore Hub model uses the implementation of Residual Distillation on ResNet50.

## Citation

1. Guilin Li, Junlei Zhang, Yunhe Wang, Chuanjian Liu, Matthias Tan, Yunfeng Lin, Wei Zhang, Jiashi Feng, Tong Zhang. Residual Distillation: Towards Portable Deep Neural Networks without Shortcuts. Accepted by NeurIPS 2020.
