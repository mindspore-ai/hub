# GoogleNet

---

model-name: GoogleNet

backbone-name: GoogleNet

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: cifar10

accuracy: 0.92

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/googlenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/googlenet_ascend_v111_cifar10_offical_cv_bs128_acc92/googlenet_ascend_v111_cifar10_offical_cv_bs128_acc92.ckpt>
    asset-sha256: c1ef96eff71a1eedc8d0d2934a49a9ce96a43ddde4e5ea778675984317d57f4f

license: Apache2.0

summary: GoogleNet used to classify the 10 classes of cifar10.

---

## Introduction

This MindSpore Hub model uses the implementation of googlenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/googlenet.

googlenet is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/googlenet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/googlenet/README.md).

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

model = "mindspore/ascend/1.1/googlenet_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=10)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Szegedy C, Liu W, Jia Y, et al. Going deeper with convolutions[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 1-9.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
