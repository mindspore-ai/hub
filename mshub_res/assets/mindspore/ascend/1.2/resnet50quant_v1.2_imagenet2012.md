# resnet50_quant

---

model-name: resnet50_quant

backbone-name: resnet50_quant

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 76

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnet50_quant>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnet50quant_ascend_v120_imagenet2012_official_cv_bs32_acc76/resnet50quant_ascend_v120_imagenet2012_official_cv_bs32_acc76.ckpt>
    asset-sha256: fc25f91acd9535e0f36deffb8f1ae76255a9c397350d5cca7b188002f133231f

license: Apache2.0

summary: resnet50_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet50_quant from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet50_quant.

resnet50_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet50_quant](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnet50_quant/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnet50quant_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun."Deep Residual Learning for Image Recognition." He, Kaiming , et al. "Deep Residual Learning for Image Recognition." IEEE Conference on Computer Vision & Pattern Recognition IEEE Computer Society, 2016.
