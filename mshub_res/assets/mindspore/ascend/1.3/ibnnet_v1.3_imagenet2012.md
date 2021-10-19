# ibnnet

---

model-name: ibnnet

backbone-name: ibnnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: imagenet2012

accuracy: 77.13

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/ibnnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/ibnnet_ascend_v130_imagenet2012_research_cv_bs64_top1acc77.13__top5acc93.59/ibnnet_ascend_v130_imagenet2012_research_cv_bs64_top1acc77.13__top5acc93.59.ckpt>
    asset-sha256: c9ab6f1198b1b930fb2df92715134de798e103c1dd66bca06f3ee826b1a9983e

license: Apache2.0

summary: ibnnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ibnnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/ibnnet.

ibnnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ibnnet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/ibnnet/README_CN.md).

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

model = "mindspore/ascend/1.3/ibnnet_v1.3_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Pan X ,  Ping L ,  Shi J , et al. Two at Once: Enhancing Learning and Generalization Capacities via IBN-Net[C]// European Conference on Computer Vision. Springer, Cham, 2018.
