# GCN

---

model-name: gcn

backbone-name: GCN

module-type: nlp

fine-tunable: True

input-shape: [3327, 3703, 6]

model-version: 1.1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/gnn/gcn>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/gcn_ascend_v111_citeseer_offical_gnn_acc70/gcn_ascend_v111_citeseer_offical_gnn_acc70.ckpt>
    asset-sha256: bed6b1f74537d96f90619a38826bf2ecbc8a12dac620a6935981a2fc113d2949

license: Apache2.0

summary: GCN used to text classification.

---

## Introduction

This MindSpore Hub model uses the implementation of GCN from the MindSpore model zoo on Gitee at model_zoo/official/gnn/gcn.

More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/gnn/gcn](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/gnn/gcn/README.md)

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from model_zoo.official.gnn.gcn.src.config import ConfigGCN

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/gcn_v1.1_citeseer"

config = ConfigGCN
input_dim = 3703
class_num = 6
network = mshub.load(model, config, input_dim, class_num)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/models/tree/master/official/gnn/gcn>.
```

## Citation

1. Kipf T N , Welling M . Semi-Supervised Classification with Graph Convolutional Networks[J]. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.