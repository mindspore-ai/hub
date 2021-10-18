# Glore_resnet200

---

model-name: Glore_resnet200

backbone-name: Glore_resnet200

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 79.95

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/Glore_resnet200>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/gloreresnet200_ascend_v130_imagenet2012_research_cv_bs128_top1acc79.95__top5acc94.89/gloreresnet200_ascend_v130_imagenet2012_research_cv_bs128_top1acc79.95__top5acc94.89.ckpt>
    asset-sha256: 106bba976cc6f7d5d59a74a63062d5600165090763fcfebc96af507b15c24dfb

license: Apache2.0

summary: Glore_resnet200 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Glore_resnet200 from the MindSpore model zoo on Gitee at model_zoo/research/cv/Glore_resnet200.

Glore_resnet200 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/Glore_resnet200](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/Glore_resnet200/README_CN.md).

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

model = "mindspore/ascend/1.3/gloreresnet200_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Yunpeng Chen, Marcus Rohrbach, Zhicheng Yan, Shuicheng Yan, Jiashi Feng, Yannis Kalantidis. Graph-Based Global Reasoning Networks
