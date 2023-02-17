# bgcf

---

model-name: bgcf

backbone-name: bgcf

module-type: gnn

fine-tunable: True

model-version: 1.10

train-dataset: amazonbeauty

evaluation: recall20acc15.32 | ndcg20acc9.16

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/gnn/bgcf>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/bgcf_ascend_v1100_amazonbeauty_official_gnn_recall20acc15.32_ndcg20acc9.16.ckpt>
    asset-sha256: 1ba27594e030d343d1c71cb5bc7ae6323d39c8d187226c88e9931d96ad786ba1

license: Apache2.0

summary: bgcf is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of bgcf from the MindSpore model zoo on Gitee at official/gnn/bgcf.

bgcf is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [official/gnn/bgcf](https://gitee.com/mindspore/models/blob/r1.10/official/gnn/bgcf/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/bgcf_amazonbeauty"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[A Framework for Recommending Accurate and Diverse ItemsUsing Bayesian Graph Convolutional Neural Networks](https://dl.acm.org/doi/abs/10.1145/3394486.3403254)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
