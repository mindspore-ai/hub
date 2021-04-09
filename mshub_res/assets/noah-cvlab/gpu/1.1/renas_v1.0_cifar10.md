# renas-nasmodel

---

model-name: renas-nasmodel

backbone-name: renas-nasmodel

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.9411

author: Noah CVLab

update-time: 2021-03-31

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/renas>

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.1

mindspore-lite: False

asset:

- file-format: ckpt

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/renas/nasmodel.ckpt>

  asset-sha256: 5d5add9adef4f3792facb6d018a2905986c6381a61a97c5be049e5936a125e5f

license: Apache2.0

summary: renas-nasmodel derived by neural architecture search, and is used to classify 10 classes of CIFAR-10

---

## Introduction

This MindSpore Hub model uses the implementation of ReNAS from the MindSpore model zoo on Gitee at model_zoo/research/cv/renas.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.1/renas_v1.0_cifar10"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Yixing Xu, Yunhe Wang, Kai Han, Yehui Tang, Shangling Jui, Chunjing Xu, Chang Xu. **"ReNAS: Relativistic Evaluation of Neural Architecture Search"**. <i>**CVPR 2021**.</i>