# LeNet

---

model-name: LeNet

backbone-name: LeNet

module-type: cv-classification

fine-tunable: True

input-shape: [32, 32, 1]

model-version: 1.0

train-dataset: mnist

accuracy: 0.986

author: MindSpore team

update-time: 2020-09-21

repo-link: <https://gitee.com/mindspore/models/tree/master/official/cv/lenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/lenet/lenet_ascend_0.5.0_mnist_official_classification_20200716/lenet.ckpt>  
    asset-sha256: 7adc21461aa42d10b065eb8be9a5b420b0d1336f6b33a84086e94fd5de8c48c5

license: Apache2.0

summary: LeNet used to classify the 10 classes of mnist.

---

## Introduction

This MindSpore Hub model uses the implementation of LeNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/lenet.

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

model = "mindspore/ascend/0.7/lenet_v1_mnist"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based learning applied to document recognition." Proceedings of the IEEE, 86(11):2278-2324, November 1998.
