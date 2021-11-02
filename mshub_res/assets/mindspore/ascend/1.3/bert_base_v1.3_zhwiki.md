# bert

---

model-name: bert_base

backbone-name: bert

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: zhwiki

accuracy: 91.72

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/nlp/bert>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/bert_base_ascend_v130_zhwiki_official_nlp_bs256_acc91.72_recall95.06_F1score93.36/bert_base_ascend_v130_zhwiki_official_nlp_bs256_acc91.72_recall95.06_F1score93.36.ckpt>
    asset-sha256: 83d56308422e7dbb10dad3382f1422ba97054f77df639ea81ad86585ee11b942

license: Apache2.0

summary: bert is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of bert from the MindSpore model zoo on Gitee at model_zoo/official/nlp/bert.

bert is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/bert](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/nlp/bert/README.md).

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

model = "mindspore/ascend/1.3/bert_base_v1.3_zhwiki"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding]((https://arxiv.org/abs/1810.04805)). arXiv preprint arXiv:1810.04805.
