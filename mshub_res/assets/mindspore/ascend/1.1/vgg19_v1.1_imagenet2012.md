# vgg19

---

model-name: vgg19

backbone-name: vgg19

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 74

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/vgg19>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/vgg19_ascend_v111_imagenet2012_research_cv_bs64_acc74/vgg19_ascend_v111_imagenet2012_research_cv_bs64_acc74.ckpt>
    asset-sha256: a361c6b410cccd30325e4da701209379589dcecc0a586894cc79978165c17d57

license: Apache2.0

summary: vgg19 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vgg19 from the MindSpore model zoo on Gitee at model_zoo/research/cv/vgg19.

vgg19 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/vgg19](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/vgg19/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/vgg19_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Simonyan K, zisserman A. Very Deep Convolutional Networks for
   Large-Scale Image Recognition[J]. arXiv preprint arXiv:1409.1556, 2014.
