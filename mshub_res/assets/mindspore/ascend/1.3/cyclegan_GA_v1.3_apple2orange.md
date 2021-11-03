# CycleGAN

---

model-name: CycleGAN

backbone-name: CycleGAN

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: apple2orange

accuracy: 0

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/CycleGAN>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/cyclegan_GA_ascend_v130_apple2orange_research_cv_bs1_acc0/cyclegan_GA_ascend_v130_apple2orange_research_cv_bs1_acc0.ckpt>
    asset-sha256: 44bc99276b91d5113636c37a03e75d15daf6c836e6cc59be07507223f69f9a5d

license: Apache2.0

summary: CycleGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of CycleGAN from the MindSpore model zoo on Gitee at model_zoo/research/cv/CycleGAN.

CycleGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/CycleGAN](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/CycleGAN/README.md).

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

model = "mindspore/ascend/1.3/cyclegan_GA_v1.3_apple2orange"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, istrain="train", style="G_A")
network.set_train(False)

# ...
```

## Citation

1. Zhu J Y , Park T , Isola P , et al. Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks[J]. 2017.
