# resnetv2

---

model-name: resnetv2_101

backbone-name: resnetv2_101

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: cifar10

accuracy: 95

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/resnetv2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnetv2101_ascend_v120_cifar10_research_cv_bs32_acc95/resnetv2101_ascend_v120_cifar10_research_cv_bs32_acc95.ckpt>
    asset-sha256: 183f9e5feaef51c792c45f55ccafb2dd0467ae8809aee7537827d674c26633f5

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

model = "mindspore/ascend/1.2/resnetv2101_v1.2_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun."Identity Mappings in Deep Residual Networks"
