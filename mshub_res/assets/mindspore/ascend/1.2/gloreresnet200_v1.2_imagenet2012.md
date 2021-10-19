# glore_res200

---

model-name: glore_res200

backbone-name: glore_res200

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 80

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/Glore_resnet200>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/gloreresnet200_ascend_v120_imagenet2012_research_cv_bs128_acc80/gloreresnet200_ascend_v120_imagenet2012_research_cv_bs128_acc80.ckpt>
    asset-sha256: 5182f2b873b71f05fd1aa55abafabc00668374c519ef161b284ba4df475ba6f7

license: Apache2.0

summary: Glore_resnet200 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Glore_resnet200 from the MindSpore model zoo on Gitee at model_zoo/research/cv/Glore_resnet200.

Glore_resnet200 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/Glore_resnet200](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/Glore_resnet200/README_CN.md).

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

model = "mindspore/ascend/1.2/gloreresnet200_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Deep Residual Learning for Image Recognition.Yupeng Chen, Marcus Rohrbach, Zhicheng Yan, Shuicheng Yan, Jiashi Feng, Yannis Kalantidis.
