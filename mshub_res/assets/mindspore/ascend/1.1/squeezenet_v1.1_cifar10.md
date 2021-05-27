# SqueezeNet

---

model-name: squeezenet

backbone-name: squeezenet

module-type: cv-classification

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.1

train-dataset: cifar10

accuracy: 0.881

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/squeezenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/squeezenet_ascend_v111_cifar10_offical_cv_bs32_acc84/squeezenet_ascend_v111_cifar10_offical_cv_bs32_acc84.ckpt>
    asset-sha256: cbf2874848fb159e2cfd2658aff664115dfc953353c0104bcc9ef96323c35049

license: Apache2.0

summary: AlexNet used to classify the 10 classes of cifar10.

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/squeezenet.

squeezenet is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/squeezenet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/squeezenet/README.md).

All parameters in the module are trainable.

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

model = "mindspore/ascend/1.1/squeezenet_v1.1_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Forrest N. Iandola and Song Han and Matthew W. Moskewicz and Khalid Ashraf and William J. Dally and Kurt Keutzer.
   "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size"
