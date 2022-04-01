# naml

---

model-name: naml

backbone-name: naml

module-type: recommend

fine-tunable: True

model-version: 1.6

train-dataset: mindlarge

evaluation: acc67

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/recommend/naml>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/naml_ascend_v160_mindlarge_official_recommend_acc67.ckpt>
    asset-sha256: 9d553eae6ce96f019148b69ed4ce3ebb665503d7f1eda7c4907e23242479cdce

license: Apache2.0

summary: naml is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of naml from the MindSpore model zoo on Gitee at official/recommend/naml.

naml is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [official/recommend/naml](https://gitee.com/mindspore/models/blob/r1.6/official/recommend/naml/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/naml_mindlarge"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Chuhan Wu, Fangzhao Wu, Mingxiao An, Jianqiang Huang, Yongfeng Huang and Xing Xie: Neural News Recommendation with Attentive Multi-View Learning, IJCAI 2019

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
