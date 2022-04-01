# gat

---

model-name: gat

backbone-name: gat

module-type: gnn

fine-tunable: True

model-version: 1.5

train-dataset: cora

evaluation: acc83.3

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/gnn/gat>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/gat_ascend_v150_cora_official_gnn_acc83.3.ckpt>
    asset-sha256: 366b1211c0cbd2e101b7ae5ab1969dd0bc1f09d41a2b646c0c56f3e50b3627c3

license: Apache2.0

summary: gat is used for gnn

---

## Introduction

This MindSpore Hub model uses the implementation of gat from the MindSpore model zoo on Gitee at official/gnn/gat.

gat is a gnn network. More details please refer to the MindSpore model zoo on Gitee at [official/gnn/gat](https://gitee.com/mindspore/models/blob/r1.5/official/gnn/gat/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/gat_cora"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2017).Graph attention networks. arXiv preprint arXiv:1710.10903.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
