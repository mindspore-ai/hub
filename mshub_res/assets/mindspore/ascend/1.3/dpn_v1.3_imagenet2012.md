# dpn

---

model-name: dpn

backbone-name: dpn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: imagenet2012

accuracy: 78.81

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/dpn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/dpn_ascend_v130_imagenet2012_official_cv_bs32_acctop1%3D78.81_top5%3D94.34/dpn_ascend_v130_imagenet2012_official_cv_bs32_acctop1%3D78.81_top5%3D94.34.ckpt>
    asset-sha256: 3fa441570f3a6ca0b8cc03dc4205bd881dafad4d8780daf153beec501947b9b2

license: Apache2.0

summary: dpn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of dpn from the MindSpore model zoo on Gitee at model_zoo/official/cv/dpn.

dpn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/dpn](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/dpn/README.md).

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

model = "mindspore/ascend/1.3/dpn_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Yunpeng Chen, Jianan Li, Huaxin Xiao, Xiaojie Jin, Shuicheng Yan, Jiashi Feng. Dual Path Networks
