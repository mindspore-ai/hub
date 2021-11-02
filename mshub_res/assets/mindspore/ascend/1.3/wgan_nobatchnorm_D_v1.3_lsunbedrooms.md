# wgan

---

model-name: wgan

backbone-name: wgan

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: lsunbedrooms

accuracy: 0

author: MindSpore team

update-time: 2021-09-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/research/cv/wgan>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/wgan_nobatchnorm_D_ascend_v130_lsunbedrooms_research_cv_bs64_acc0/wgan_nobatchnorm_D_ascend_v130_lsunbedrooms_research_cv_bs64_acc0.ckpt>
    asset-sha256: 4885511962a988287e3ca1ffb703f2ab99844a6035a2b94c8e73fac29c16f25b

license: Apache2.0

summary: wgan is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wgan from the MindSpore model zoo on Gitee at model_zoo/research/cv/wgan.

wgan is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/wgan](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/research/cv/wgan/README_CN.md).

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

model = "mindspore/ascend/1.3/wgan_nobatchnorm_D_v1.3_lsunbedrooms"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, isTrain=True ,isNoBN=True, style="D")
network.set_train(False)

# ...
```

## Citation

1. Martin Arjovsky, Soumith Chintala, Léon Bottou. "Wasserstein GAN"*In International Conference on Machine Learning(ICML 2017).
