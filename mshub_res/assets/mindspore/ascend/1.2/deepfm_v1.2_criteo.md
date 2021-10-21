# deepfm

---

model-name: deepfm

backbone-name: deepfm

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: criteo

accuracy: 80

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/recommend/deepfm>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/deepfm_ascend_v120_criteo_official_recommend_bs16000_acc80/deepfm_ascend_v120_criteo_official_recommend_bs16000_acc80.ckpt>
    asset-sha256: a466dc4b2dd6ae2b3942c31df7613a588cb9d0fa4cfb5a8d74b293f4faa37430

license: Apache2.0

summary: deepfm is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of deepfm from the MindSpore model zoo on Gitee at model_zoo/official/recommend/deepfm.

deepfm is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/recommend/deepfm](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/recommend/deepfm/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/deepfm_v1.2_criteo"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, Xiuqiang He. DeepFM: A Factorization-Machine based Neural Network for CTR Prediction
