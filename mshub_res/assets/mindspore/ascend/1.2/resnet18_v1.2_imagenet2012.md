# resnet

---

model-name: resnet

backbone-name: resnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 70

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
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnet18_ascend_v120_imagenet2012_official_cv_bs256_acc70/resnet18_ascend_v120_imagenet2012_official_cv_bs256_acc70.ckpt>
    asset-sha256: 0841e1670e00affb1c8acc96b8983c502c4943b25f2f4b5926364d3af472766a

license: Apache2.0

summary: resnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

resnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnet18_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, class_num=1001)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"
