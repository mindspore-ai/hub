# gnmt_v2

---

model-name: gnmt

backbone-name: gnmt_v2

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: wmtende

accuracy: 24

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/nlp/gnmt_v2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/gnmtv2_ascend_v130_wmtende_official_nlp_bs6400_acc24/gnmtv2_ascend_v130_wmtende_official_nlp_bs6400_acc24.ckpt>
    asset-sha256: 48546b769601e39e380c2ec3916930501195e200fe84f1ef04d91725b4380e1a

license: Apache2.0

summary: gnmt_v2 is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of gnmt_v2 from the MindSpore model zoo on Gitee at model_zoo/official/nlp/gnmt_v2.

gnmt_v2 is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/gnmt_v2](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/nlp/gnmt_v2/README.md).

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

model = "mindspore/ascend/1.3/gnmtv2_v1.3_wmtende"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le, Mohammad Norouzi, Wolfgang Macherey, etc at all. Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation
