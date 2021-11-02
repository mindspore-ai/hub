# resnet50se

---

model-name: resnet50se

backbone-name: resnet50se

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 76

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnet50se_ascend_v120_imagenet2012_official_cv_bs32_acc76/resnet50se_ascend_v120_imagenet2012_official_cv_bs32_acc76.ckpt>
    asset-sha256: 3a40d328e19c335bbd2c70b3eafaa9df8626a61b75a196efb5a7cea52b2585e0

license: Apache2.0

summary: resnet50se is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet50se from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet50se.

resnet50se is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet50se](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnet50se_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
