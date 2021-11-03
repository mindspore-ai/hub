# lstm

---

model-name: lstm

backbone-name: lstm

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: aclimdbv1

accuracy: 83.27

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/nlp/lstm>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/lstm_ascend_v130_aclimdbv1_official_nlp_bs64_acc83.27/lstm_ascend_v130_aclimdbv1_official_nlp_bs64_acc83.27.ckpt>
    asset-sha256: 1753803072319f6538e5850d309afcad306f15b3b0fee995ce2234f1a2bb7e7e

license: Apache2.0

summary: lstm is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of lstm from the MindSpore model zoo on Gitee at model_zoo/official/nlp/lstm.

lstm is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/lstm](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/nlp/lstm/README.md).

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

model = "mindspore/ascend/1.3/lstm_v1.3_aclimdbv1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts. [Learning Word Vectors for Sentiment Analysis](https://www.aclweb.org/anthology/P11-1015/). Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies. 2011
