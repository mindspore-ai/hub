# manidp-res20

---

model-name: manidp-res20

backbone-name: manidp-res20

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.9205

author: Noah's Ark Lab

update-time: 2021-03-31

repo-link: <https://gitee.com/mindspore/models/tree/master/research/cv/ManiDP>

user-id: noah-cvlab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.1

mindspore-lite: False

asset:

- file-format: ckpt

  asset-link: <https://download.mindspore.cn/model_zoo/research/cv/manidp/resnet20.ckpt>

  asset-sha256: 3ba6e1e064231e5afd7bb776c52442a9bacb4e48195c9c93d1f7e4c3ddc279eb

license: Apache2.0

summary: manidp-res20 derived by ManiDP method can achieve comparable performance with 54.2% FLOPs drop, and is used to classify 10 classes of CIFAR-10

---

## Introduction

This MindSpore Hub model uses the implementation of ManiDP from the MindSpore model zoo on Gitee at model_zoo/research/cv/ManiDP.

## Usage

```python
import mindspore_hub as mshub

from mindspore import context

from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "noah-cvlab/gpu/1.1/manidp_v1.0_cifar10"
network = mshub.load(model, args)

network.set_train(False)
```

## Citation

[1] Yehui Tang, Yunhe Wang Yixing Xu, Yiping Deng, Chao Xu, Dacheng Tao, Chang Xu. **"Manifold Regularized Dynamic Network Pruning"**. <i>**CVPR 2021**.</i>

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.