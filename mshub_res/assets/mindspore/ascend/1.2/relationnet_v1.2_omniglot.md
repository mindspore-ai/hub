# relationnet

---

model-name: relationnet

backbone-name: relationnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: omniglot

accuracy: 99

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/relationnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/relationnet_ascend_v120_omniglot_research_cv_bs20_acc99/relationnet_ascend_v120_omniglot_research_cv_bs20_acc99.ckpt>
    asset-sha256: f18c8a3eb7e1a1a4cdeb8296486abaa954ae9f370b790ebd021b5ca17ea76c98

license: Apache2.0

summary: relationnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of relationnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/relationnet.

relationnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/relationnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/relationnet/README.md).

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

model = "mindspore/ascend/1.2/relationnet_v1.2_omniglot"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Flood Sung, Yongxin Yang, Li Zhang, Tao Xiang, Philip H.S. Torr, Timothy M. Hospedales. Learning to Compare: Relation Network for Few-Shot Learning
