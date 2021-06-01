# LeNet

---

model-name: LeNet

backbone-name: LeNet

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 1]

model-version: 1.1

train-dataset: mnist

accuracy: 0.98

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/lenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/lenet_ascend_v111_offical_cv_mnist_bs32_acc98/lenet_ascend_v111_offical_cv_mnist_bs32_acc98.ckpt>
    asset-sha256: a314eb568eb8ccc8b3c9002f26685f20b6aa3e7c72418212a5e166a561a3e6bb

license: Apache2.0

summary: LeNet used to classify the 10 classes of mnist.

---

## Introduction

This MindSpore Hub model uses the implementation of LeNet from the MindSpore model zoo on Gitee at [model_zoo/official/cv/lenet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/lenet/README.md)..

This model has been trained on mnsit using the code published on Gitee.

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

model = "mindspore/ascend/1.1/LeNet_v1.1_mnist"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based learning applied to document recognition." Proceedings of the IEEE, 86(11):2278-2324, November 1998.
