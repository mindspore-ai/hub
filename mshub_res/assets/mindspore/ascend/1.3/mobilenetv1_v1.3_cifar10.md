# mobilenetv1

---

model-name: mobilenetv1

backbone-name: mobilenetv1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: cifar10

accuracy: 93.17

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/mobilenetv1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/temp/mobilenetv1_ascend_v130_cifar10_official_cv_bs32_acctop1%3D93.17_top5%3D99.81/mobilenetv1_ascend_v130_cifar10_official_cv_bs32_acctop1%3D93.17_top5%3D99.81.ckpt>
    asset-sha256: 88aa89d6183c7268981ca7b0f4f7e17b851a1e0c4870a852f81252ae3a4b5057

license: Apache2.0

summary: mobilenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv1 from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv1.

mobilenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/mobilenetv1](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/mobilenetv1/README.md).

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

model = "mindspore/ascend/1.3/mobilenetv1_v1.3_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, class_num=10)
network.set_train(False)

# ...
```

## Citation

1. Howard A G , Zhu M , Chen B , et al. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications[J]. 2017.
