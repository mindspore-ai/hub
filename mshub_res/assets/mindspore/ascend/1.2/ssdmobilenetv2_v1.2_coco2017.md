# ssd_mobilenetV2

---

model-name: ssd_mobilenetV2

backbone-name: ssd_mobilenetV2

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: coco2017

accuracy: 25

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/ssd_mobilenetV2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ssdmobilenetv2_ascend_v120_coco2017_research_cv_bs32_acc25/ssdmobilenetv2_ascend_v120_coco2017_research_cv_bs32_acc25.ckpt>
    asset-sha256: b977f7356fcd8a0aeb7e442afac44b681078f6bebf0062a39fb5eb37a485bf29

license: Apache2.0

summary: ssd_mobilenetV2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_mobilenetV2 from the MindSpore model zoo on Gitee at model_zoo/research/cv/ssd_mobilenetV2.

ssd_mobilenetV2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ssd_mobilenetV2](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/ssd_mobilenetV2/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/ssdmobilenetv2_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
