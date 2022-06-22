# gcn

---

model-name: gcn

backbone-name: gcn

module-type: gnn

fine-tunable: True

model-version: 1.7

train-dataset: cora

evaluation: acc82.7

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/gnn/gcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/gcn_ascend_v170_cora_official_gnn_acc82.7.ckpt>
    asset-sha256: 5bf8a58e7129d0191c4e6c16d3eb346b6eb8885d5b7754b88fb8e959c9ae9876

license: Apache2.0

summary: gcn is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of gcn from the MindSpore model zoo on Gitee at official/gnn/gcn.

gcn is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [official/gnn/gcn](https://gitee.com/mindspore/models/blob/r1.7/official/gnn/gcn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/gcn_cora"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Thomas N. Kipf, Max Welling. 2016. Semi-Supervised Classification with Graph Convolutional Networks. In ICLR 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
