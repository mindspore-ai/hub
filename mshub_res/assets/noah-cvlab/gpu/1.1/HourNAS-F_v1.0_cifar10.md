# HourNAS-F

---

model-name: HourNAS-F

backbone-name: HourNAS-F

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.9618

author: Noah CVLab

update-time: 2021-03-24

repo-link: <https://gitee.com/mindspore/models/tree/master/research/cv/HourNAS>

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.1

mindspore-lite: False

asset:

- file-format: ckpt

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/HourNAS/hournas_f_cifar10.ckpt>

  asset-sha256: 2ce9cb49fd381a3a2d51a7f5b29e2039a00e178e1ec119d4505b0ed671379663

license: Apache2.0

summary: HourNAS-F derived by extremely fast neural architecture search through an hourglass lens, and is used to classify 10 classes of CIFAR-10

---

## Introduction

This MindSpore Hub model uses the implementation of HourNAS from the MindSpore model zoo on Gitee at model_zoo/research/cv/HourNAS.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.1/HourNAS-F_v1.0_cifar10"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Zhaohui Yang, Yunhe Wang, Xinghao Chen, Jianyuan Guo, Wei Zhang, Chao Xu, Chunjing Xu, Dacheng Tao, Chang Xu. **"HourNAS: Extremely Fast Neural Architecture Search Through an Hourglass Lens"**. <i>**CVPR 2021**.</i>