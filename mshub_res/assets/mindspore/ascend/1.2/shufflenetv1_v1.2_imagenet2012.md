# shufflenetv1

---

model-name: shufflenetv1

backbone-name: shufflenetv1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 73

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/shufflenetv1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/shufflenetv1_ascend_v120_imagenet2012_official_cv_bs128_top1acc73_top5top173/shufflenetv1_ascend_v120_imagenet2012_official_cv_bs128_top1acc73_top5top173.ckpt>
    asset-sha256: 2457736cd8db995433ef0c3a24b96980bae2a2363a71be99df31a6354edcc0cb

license: Apache2.0

summary: shufflenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of shufflenetv1 from the MindSpore model zoo on Gitee at model_zoo/official/cv/shufflenetv1.

shufflenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/shufflenetv1](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/shufflenetv1/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/shufflenetv1_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, Jian Sun. "ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices." *Proceedings of the IEEE conference on computer vision and pattern recognition*. 2018.
