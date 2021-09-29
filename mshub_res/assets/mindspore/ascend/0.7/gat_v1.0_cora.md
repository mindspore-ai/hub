# GAT

---

model-name: gat

backbone-name: GAT

module-type: nlp

fine-tunable: True

input-shape: [2708, 1433, 7]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-19

repo-link: <https://gitee.com/mindspore/models/tree/master/official/gnn/gat>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

license: Apache2.0

summary: GAT used to text classification.

---

## Introduction

This MindSpore Hub model uses the implementation of GAT from the MindSpore model zoo on Gitee at model_zoo/official/gnn/gat.

More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/models/blob/master/official/gnn/gat/README.md)

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import GatConfig

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/gat_v1.0_cora"

config = GatConfig
config.feature_size = 1433
config.num_class = 7
config.num_nodes = 2708
network = mshub.load(model, config.feature_size, config.num_class, config.num_nodes,
                     config.hid_units, config.n_heads, 0.0, 0.0)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/models/tree/master/official/gnn/gat>.
```

## Citation

1. Velikovi P , Cucurull G , Casanova A , et al. Graph Attention Networks[J]. 2017.
