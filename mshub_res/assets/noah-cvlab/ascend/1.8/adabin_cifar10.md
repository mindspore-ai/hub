# AdaBin

---

model-name: AdaBin

backbone-name: AdaBin

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 88.15

author: Noah's Ark Lab

update-time: 2022-08-28

repo-link: https://gitee.com/mindspore/models/tree/master/research/cv/AdaBin

user-id: Noah's Ark Lab

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.8

asset:

- file-format: ckpt
  asset-link: https://download.mindspore.cn/models/r1.8/adabin_ascend_v180_cifar10_research_cv_acc88.15.ckpt
  asset-sha256: 9bf0fca99efd709f65ce1e31c8bad84f3a9c15e23d4a9fdeef4e35deeef11b8e

license: Apache2.0

summary: 1-bit ResNet-20 model trained by AdaBin for image classification

---

## Introduction

This MindSpore Hub model uses the implementation of FDA-BNN from the MindSpore model zoo on Gitee at models/tree/master/research/cv/AdaBin.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context
from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "noah-cvlab/ascend/1.8/adabin_cifar10"
network = mshub.load(model, args)
network.set_train(False)
```

## Citation

1. Zhijun Tu, Xinghao Chen, Pengju Ren, and Yunhe Wang. "AdaBin: Improving Binary Neural Networks with Adaptive Binary Sets." arXiv preprint arXiv:2208.08084 (2022).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
