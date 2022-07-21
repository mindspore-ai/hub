# gcn

---

model-name: gcn

backbone-name: gcn

module-type: gnn

fine-tunable: True

model-version: 1.8

train-dataset: citesser

evaluation: acc71.9

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/gnn/gcn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/gcn_ascend_v180_citesser_official_gnn_acc71.9.ckpt>
    asset-sha256: 00cc8132de8f255591564040dbd655fc23e5826e0f6e350bd4e20ec85e910bf3

license: Apache2.0

summary: gcn is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of gcn from the MindSpore model zoo on Gitee at official/gnn/gcn.

gcn is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [official/gnn/gcn](https://gitee.com/mindspore/models/blob/r1.8/official/gnn/gcn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/gcn_citesser"
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
