# alexnet

---

model-name: alexnet

backbone-name: alexnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 57

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/alexnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/alexnet_ascend_v120_imagenet2012_official_cv_bs256_acc57/alexnet_ascend_v120_imagenet2012_official_cv_bs256_acc57.ckpt>
    asset-sha256: 1cfc87c618e9bc9f27413f6d101884712ff56649a4980b4743a8777887f7d3b9

license: Apache2.0

summary: alexnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of alexnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/alexnet.

alexnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/alexnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/alexnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/alexnet_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000)
network.set_train(False)

# ...
```

## Citation

1. Krizhevsky A, Sutskever I, Hinton G E. ImageNet Classification with Deep ConvolutionalNeural Networks. Advances In Neural Information Processing Systems.2012.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
