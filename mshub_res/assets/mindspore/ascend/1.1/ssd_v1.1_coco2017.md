# SSD

---

model-name: ssd

backbone-name: ssd300

module-type: cv-object_detection

fine-tunable: True

input-shape: [300, 300, 3]

model-version: 1.1

train-dataset: coco2017

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/ssd>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/ssd_ascend_v111_coco2017_offical_cv_bs32_belu22/ssd_ascend_v111_coco2017_offical_cv_bs32_belu22.ckpt>
    asset-sha256: 13d28a651dabc8caab062bca8093c5c8abd76621161bab222235bc3f66b11cf1

license: Apache2.0

summary: ssd with the shape 300 * 300 for object detection

---

## Introduction

This MindSpore Hub model uses the implementation of ssd from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssd.

ssd is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/ssd](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/ssd/README.md).

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

model = "mindspore/ascend/1.1/ssd_v1.1_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C.
   Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
