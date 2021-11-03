# SE-Net

---

model-name: SE-Net

backbone-name: SE-Net

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: imagenet2012

accuracy: 77.74

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/SE-Net>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/senet_ascend_v130_imagenet2012_research_cv_bs256_top1acc77.74__top5acc93.99/senet_ascend_v130_imagenet2012_research_cv_bs256_top1acc77.74__top5acc93.99.ckpt>
    asset-sha256: 67308b5ae44a2c7e27984abe72abe294223c31562ddcf32cdf714ad863a49125

license: Apache2.0

summary: SE-Net is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of SE-Net from the MindSpore model zoo on Gitee at model_zoo/research/cv/SE-Net.

SE-Net is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/SE-Net](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/SE-Net/README.md).

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

model = "mindspore/ascend/1.3/senet_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Enhua Wu. "Squeeze-and-Excitation Networks"
