# Resnet50

---

model-name: resnet50

backbone-name: resnet50

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.5

train-dataset: cifar10

accuracy: 0.91

author: MindSpore team

update-time: 2020-08-26

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/resnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/resnet/resnet50_v1.5_ascend_0.3.0_cifar10_official_classification_20200718/resnet50.ckpt>  
    asset-sha256: 242da26be495f09ac8571811ba163ca22cda86025e800f1c04c4cddeaa3fa55b  

-
    file-format: air  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/resnet/resnet50_v1.5_ascend_0.3.0_cifar10_official_classification_20200718/resnet50.geir>  
    asset-sha256: b06031e2970316597f4f3c4f89ccfd859b9ef665fd21e001a5e8d46a886dbf67  

license: Apache2.0

summary: resnet50 used to classify 10 classes of cifar10

---

## Introduction

This MindSpore Hub model uses the implementation of Resnet50 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

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

model = "mindspore/ascend/0.7/resnet50_v1.5_cifar10"
network = mshub.load(model, class_num=10)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. He K , Zhang X , Ren S , et al. Deep Residual Learning for Image Recognition[J]. 2016.
