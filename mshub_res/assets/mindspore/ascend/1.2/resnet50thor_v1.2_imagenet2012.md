# resnet_thor

---

model-name: resnet_thor

backbone-name: resnet_thor

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 76

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnet_thor>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnet50thor_ascend_v120_imagenet2012_official_cv_bs32_acc76/resnet50thor_ascend_v120_imagenet2012_official_cv_bs32_acc76.ckpt>
    asset-sha256: 84984e19dbd0243955e028a5aebbe70703270eb7878cbc22009775ac7b3348ec

license: Apache2.0

summary: resnet_thor is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet_thor from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet_thor.

resnet_thor is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet_thor](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnet_thor/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnet50thor_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, class_num=1001)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. Deep Residual Learning for Image Recognition.
