# efficientnet-b0

---

model-name: efficientnet-b0

backbone-name: efficientnet-b0

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 76

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/efficientnet-b0>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/efficientnet-b0_ascend_v111_imagenet2012_research_cv_bs256_acc76/efficientnet-b0_ascend_v111_imagenet2012_research_cv_bs256_acc76.ckpt>
    asset-sha256: b27cedc2df90b386cc8a06d7e7335ea49df2cacf1603b00e3820bd85af64176d

license: Apache2.0

summary: efficientnet-b0 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of efficientnet-b0 from the MindSpore model zoo on Gitee at model_zoo/research/cv/efficientnet-b0.

efficientnet-b0 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/efficientnet-b0](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/efficientnet-b0/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/efficientnet-b0_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. 2019.
