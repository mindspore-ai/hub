# GoogleNet

---

model-name: GoogleNet

backbone-name: GoogleNet

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.934



author: MindSpore team

update-time: 2020-08-25

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/googlenet

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:
  -
    file-format: ckpt  
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/googlenet/goolenet_ascend_0.2.0_cifar10_official_classification_20200713/googlenet.ckpt  
    asset-sha256: 114e5acc31dad444fa8ed2aafa02ca34734419f602b9299f3b53013dfc71b0f7
  -
    file-format: air  
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/googlenet/goolenet_ascend_0.2.0_cifar10_official_classification_20200713/googlenet.geir  
    asset-sha256: a092a28211fcab98fdabdf00c95098587b8d84d0f33c2a4d29e2f6c43d3b0b60

license: Apache2.0
summary: GoogLeNet used to classify the 10 classes of cifar10.
---


## Introduction

This MindSpore Hub model uses the implementation of GoogleNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/googlenet.

This model has been trained on Cifar10 using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/googlenet_v1_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=10)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Szegedy C, Liu W, Jia Y, et al. Going deeper with convolutions[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 1-9.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
