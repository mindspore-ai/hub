# arcface

---

model-name: arcface

backbone-name: arcface

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: ms1mv2

ijbb: 94.93

ijbc: 96.33

author: MindSpore team

update-time: 2021-09-23

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/arcface>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/arcface_ascend_v120_ms1mv2_research_cv_bs64_ijbb94.93_ijbc96.33/arcface_ascend_v120_ms1mv2_research_cv_bs64_ijbb94.93_ijbc96.33.ckpt>
    asset-sha256: 347f2183de414b90d93d8de5e26cc9a68e972d74ad3481ec7cbc720bc7f8d96b

license: Apache2.0

summary: arcface is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of arcface from the MindSpore model zoo on Gitee at model_zoo/research/cv/arcface.

arcface is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/arcface](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/arcface/README.md).

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

model = "mindspore/ascend/1.2/arcface_v1.2_ms1mv2"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Deng J ,  Guo J ,  Zafeiriou S . ArcFace: Additive Angular Margin Loss for Deep Face Recognition[J].  2018.
