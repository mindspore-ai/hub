# inceptionv3

---

model-name: inceptionv3

backbone-name: inceptionv3

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 78

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/inceptionv3>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/inceptionv3_ascend_v120_imagenet2012_official_cv_bs128_acc78/inceptionv3_ascend_v120_imagenet2012_official_cv_bs128_acc78.ckpt>
    asset-sha256: 10e76a957fff0c307a8a074af0730e1eea6c65e476f0ad37620950b3d7d18e0c

license: Apache2.0

summary: inceptionv3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of inceptionv3 from the MindSpore model zoo on Gitee at model_zoo/official/cv/inceptionv3.

inceptionv3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/inceptionv3](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/inceptionv3/README.md).

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

model = "mindspore/ascend/1.2/inceptionv3_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000)
network.set_train(False)

# ...
```

## Citation

1. Min Sun, Ali Farhadi, Steve Seitz. Ranking Domain-Specific Highlights by Analyzing Edited Videos[J]. 2014.
