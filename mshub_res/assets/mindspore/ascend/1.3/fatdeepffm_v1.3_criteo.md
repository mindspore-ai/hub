# Fat-DeepFFM

---

model-name: Fat-DeepFFM

backbone-name: Fat-DeepFFM

module-type: recommend

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: criteo

accuracy: 80.91

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/recommend/Fat-DeepFFM>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/fatdeepffm_ascend_v130_criteo_research_recommend_bs1000_acc80.91/fatdeepffm_ascend_v130_criteo_research_recommend_bs1000_acc80.91.ckpt>
    asset-sha256: c347768ae3632983113fdf0583aa766db4300cd9abd9653699d135bfcd8dc938

license: Apache2.0

summary: Fat-DeepFFM is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of Fat-DeepFFM from the MindSpore model zoo on Gitee at model_zoo/research/recommend/Fat-DeepFFM.

Fat-DeepFFM is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/recommend/Fat-DeepFFM](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/recommend/Fat-DeepFFM/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/fatdeepffm_v1.3_criteo"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, isTrained=False)
network.set_train(False)

# ...
```

## Citation

1. Junlin Zhang , Tongwen Huang , Zhiqi Zhang FAT-DeepFFM: Field Attentive Deep Field-aware Factorization Machine
