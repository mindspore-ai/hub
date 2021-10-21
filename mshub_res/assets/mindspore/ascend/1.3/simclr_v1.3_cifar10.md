# simclr

---

model-name: simclr

backbone-name: simclr

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: cifar10

accuracy: 84

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/simclr>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/simclr_ascend_v130_cifar10_official_cv_bs128_acc84/simclr_ascend_v130_cifar10_official_cv_bs128_acc84.ckpt>
    asset-sha256: f990e701d64215c504bde64fd99a2d2c1f6c18926fb616866d303d962809a9c1

license: Apache2.0

summary: simclr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simclr from the MindSpore model zoo on Gitee at model_zoo/official/cv/simclr.

simclr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/simclr](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/simclr/README.md).

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

model = "mindspore/ascend/1.3/simclr_v1.3_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Ting Chen and Simon Kornblith and Mohammad Norouzi and Geoffrey Hinton. A Simple Framework for Contrastive Learning of Visual Representations. *arXiv preprint arXiv:2002.05709*. 2020.
