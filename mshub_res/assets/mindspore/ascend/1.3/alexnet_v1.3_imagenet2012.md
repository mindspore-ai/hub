# alexnet

---

model-name: alexnet

backbone-name: alexnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 57.45

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/alexnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/alexnet_ascend_v130_imagenet2012_official_cv_bs256_top1acc57.45__top5acc80/alexnet_ascend_v130_imagenet2012_official_cv_bs256_top1acc57.45__top5acc80.ckpt>
    asset-sha256: 363ce17938585048f0725d57372bcef2d167b4e4346cb39f1128434686f2b69f

license: Apache2.0

summary: alexnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of alexnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/alexnet.

alexnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/alexnet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/alexnet/README.md).

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

model = "mindspore/ascend/1.3/alexnet_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000)
network.set_train(False)

# ...
```

## Citation

1. Krizhevsky A, Sutskever I, Hinton G E. ImageNet Classification with Deep ConvolutionalNeural Networks. Advances In Neural Information Processing Systems.2012.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
