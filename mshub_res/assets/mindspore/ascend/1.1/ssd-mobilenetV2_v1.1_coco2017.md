# ssd_mobilenetV2

---

model-name: ssd_mobilenetV2

backbone-name: ssd_mobilenetV2

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: coco2017

accuracy: 88

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/ssd_mobilenetV2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/ssd-mobilenetV2_ascend_v111_coco2017_bs32_iou25/ssd-mobilenetV2_ascend_v111_coco2017_bs32_iou25.ckpt>
    asset-sha256: 329c5a2b34eeb947bd2fbdddec1a3c7675b18a1533aeaabd253dcab8bb77b06c

license: Apache2.0

summary: ssd_mobilenetV2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_mobilenetV2 from the MindSpore model zoo on Gitee at model_zoo/research/cv/ssd_mobilenetV2.

ssd_mobilenetV2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ssd_mobilenetV2](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/ssd_mobilenetV2/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/ssd-mobilenetV2_v1.1_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C.
   Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
