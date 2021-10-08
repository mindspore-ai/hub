# simclr

---

model-name: simclr

backbone-name: simclr

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: cifar10

accuracy: 85

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/simclr>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/simclr_ascend_v120_cifar10_official_cv_bs128_acc85/simclr_ascend_v120_cifar10_official_cv_bs128_acc85.ckpt>
    asset-sha256: f0d788a9dd66d496d2388f598a388645abdd8bd8ba31607f270ee30f1de0ac7b

license: Apache2.0

summary: simclr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simclr from the MindSpore model zoo on Gitee at model_zoo/official/cv/simclr.

simclr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/simclr](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/simclr/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)
# these parameter please refer the train file of the net.
width_multiplier = 1
projection_dimension = 128
dataset = "cifar10"

model = "mindspore/ascend/1.2/simclr_v1.2_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, width_multiplier, projection_dimension, dataset)
network.set_train(False)

# ...
```

## Citation

1. Ting Chen and Simon Kornblith and Mohammad Norouzi and Geoffrey Hinton. A Simple Framework for Contrastive Learning of Visual Representations. *arXiv preprint arXiv:2002.05709*. 2020.
