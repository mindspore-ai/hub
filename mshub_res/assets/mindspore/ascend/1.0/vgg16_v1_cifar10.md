# VGG16

---

model-name: VGG16

backbone-name: VGG16

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.93

author: MindSpore team

update-time: 2020-09-22

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/vgg16>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/vgg/vgg16_ascend_1.0_cifar10_official_classification_20200923/vgg16.ckpt>  
    asset-sha256: 8f24d2782b3f6ec0380c1ea597ba24c1cf8749d1b0411e147263e266788869e4  

-
    file-format: air  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/vgg/vgg16_ascend_1.0_cifar10_official_classification_20200923/vgg16.geir>  
    asset-sha256: 2ebff88197f0fdefbb3249fa8770a48fe8242b3e69333a2e76af147158108cf9  

license: Apache2.0

summary: VGG16 used to classify the 10 classes of cifar10.

---

## Introduction

This MindSpore Hub model uses the implementation of VGG16 from the MindSpore model zoo on Gitee at model_zoo/official/cv/vgg16.

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

model = "mindspore/ascend/1.0/vgg16_v1_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=10)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Simonyan K, zisserman A. Very Deep Convolutional Networks for Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.
