# gat

---

model-name: gat

backbone-name: gat

module-type: gnn

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: cora

accuracy: 83

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/gnn/gat>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/gat_ascend_v120_cora_official_gnn_bs1_acc83/gat_ascend_v120_cora_official_gnn_bs1_acc83.ckpt>
    asset-sha256: a39757942143b7a55e1473485684ee6164aaca7c6894b64059ec8ed46c7f4ec2

license: Apache2.0

summary: gat is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of gat from the MindSpore model zoo on Gitee at model_zoo/official/gnn/gat.

gat is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/gnn/gat](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/gnn/gat/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

feature_dims = 1433
num_class = 7
num_nodes = 30

model = "mindspore/ascend/1.2/gat_v1.2_cora"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, ftr_dims=feature_dims, num_class=num_class, num_nodes=num_nodes)
network.set_train(False)

# ...
```

## Citation

1. Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2017). Graph attention networks. arXiv preprint arXiv:1710.10903.
