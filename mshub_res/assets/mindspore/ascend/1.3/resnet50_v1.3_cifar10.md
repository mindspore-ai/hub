# resnet

---

model-name: resnet50

backbone-name: resnet50

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: cifar10

accuracy: 57.86

author: MindSpore team

update-time: 2021-09-28

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/resnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/resnet50_ascend_v130_cifar10_official_cv_bs32_top1acc57.86__top5acc95.02/resnet50_ascend_v130_cifar10_official_cv_bs32_top1acc57.86__top5acc95.02.ckpt>
    asset-sha256: fce4ad582a988602b515c3216de47e5c98cd93df8cd5d6ec6ece3c09c0791ae5

license: Apache2.0

summary: resnet50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet50 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

resnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/resnet/README.md).

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

model = "mindspore/ascend/1.3/resnet50_v1.3_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, dataset="cifar10")
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"
