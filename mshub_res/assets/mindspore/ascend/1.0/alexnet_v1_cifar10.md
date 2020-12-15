# AlexNet

---

model-name: AlexNet

backbone-name: AlexNet

module-type: cv-classification

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.881

author: MindSpore team

update-time: 2020-12-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/alexnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/alexnet/alexnet_ascend_1.0_cifar10_official_classification_20201214/alexnet.ckpt>
    asset-sha256: 0203d68bcff7d02aaee42bd6a42b5fe1306ab8fb2a82feb1ec06d8e62284600a

license: Apache2.0
summary: AlexNet used to classify the 10 classes of cifar10.
---

## Introduction

This MindSpore Hub model uses the implementation of AlexNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/alexnet.

This model has been trained on cifar10 using the code published on Gitee.

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

model = "mindspore/ascend/1.0/alexnet_v1_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=10)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Krizhevsky A, Sutskever I, Hinton G E. ImageNet Classification with Deep ConvolutionalNeural Networks. Advances In Neural Information Processing Systems.2012.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
