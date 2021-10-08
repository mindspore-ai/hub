# ghostnet

---

model-name: ghostnet

backbone-name: ghostnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 73.81

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/ghostnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/ghostnet_ascend_v130_imagenet2012_research_cv_bs128_top1acc73.81__top5acc91.77/ghostnet_ascend_v130_imagenet2012_research_cv_bs128_top1acc73.81__top5acc91.77.ckpt>
    asset-sha256: 612f2fee612654057734283a50ff9eb9c967ee838c1b2f3b9b555e1689f53851

license: Apache2.0

summary: ghostnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ghostnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/ghostnet.

ghostnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ghostnet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/ghostnet/README_CN.md).

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

model = "mindspore/ascend/1.3/ghostnet_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu. GhostNet: More Features from Cheap Operations. CVPR 2020.
