# densenet

---

model-name: densenet

backbone-name: densenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 75

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/densenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/densenet121_ascend_v120_imagenet2012_official_cv_bs32_top1acc75_top5acc92/densenet121_ascend_v120_imagenet2012_official_cv_bs32_top1acc75_top5acc92.ckpt>
    asset-sha256: 5e0a855fb6fbfa5f46e9bba581d798147a3ca6bce0a2b63981928809f21c7665

license: Apache2.0

summary: densenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of densenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/densenet.

densenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/densenet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/densenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/densenet121_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1001)
network.set_train(False)

# ...
```

## Citation

1. Gao Huang, Zhuang Liu, Laurens van der Maaten, Kilian Q. Weinberger. Densely Connected Convolutional Networks
