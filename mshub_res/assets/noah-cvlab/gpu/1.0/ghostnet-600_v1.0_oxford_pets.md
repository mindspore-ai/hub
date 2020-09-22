# GhostNet-600

---

model-name: GhostNet-600

backbone-name: GhostNet-600

module-type: cv-classification

fine-tunable: True

input-shape: [240, 240, 3]

model-version: 1.0

train-dataset: Oxford-IIIT Pet

accuracy: 0.869



author: Noah CVLab

update-time: 2020-09-08

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/ghostnet

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/research/cv/ghostnet/ghostnet600M_pets.ckpt
    asset-sha256: a37ea724eed747ef2f36961e1fdb0deec892643cb2b1d6826ea738539259c139

license: Apache2.0

summary: AlexNet used to classify 37 classes of Oxford-IIIT Pet

---


## Introduction

This MindSpore Hub model uses the implementation of GhostNet from the MindSpore model zoo on Gitee at
model_zoo/research/cv/ghostnet.


## Usage

```python
import mindspore_hub as mshub

from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/ghostnet-600_v1.0_oxford_pets"
network = mshub.load(model, num_classes=37)

network.set_train(False)
```

## Citation

1. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589