# inception_resnet_v2

---

model-name: inception_resnet_v2

backbone-name: inception_resnet_v2

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: imagenet2012

accuracy: 80.04

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/inception_resnet_v2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/inceptionresnetv2_ascend_v130_imagenet2012_research_cv_bs128_top1acc80.04__top5acc94.54/inceptionresnetv2_ascend_v130_imagenet2012_research_cv_bs128_top1acc80.04__top5acc94.54.ckpt>
    asset-sha256: cf282d78635945173a79accf2068b0c651aff1253eeae556f31428190b7e3dbd

license: Apache2.0

summary: inception_resnet_v2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of inception_resnet_v2 from the MindSpore model zoo on Gitee at model_zoo/research/cv/inception_resnet_v2.

inception_resnet_v2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/inception_resnet_v2](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/inception_resnet_v2/README.md).

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

model = "mindspore/ascend/1.3/inceptionresnetv2_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Computer Vision and Pattern Recognition[J]. 2016. Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi.
