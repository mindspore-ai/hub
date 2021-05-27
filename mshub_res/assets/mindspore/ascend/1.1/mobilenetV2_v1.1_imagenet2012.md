# MobileNetV2

---

model-name: mobilenetV2

backbone-name: mobilenetV2

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: imagenet2012

accuracy: 0.71

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/mobilenetv2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

mindspore-lite: true

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/mobilenetv2_ascend_v111_imagenet2012_offical_cv_bs256_acc71/mobilenetv2_ascend_v111_imagenet2012_offical_cv_bs256_acc71.ckpt>
    asset-sha256: a9c8d8e461338c670af5f953d0c188ced1da01882abb7865d028840e94d7e4fd

license: Apache2.0

summary: mobilenetv2 used to classify 600 classes of openimage.

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv2 from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv2.

mobilenetv2 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/mobilenetv2](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/mobilenetv2/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/mobilenetV2_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.
