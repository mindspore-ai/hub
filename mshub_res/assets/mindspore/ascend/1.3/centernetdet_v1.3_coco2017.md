# centernet_det

---

model-name: centernet

backbone-name: centernet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: coco2017

accuracy: 41.5

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/centernet_det>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/centernetdet_ascend_v130_coco2017_research_cv_bs12_acc41.5/centernetdet_ascend_v130_coco2017_research_cv_bs12_acc41.5.ckpt>
    asset-sha256: 39ccffb7eae3cbcf2821fe093e3f48c9acde272669a7d9f90a2f08964514f4fd

license: Apache2.0

summary: centernet_det is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of centernet_det from the MindSpore model zoo on Gitee at model_zoo/research/cv/centernet_det.

centernet_det is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/centernet_det](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/centernet_det/README.md).

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

model = "mindspore/ascend/1.3/centernetdet_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Xingyi Zhou(UT Austin) and Dequan Wang(UC Berkeley) and Philipp Krahenbuhl(UT Austin). Objects as Points. 2019.
