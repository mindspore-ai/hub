# GCN

---

model-name: gcn

backbone-name: GCN

module-type: nlp

fine-tunable: True

input-shape: [2708, 1433, 7]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-19

repo-link: <https://gitee.com/mindspore/models/tree/master/official/gnn/gcn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

license: Apache2.0

summary: GCN used to text classification.

---

## Introduction

This MindSpore Hub model uses the implementation of GCN from the MindSpore model zoo on Gitee at model_zoo/official/gnn/gcn.

More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/models/blob/master/official/gnn/gcn/README.md)

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import ConfigGCN

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/gcn_v1.0_cora"

config = ConfigGCN
input_dim = 1433
class_num = 7
network = mshub.load(model, config, input_dim, class_num)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/models/tree/master/official/gnn/gcn>.
```

## Citation

1. Kipf T N , Welling M . Semi-Supervised Classification with Graph Convolutional Networks[J]. 2016.
