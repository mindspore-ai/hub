# emotect

---

model-name: emotect

backbone-name: emotect

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: baiduzijianshujuji

accuracy: 90

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/emotect>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/emotect_ascend_v120_baiduzijianshujuji_official_nlp_bs32_acc90/emotect_ascend_v120_baiduzijianshujuji_official_nlp_bs32_acc90.ckpt>
    asset-sha256: 99aa4ff934fc93d0d59db7a79a2f2c51d081ba1288948669e3609caebee464e0

license: Apache2.0

summary: emotect is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of emotect from the MindSpore model zoo on Gitee at model_zoo/official/nlp/emotect.

emotect is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/emotect](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/emotect/README.md).

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

model = "mindspore/ascend/1.2/emotect_v1.2_baiduzijianshujuji"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
