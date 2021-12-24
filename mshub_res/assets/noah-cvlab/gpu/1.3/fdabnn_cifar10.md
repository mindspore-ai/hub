# FDA-BNN

---

model-name: FDA-BNN

backbone-name: FDA-BNN

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 86.6

author: Noah's Ark Lab

update-time: 2021-12-16

repo-link: https://gitee.com/mindspore/models/tree/master/research/cv/FDA-BNN

user-id: Noah's Ark Lab

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 1.3

asset:

- file-format: ckpt

  asset-link: https://download.mindspore.cn/model_zoo/research/cv/FDA_BNN/fdabnn.ckpt

  asset-sha256: 8c6c14514ebd75e7992400b2839b1135438736941408889698120a3e0be56101

license: Apache2.0
summary: 1-bit ResNet-20 model trained by FDA-BNN for visual recognition

---

## Introduction

This MindSpore Hub model uses the implementation of FDA-BNN from the MindSpore model zoo on Gitee at models/tree/master/research/cv/FDA-BNN.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context
from src.args import args

context.set_context(mode=context.PYNATIVE_MODE,
                    device_target="GPU",
                    device_id=0)

model = "mindspore/gpu/1.3/fdabnn_cifar10"
network = mshub.load(model, args)
network.set_train(False)
```

## Citation

1. Yixing Xu, Kai Han, Chang Xu, Yehui Tang, Chunjing Xu, Yunhe Wang;  Learning frequency domain approximation for binary neural networks[J]. arXiv preprint arXiv:2103.00841, 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.