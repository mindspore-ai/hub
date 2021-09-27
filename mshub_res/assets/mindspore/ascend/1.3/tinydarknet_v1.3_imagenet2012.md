# tinydarknet

---

model-name: tinydarknet

backbone-name: tinydarknet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 59.0

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/tinydarknet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/tinydarknet_ascend_v130_imagenet2012_official_cv_bs128_acctop1%3D59.0_top5%3D81.84/tinydarknet_ascend_v130_imagenet2012_official_cv_bs128_acctop1%3D59.0_top5%3D81.84.ckpt>
    asset-sha256: 00a1544972eaeecec147e15dfa49c1796368c054776d59a73a7e905c285b6256

license: Apache2.0

summary: tinydarknet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of tinydarknet from the MindSpore model zoo on Gitee at model_zoo/official/cv/tinydarknet.

tinydarknet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/tinydarknet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/tinydarknet/README.md).

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

model = "mindspore/ascend/1.3/tinydarknet_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1001)
network.set_train(False)

# ...
```

## Citation

1. You Only Look Once: Unified, Real-Time Object Detection. Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi
