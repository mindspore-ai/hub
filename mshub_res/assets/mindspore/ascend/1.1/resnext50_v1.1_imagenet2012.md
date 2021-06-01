# ResNeXt50

---

model-name: resnext50

backbone-name: resnext50

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: imagenet2012

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/resnext50>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/resnext50_ascend_v111_imagenet2012_offical_cv_bs128_acc78/resnext50_ascend_v111_imagenet2012_offical_cv_bs128_acc78.ckpt>
    asset-sha256: 581d3e7a97d408d4f690ef5f362e5435d853348f1f0f18c351931ab77e8f3e45

license: Apache2.0

summary: resnext50 for image classification

---

## Introduction

This MindSpore Hub model uses the implementation of resnext50 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnext50.

resnext50 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnext50](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/resnext50/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/resnext50_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Xie S, Girshick R, Dollár, Piotr, et al. Aggregated Residual Transformations for Deep Neural Networks. 2016.
