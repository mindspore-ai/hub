# BGCF

---

model-name: bgcf

backbone-name: BGCF

module-type: recommend

fine-tunable: True

input-shape: [7068, 3570]

model-version: 1.1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/gnn/bgcf>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/bgcf_ascend_v111_amazonbeauty_offcial_gnn_bs12_5000_20recall_15/bgcf_ascend_v111_amazonbeauty_offcial_gnn_bs12_5000_20recall_15.81.ckpt>
    asset-sha256: 4d8c52d9b0b75e8c77972752a3df17b365356c5c8a88b51e3a7742da4d8528c0

license: Apache2.0

summary: BGCF used to recommend items.

---

## Introduction

This MindSpore Hub model uses the implementation of BGCF from the MindSpore model zoo on Gitee at model_zoo/official/gnn/bgcf.

More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/gnn/bgcf](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/gnn/bgcf/README.md)

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/bgcf_v1.1"

network = mshub.load(model)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/models/tree/master/official/gnn/bgcf>.
```

## Citation

1. Sun J , Guo W , Zhang D , et al. A Framework for Recommending Accurate and Diverse Items Using Bayesian Graph Convolutional Neural Networks[C]// KDD '20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. ACM, 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.