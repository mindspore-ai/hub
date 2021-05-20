# mobilenetV3_small_x1_0

---

model-name: mobilenetV3_small_x1_0

backbone-name: mobilenetV3_small_x1_0

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 67

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/mobilenetV3_small_x1_0>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/mobilenetV3-small_ascend_v111_imagenet2012_research_cv_bs256_acc67/mobilenetV3-small_ascend_v111_imagenet2012_research_cv_bs256_acc67.ckpt>
    asset-sha256: 8fb6dfd4373bd605de9c63e97d826406cf87ff57a6dbfcc03b2104f0a2c3e37b

license: Apache2.0

summary: mobilenetV3_small_x1_0 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetV3_small_x1_0 from the MindSpore model zoo on Gitee at model_zoo/research/cv/mobilenetV3_small_x1_0.

mobilenetV3_small_x1_0 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/mobilenetV3_small_x1_0](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/mobilenetV3_small_x1_0/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/mobilenetV3-small_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al.
   "Searching for mobilenetv3."In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324.2019.
