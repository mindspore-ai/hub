# advanced_east

---

model-name: advanced_east

backbone-name: advanced_east

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: icpr2018

accuracy: 92

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/advanced_east>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/advancedeast_ascend_v120_icpr2018_research_cv_bs2_f1acc92/advancedeast_ascend_v120_icpr2018_research_cv_bs2_f1acc92.ckpt>
    asset-sha256: a1dce3a1374701531199b7cb4a73112cd27f5b151b4e189de38c01d3e8c763de

license: Apache2.0

summary: advanced_east is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of advanced_east from the MindSpore model zoo on Gitee at model_zoo/research/cv/advanced_east.

advanced_east is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/advanced_east](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/advanced_east/README.md).

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

model = "mindspore/ascend/1.2/advancedeast_v1.2_icpr2018"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Xinyu Zhou, Cong Yao, He Wen, Yuzhi Wang, Shuchang Zhou, Weiran He, Jiajun Liang. EAST: An Efficient and Accurate Scene Text Detector
