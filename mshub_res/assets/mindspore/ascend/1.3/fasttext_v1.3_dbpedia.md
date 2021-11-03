# fasttext

---

model-name: fasttext

backbone-name: fasttext

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: dbpedia

accuracy: 98

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/nlp/fasttext>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/fasttext_ascend_v130_dbpedia_official_nlp_bs4096_acc98/fasttext_ascend_v130_dbpedia_official_nlp_bs4096_acc98.ckpt>
    asset-sha256: 3798190b1dbb78c4e76baac2b1228bab6c0e5ba5dfdede664fab47abc02d0b1e

license: Apache2.0

summary: fasttext is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of fasttext from the MindSpore model zoo on Gitee at model_zoo/official/nlp/fasttext.

fasttext is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/fasttext](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/nlp/fasttext/README.md).

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

model = "mindspore/ascend/1.3/fasttext_v1.3_dbpedia"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Bag of Tricks for Efficient Text Classification, 2016, A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov
