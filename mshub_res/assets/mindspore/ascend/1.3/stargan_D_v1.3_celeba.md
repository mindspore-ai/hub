# StarGAN

---

model-name: StarGAN

backbone-name: StarGAN

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: celeba

accuracy: 0

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/StarGAN>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/stargan_D_ascend_v130_celeba_research_cv_bs4_acc0/stargan_D_ascend_v130_celeba_research_cv_bs4_acc0.ckpt>
    asset-sha256: 13c9dce4b8151f8176aba4b4cd494ec7fcc443f39c7b9b43b5fa25a72e3e00d9

license: Apache2.0

summary: StarGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of StarGAN from the MindSpore model zoo on Gitee at model_zoo/research/cv/StarGAN.

StarGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/StarGAN](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/StarGAN/README.md).

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

model = "mindspore/ascend/1.3/stargan_D_v1.3_celeba"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, style="D")
network.set_train(False)

# ...
```

## Citation

1. Yunjey Choi, Minje Choi, Munyoung Kim, Jung-Woo Ha, Sunghun Kim, Jaegul Choo. StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation
