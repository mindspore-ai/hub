# glore_res50

---

model-name: glore_res50

backbone-name: glore_res50

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: imagenet2012

accuracy: 78.32

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/glore_res50>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/gloreres50_ascend_v130_imagenet2012_research_cv_bs128_top1acc78.32__top5acc94.02/gloreres50_ascend_v130_imagenet2012_research_cv_bs128_top1acc78.32__top5acc94.02.ckpt>
    asset-sha256: b2ee8e5bdf5059b9229d539c485c8da1437b23c7b5554970808ca99610631efd

license: Apache2.0

summary: glore_res50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of glore_res50 from the MindSpore model zoo on Gitee at model_zoo/research/cv/glore_res50.

glore_res50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/glore_res50](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/glore_res50/README.md).

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

model = "mindspore/ascend/1.3/gloreres50_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Yupeng Chen, Marcus Rohrbach, Zhicheng Yan, Shuicheng Yan, Jiashi Feng, Yannis Kalantidis."Deep Residual Learning for Image Recognition"
