# autodis

---

model-name: autodis

backbone-name: autodis

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: criteo

accuracy: 81

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/recommend/autodis>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/autodis_ascend_v120_criteo_research_recommend_bs1000_acc81/autodis_ascend_v120_criteo_research_recommend_bs1000_acc81.ckpt>
    asset-sha256: 44054ca5950f7eff124445c04db02e59c99bfbe3055c36985292497aee571d2c

license: Apache2.0

summary: autodis is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of autodis from the MindSpore model zoo on Gitee at model_zoo/research/recommend/autodis.

autodis is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/recommend/autodis](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/recommend/autodis/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/autodis_v1.2_criteo"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Huifeng Guo*, Bo Chen*, Ruiming Tang, Zhenguo Li, Xiuqiang He. AutoDis: Automatic Discretization for Embedding Numerical Features in CTR Prediction