# resnet

---

model-name: resnet152

backbone-name: resnet152

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 78.72

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnet152>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnet152_ascend_v120_imagenet2012_official_cv_bs32_top1acc78.72__top5acc94.34/resnet152_ascend_v120_imagenet2012_official_cv_bs32_top1acc78.72__top5acc94.34.ckpt>
    asset-sha256: 840c362b02beed6ae85f09b0dd09c41a5e70c012b396ca3f942e41d1b272c67d

license: Apache2.0

summary: resnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

resnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnet152/README-CN.md).

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

model = "mindspore/ascend/1.2/resnet152_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"
