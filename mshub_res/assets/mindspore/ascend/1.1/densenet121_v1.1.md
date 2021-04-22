# DenseNet121

---

model-name: DenseNet121

backbone-name: DenseNet121

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

accuracy: 0.754

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/densenet121>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

- file-format: mslite  
  asset-link: <https://download.mindspore.cn/model_zoo/r1.1/densenet121_ascend_v111_imagenet2012_offical_cv_bs32_acc75/densenet121_ascend_v111_imagenet2012_offical_cv_bs32_acc75.ckpt>
  asset-sha256: e7f17b626bc8f041dad67732cbff6c202a3bd57a0530fb5b91fa13fc8cdbc371

license: Apache2.0

summary: DenseNet121 used to classify the 1000 classes.

---

## Introduction

This MindSpore Hub model uses the implementation of DenseNet121 from the MindSpore model zoo on Gitee [model_zoo/official/cv/densenet121](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/densenet121/README.md).

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

model = "mindspore/ascend/1.1/densenet121_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000)
# network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Huang G , Liu Z , Laurens V D M , et al. Densely Connected Convolutional Networks[J]. 2016.
