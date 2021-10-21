# squeezenet1_1

---

model-name: squeezenet1_1

backbone-name: squeezenet1_1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: imagenet2012

accuracy: 58.51

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/squeezenet1_1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/squeezenet11_ascend_v130_imagenet2012_research_cv_bs32_top1acc58.51__top5acc80.82/squeezenet11_ascend_v130_imagenet2012_research_cv_bs32_top1acc58.51__top5acc80.82.ckpt>
    asset-sha256: c50c0293a9efbe2a9338bf41df6e8c399c4ef40511e9d27a5ebef83deea61252

license: Apache2.0

summary: squeezenet1_1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenet1_1 from the MindSpore model zoo on Gitee at model_zoo/research/cv/squeezenet1_1.

squeezenet1_1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/squeezenet1_1](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/squeezenet1_1/README.md).

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

model = "mindspore/ascend/1.3/squeezenet11_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Forrest N. Iandola and Song Han and Matthew W. Moskewicz and Khalid Ashraf and William J. Dally and Kurt Keutzer. "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size"
