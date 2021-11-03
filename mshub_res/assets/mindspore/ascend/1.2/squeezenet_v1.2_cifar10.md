# squeezenet

---

model-name: squeezenet

backbone-name: squeezenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: cifar10

accuracy: 89

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/squeezenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/squeezenet_ascend_v120_cifar10_official_cv_bs32_acc89/squeezenet_ascend_v120_cifar10_official_cv_bs32_acc89.ckpt>
    asset-sha256: 94c9f16622f8fe867a9f34093008ce5be233138eac6657e469192ad319eaa0fc

license: Apache2.0

summary: squeezenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/squeezenet.

squeezenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/squeezenet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/squeezenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/squeezenet_v1.2_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Forrest N. Iandola and Song Han and Matthew W. Moskewicz and Khalid Ashraf and William J. Dally and Kurt Keutzer. "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size"
