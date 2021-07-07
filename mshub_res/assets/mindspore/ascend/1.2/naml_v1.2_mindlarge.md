# naml

---

model-name: naml

backbone-name: naml

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: mindlarge

accuracy: 67

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/recommend/naml>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/naml_ascend_v120_mindlarge_official_recommend_bs64_acc67/naml_ascend_v120_mindlarge_official_recommend_bs64_acc67.ckpt>
    asset-sha256: 9d553eae6ce96f019148b69ed4ce3ebb665503d7f1eda7c4907e23242479cdce

license: Apache2.0

summary: naml is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of naml from the MindSpore model zoo on Gitee at model_zoo/official/recommend/naml.

naml is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/recommend/naml](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/recommend/naml/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/naml_v1.2_mindlarge"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Chuhan Wu, Fangzhao Wu, Mingxiao An, Jianqiang Huang, Yongfeng Huang and Xing Xie: Neural News Recommendation with Attentive Multi-View Learning, IJCAI 2019
