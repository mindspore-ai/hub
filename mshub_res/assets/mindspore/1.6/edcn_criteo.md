# EDCN

---

model-name: edcn

backbone-name: EDCN

module-type: recommend

fine-tunable: True

model-version: 1.6

train-dataset: criteo

evaluation: acc80.64

author: MindSpore team

update-time: 2022-07-21

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/recommend/EDCN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/edcn_ascend_v160_criteo_research_recommend_acc80.64.ckpt>
    asset-sha256: 80530e74c733c90186d62a34049730ed1f58cfa8048cd83d7e0abe7be19f9dfe

license: Apache2.0

summary: EDCN is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of EDCN from the MindSpore model zoo on Gitee at research/recommend/EDCN.

EDCN is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [research/recommend/EDCN](https://gitee.com/mindspore/models/blob/r1.6/research/recommend/EDCN/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/edcn_criteo"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Bo Chen*, Yichao Wang*, Zhirong Liu, Ruiming Tang, Wei Guo, Hongkun Zheng, Weiwei Yao, Muyu Zhang, Xiuqiang He. Enhancing Explicit and Implicit Feature Interactions via Information Sharing for Parallel Deep CTR Models

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
