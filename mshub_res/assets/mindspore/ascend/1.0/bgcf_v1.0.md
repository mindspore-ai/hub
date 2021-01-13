# BGCF

---

model-name: bgcf

backbone-name: BGCF

module-type: recommend

fine-tunable: True

input-shape: [7068, 3570]

model-version: 1.0

author: MindSpore team

update-time: 2020-09-19

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/bgcf>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0

summary: BGCF used to recommend items.

---

## Introduction

This MindSpore Hub model uses the implementation of BGCF from the MindSpore model zoo on Gitee at model_zoo/official/gnn/bgcf.

More details pleas refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/mindspore/blob/master/model_zoo/official/gnn/bgcf/README.md)

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import parser_args

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/bgcf_v1.0"

config = parser_args()
config.num_user = 7068
config.num_item = 3570
network = mshub.load(model, [config.input_dim, config.num_user, config.num_item], config.embedded_dimension, config.activation, [0.0, 0.0, 0.0], config.num_user, config.num_item, config.input_dim)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/gnn/bgcf>.
```

## Citation

1. Sun J , Guo W , Zhang D , et al. A Framework for Recommending Accurate and Diverse Items Using Bayesian Graph Convolutional Neural Networks[C]// KDD '20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. ACM, 2020.
