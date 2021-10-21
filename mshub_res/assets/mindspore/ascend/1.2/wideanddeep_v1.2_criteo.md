# wide_and_deep

---

model-name: wide_and_deep

backbone-name: wide_and_deep

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: criteo

accuracy: 80

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/recommend/wide_and_deep>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/wideanddeep_ascend_v120_criteo_official_recommend_bs16000_acc80/wideanddeep_ascend_v120_criteo_official_recommend_bs16000_acc80.ckpt>
    asset-sha256: c0650ccd04daee76a8c1021813b9fecb4f25d386fd420fe1b75f849705481dcb

license: Apache2.0

summary: wide_and_deep is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of wide_and_deep from the MindSpore model zoo on Gitee at model_zoo/official/recommend/wide_and_deep.

wide_and_deep is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/recommend/wide_and_deep](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/recommend/wide_and_deep/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/wideanddeep_v1.2_criteo"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen, Tal Shaked, Tushar Chandra,Hrishi Aradhye, Glen Anderson, Greg Corrado, Wei Chai, Mustafa Ispir, Rohan Anil,Zakaria Haque, Lichan Hong, Vihan Jain, Xiaobing Liu, Hemal Shah. Wide & Deep Learning for Recommender Systems
