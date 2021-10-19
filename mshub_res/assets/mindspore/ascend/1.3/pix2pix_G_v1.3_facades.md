# Pix2Pix

---

model-name: Pix2Pix

backbone-name: Pix2Pix

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.3

train-dataset: facades

accuracy: 0

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/Pix2Pix>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/pix2pix_G_ascend_v130_facades_research_cv_bs1_acc0/pix2pix_G_ascend_v130_facades_research_cv_bs1_acc0.ckpt>
    asset-sha256: a0d6f51ba1f13be48c28991fad7a07a8ffbcd63bf23eb2125a7007ef67d54234

license: Apache2.0

summary: Pix2Pix is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Pix2Pix from the MindSpore model zoo on Gitee at model_zoo/research/cv/Pix2Pix.

Pix2Pix is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/Pix2Pix](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/Pix2Pix/README.md).

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



model = "mindspore/ascend/1.3/pix2pix_G_v1.3_facades"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. "Image-to-Image Translation with Conditional Adversarial Networks", in CVPR 2017.
