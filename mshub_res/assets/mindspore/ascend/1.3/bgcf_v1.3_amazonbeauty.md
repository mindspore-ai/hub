# bgcf

---

model-name: bgcf

backbone-name: bgcf

module-type: gnn

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: amazonbeauty

accuracy: 15.32

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/gnn/bgcf>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/bgcf_ascend_v130_amazonbeauty_official_gnn_bs5000_recall20acc15.32_nndcg20acc9.16/bgcf_ascend_v130_amazonbeauty_official_gnn_bs5000_recall20acc15.32_nndcg20acc9.16.ckpt>
    asset-sha256: 1ba27594e030d343d1c71cb5bc7ae6323d39c8d187226c88e9931d96ad786ba1

license: Apache2.0

summary: bgcf is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of bgcf from the MindSpore model zoo on Gitee at model_zoo/official/gnn/bgcf.

bgcf is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/gnn/bgcf](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/gnn/bgcf/README.md).

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

model = "mindspore/ascend/1.3/bgcf_v1.3_amazonbeauty"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Sun J, Guo W, Zhang D, et al. A Framework for Recommending Accurate and Diverse Items Using Bayesian Graph Convolutional Neural Networks[C]//Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 2020: 2030-2039.
