# resnetv2

---

model-name: resnetv2_50

backbone-name: resnetv2_50

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: cifar10

accuracy: 95.2

author: MindSpore team

update-time: 2021-09-23

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/resnetv2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnetv250_ascend_v120_cifar10_research_cv_bs32_top1acc95.2__top5acc99.82/resnetv250_ascend_v120_cifar10_research_cv_bs32_top1acc95.2__top5acc99.82.ckpt>
    asset-sha256: d88993343168c69ee523052b7cd605fd0c7cb426dff6f033d7e2be068d05a9a3

license: Apache2.0

summary: resnetv2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnetv2 from the MindSpore model zoo on Gitee at model_zoo/research/cv/resnetv2.

resnetv2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/resnetv2](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/resnetv2/README_CN.md).

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

model = "mindspore/ascend/1.2/resnetv250_v1.2_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun."Identity Mappings in Deep Residual Networks"
