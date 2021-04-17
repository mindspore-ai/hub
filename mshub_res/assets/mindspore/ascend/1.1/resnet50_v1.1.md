# Resnet50

---

model-name: resnet50

backbone-name: resnet50

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: cifar10

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/resnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/resnet50_ascend_v111_cifar10_offical_cv_bs32_acc92/resnet50_ascend_v111_cifar10_offical_cv_bs32_acc92.ckpt>
    asset-sha256: 9ded0512c65c2df4673bec62f3b0de1551166985bddf55c20aa03af6ef8e87d9

license: Apache2.0

summary: resnet50 used to classify 10 classes of cifar10

---

## Introduction

This MindSpore Hub model uses the implementation of Resnet50 from the MindSpore model zoo on Gitee [model_zoo/official/cv/resnet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/resnet/README.md).

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

model = "mindspore/ascend/1.1/resnet50_v1.1"
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. He K , Zhang X , Ren S , et al. Deep Residual Learning for Image Recognition[J]. 2016.