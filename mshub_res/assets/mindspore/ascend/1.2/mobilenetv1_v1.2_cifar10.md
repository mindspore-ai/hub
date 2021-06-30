# mobilenetv1

---

model-name: mobilenetv1

backbone-name: mobilenetv1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: cifar10

accuracy: 94

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/mobilenetv1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/mobilenetv1_ascend_v120_cifar10_official_cv_bs32_acc94/mobilenetv1_ascend_v120_cifar10_official_cv_bs32_acc94.ckpt>
    asset-sha256: 9bdf260132df2a498268224faaee4bf3f426b5893ee78b229762520dafd7ddf7

license: Apache2.0

summary: mobilenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv1 from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv1.

mobilenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/mobilenetv1](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/mobilenetv1/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/mobilenetv1_v1.2_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, class_num=10)
network.set_train(False)

# ...
```

## Citation

1. Howard A G , Zhu M , Chen B , et al. MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications[J]. 2017.
