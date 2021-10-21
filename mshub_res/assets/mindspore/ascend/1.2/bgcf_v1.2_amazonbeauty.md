# bgcf

---

model-name: bgcf

backbone-name: bgcf

module-type: gnn

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: amazonbeauty

accuracy: 15

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/gnn/bgcf>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/bgcf_ascend_v120_amazonbeauty_official_gnn_bs60000_recall20acc15_ndcg20acc9/bgcf_ascend_v120_amazonbeauty_official_gnn_bs60000_recall20acc15_ndcg20acc9.ckpt>
    asset-sha256: c9f75cb6c855b97637ee3e3dae0c350bec51704db9e1aa0d8ba7ae449187066e

license: Apache2.0

summary: bgcf is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of bgcf from the MindSpore model zoo on Gitee at model_zoo/official/gnn/bgcf.

bgcf is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/gnn/bgcf](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/gnn/bgcf/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/bgcf_v1.2_amazonbeauty"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Sun J, Guo W, Zhang D, et al. A Framework for Recommending Accurate and Diverse Items Using Bayesian Graph Convolutional Neural Networks[C]//Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. 2020: 2030-2039.
