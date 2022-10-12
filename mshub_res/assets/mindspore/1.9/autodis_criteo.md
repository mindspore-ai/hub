# autodis

---

model-name: autodis

backbone-name: autodis

module-type: recommend

fine-tunable: True

model-version: 1.9

train-dataset: criteo

evaluation: acc80.90

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/recommend/autodis>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/autodis_ascend_v190_criteo_research_recommend_acc80.90.ckpt>
    asset-sha256: 741137e75c0f59f47010d63a614cfd6487a1a744cc7a143a1613a7fc66aac2c4

license: Apache2.0

summary: autodis is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of autodis from the MindSpore model zoo on Gitee at research/recommend/autodis.

autodis is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [research/recommend/autodis](https://gitee.com/mindspore/models/blob/r1.9/research/recommend/autodis/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/autodis_criteo"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Huifeng Guo*, Bo Chen*, Ruiming Tang, Zhenguo Li, Xiuqiang He. AutoDis: Automatic Discretization for Embedding Numerical Features in CTR Prediction

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
