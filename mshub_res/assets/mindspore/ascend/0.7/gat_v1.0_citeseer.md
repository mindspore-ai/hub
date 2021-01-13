# GAT

---

model-name: gat

backbone-name: GAT

module-type: nlp

fine-tunable: True

input-shape: [3327, 3703, 6]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-19

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/gat>

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

More details pleas refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/gnn/gat/README.md)

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

model = "mindspore/ascend/1.0/gat_v1.0_citeseer"

config = GatConfig
config.feature_size = 3703
config.num_class = 6
config.num_nodes = 3327
network = mshub.load(model, config.feature_size, config.num_class, config.num_nodes,
                     config.hid_units, config.n_heads, 0.0, 0.0)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/gat>.
```

## Citation

1. Velikovi P , Cucurull G , Casanova A , et al. Graph Attention Networks[J]. 2017.
