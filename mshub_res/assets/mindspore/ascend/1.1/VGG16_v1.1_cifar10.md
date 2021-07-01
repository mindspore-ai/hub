# VGG16

---

model-name: VGG16

backbone-name: VGG16

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: cifar10

accuracy: 0.93

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/vgg16>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/vgg16_ascend_v111_cifar10_offical_cv_bs64_acc93/vgg16_ascend_v111_cifar10_offical_cv_bs64_acc93.ckpt>
    asset-sha256: b59a009a0417e12b40ecb825a800a9baffa30a8797f96fd01e52ba752e03311f

license: Apache2.0

summary: VGG16 used to classify the 10 classes of cifar10.

---

## Introduction

This MindSpore Hub model uses the implementation of VGG16 from the MindSpore model zoo on Gitee [model_zoo/official/cv/vgg16](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/vgg16/README.md).

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

model = "mindspore/ascend/1.1/VGG16_v1.1_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=10)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Simonyan K, zisserman A. Very Deep Convolutional Networks for Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.
