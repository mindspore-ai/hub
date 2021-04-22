# wide_and_deep

---

model-name: wide_and_deep

backbone-name: wide_and_deep

module-type: recommend

fine-tunable: True

input-shape: [[16000, 39], [16000, 39]]

model-version: 1.1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/recommend/wide_and_deep>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/widedeep_ascend_v111_offical_recommend_bs16000_acc80/widedeep_ascend_v111_offical_recommend_bs16000_acc80.ckpt>
    asset-sha256: fcdca8cedf9d9900055f6ca776a7ff415ee1356e4d9a4f55fe30a616d1becc5a

license: Apache2.0

summary: wide_and_deep used in recommend system

---

## Introduction

This MindSpore Hub model uses the implementation of wide&deep from the MindSpore model zoo on Gitee at [model_zoo/official/recommend/wide_and_deep](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/recommend/wide_and_deep/README.md).

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/widedeep_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Cheng H T , Koc L , Harmsen J , et al. Wide & Deep Learning for Recommender Systems[J]. 2016.