# VGG-Small Low Bit Quantization

---

model-name: VGG-Small-low bit

backbone-name: VGG-Small

module-type: cv-classification

fine-tunable: False

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.9369

author: Noah CVLab

update-time: 2020-11-28

repo-link:

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-lite: true

mindspore-version: 1.0

asset:

- file-format: mslite
  asset-link: <https://download.mindspore.cn/model_zoo/official/lite/low_bit_quant/low_bit_quant_bs_1.ms>
  asset-sha256: 81c17f9c60696bc286418563dc5dbfa240886cbd97d646596b07fc842c467d85

license: Apache2.0

summary: VGG-Small low bit derived by searching for low-bit weights method, and is used to classify 10 classes of CIFAR-10

---

## Introduction

This MindSpore Hub model uses the implementation of Searching for Low-Bit Weights, quantizing VGG-small using 2-bit weights and 2-bit activations.

## Citation

1. Zhaohui Yang, Yunhe Wang, Kai Han, Chunjing Xu, Chao Xu, Dacheng Tao, Chang Xu. Searching for Low-Bit Weights in Quantized Neural Networks. Accepted by NeurIPS 2020.
