# ResNet50 Adv Quant

---

model-name: ResNet50-0.65x

backbone-name: resnet50

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: Oxford-IIIT Pet

accuracy: 0.8024

author: Noah CVLab

update-time: 2020-09-08

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/resnet50_adv_pruning

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.0

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/research/cv/resnet50_adv_pruning/resnet50-pet-0.65x-80.24.ckpt
    asset-sha256: b41eb489a62c8c12ff88b7f028bc4a943f29f8e25a0a9ec69b9ed070681340cc

license: Apache2.0

summary: ResNet-0.65x derived by adversarial pruning method, and is used to classify 37 classes of Oxford-IIIT Pet

---


## Introduction

This MindSpore Hub model uses the implementation of Adversarial Pruning on ResNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/adversarial_pruning.


## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.0/resnet-0.65x_v1.0_oxford_pets"

network = mshub.load(model)
network.set_train(False)

```

## Citation

1. Yehui Tang, Yunhe Wang, Yixing Xu, Dacheng Tao, Chunjing Xu, Chao Xu, Chang Xu. Scientific Control for Reliable Neural Network Pruning. Submitted to NeurIPS 2020.