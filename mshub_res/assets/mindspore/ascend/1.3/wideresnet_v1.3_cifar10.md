# wideresnet

---

model-name: wideresnet

backbone-name: wideresnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: cifar10

accuracy: 96.33

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/wideresnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/wideresnet_ascend_v130_cifar10_research_cv_bs32_acc96.33/wideresnet_ascend_v130_cifar10_research_cv_bs32_acc96.33.ckpt>
    asset-sha256: 441c0aaa59b9e164be0666d5a318fc438532e7fd13730cfa0b6cb677a8217442

license: Apache2.0

summary: wideresnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wideresnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/wideresnet.

wideresnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/wideresnet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/wideresnet/README_CN.md).

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

model = "mindspore/ascend/1.3/wideresnet_v1.3_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Sergey Zagoruyko."Wide Residual Netwoks"
