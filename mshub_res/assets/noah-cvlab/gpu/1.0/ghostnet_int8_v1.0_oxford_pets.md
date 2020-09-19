# GhostNet_INT8

---

model-name: GhostNet_int8

backbone-name: GhostNet

module-type: CV-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: Oxford-IIIT Pet

accuracy: 0.8245



author: Noah CVLab

update-time: 2020-09-08

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/ghostnet_quant

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/research/cv/ghostnet_quant/ghostnet_1x_pets_int8.ckpt
    asset-sha256: e10180c9cfecb35cb261bc8668f2632990630570f189b108495168d23e935922
  
license: Apache2.0
summary: GhostNet_INT8 used to classify 37 classes of Oxford-IIIT Pet

---


## Introduction

This MindSpore Hub model uses the implementation of GhostNet_INT8 from the MindSpore model zoo on Gitee at model_zoo/official/cv/ghostnet_int8.

Quantization refers to techniques for performing computations and storing tensors at lower bitwidths than floating point precision. For 8bit quantization, we quantize the weights into [-128,127] and the activations into [0,255]. We finetune the model a few epochs after post-quantization to achieve better performance.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/ghostnet_int8_v1.0_oxford_pets"
network = mshub.load(model, num_classes=37)
network.set_train(False)
```

## Citation

1. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589