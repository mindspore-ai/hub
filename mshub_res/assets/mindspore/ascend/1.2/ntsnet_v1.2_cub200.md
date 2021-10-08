# ntsnet

---

model-name: ntsnet

backbone-name: ntsnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: cub200

accuracy: 87

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/ntsnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ntsnet_ascend_v120_cub2002011_research_cv_bs8_acc87/ntsnet_ascend_v120_cub2002011_research_cv_bs8_acc87.ckpt>
    asset-sha256: c9d7adb0ba63f97a9cb1b34655551766ff2c95bb5ae5436a9d34eb9b3749b3d8

license: Apache2.0

summary: ntsnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ntsnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/ntsnet.

ntsnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ntsnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/ntsnet/README.md).

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

model = "mindspore/ascend/1.2/ntsnet_v1.2_cub2002011"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Z. Yang, T. Luo, D. Wang, Z. Hu, J. Gao, and L. Wang, Learning to navigate for fine-grained classification, in Proceedings of the European Conference on Computer Vision (ECCV), 2018.
