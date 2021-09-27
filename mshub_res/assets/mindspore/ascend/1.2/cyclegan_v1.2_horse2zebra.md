# CycleGAN

---

model-name: CycleGAN

backbone-name: CycleGAN

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: horse2zebra

accuracy: 0

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/CycleGAN>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/cyclegan_ascend_v120_horse2zebra_research_cv_bs1_acc0/cyclegan_ascend_v120_horse2zebra_research_cv_bs1_acc0.ckpt>
    asset-sha256: 7c902214cb584f1290f1f3ed81facdd18d30942bad1159650252a4e99793573c

license: Apache2.0

summary: CycleGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of CycleGAN from the MindSpore model zoo on Gitee at model_zoo/research/cv/CycleGAN.

CycleGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/CycleGAN](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/CycleGAN/README.md).

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

model = "mindspore/ascend/1.2/cyclegan_v1.2_horse2zebra"
# initialize the number of classes based on the pre-trained model
discriminator = mshub.load(model, trainable=True, style="D")
generator = mshub.load(model, trainable=True, style="G")

# ...
```

## Citation

1. Zhu J Y , Park T , Isola P , et al. Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks[J]. 2017.
