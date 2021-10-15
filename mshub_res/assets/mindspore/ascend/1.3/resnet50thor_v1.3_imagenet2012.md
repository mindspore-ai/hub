# resnet_thor

---

model-name: resnet50_thor

backbone-name: resnet50_thor

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 76.08

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/resnet_thor>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/resnet50thor_ascend_v130_imagenet2012_official_cv_bs32_top1acc76.08__top5acc92.81/resnet50thor_ascend_v130_imagenet2012_official_cv_bs32_top1acc76.08__top5acc92.81.ckpt>
    asset-sha256: ad9b3b0bef58cbc204493b84dd0da3972acdceb4d273233a99f890adbc905ffc

license: Apache2.0

summary: resnet_thor is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet_thor from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet_thor.

resnet_thor is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet_thor](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/resnet_thor/README.md).

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

model = "mindspore/ascend/1.3/resnet50thor_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, class_num=1001)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. Deep Residual Learning for Image Recognition.
