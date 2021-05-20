# ssd_mobilenetV2_FPNlite

---

model-name: ssd_mobilenetV2_FPNlite

backbone-name: ssd_mobilenetV2_FPNlite

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: coc02017

accuracy: 88

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/ssd_mobilenetV2_FPNlite>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/ssd-mobilenetV2-FPNlite_ascend_v111_coc02017_research_cv_bs32_iou23/ssd-mobilenetV2-FPNlite_ascend_v111_coc02017_research_cv_bs32_iou23.ckpt>
    asset-sha256: fdab7cc28b20ede84f6dd9e53f4ac29c968b7f89e6bec6ec6e7eebc205e2c160

license: Apache2.0

summary: ssd_mobilenetV2_FPNlite is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_mobilenetV2_FPNlite from the MindSpore model zoo on Gitee at model_zoo/research/cv/ssd_mobilenetV2_FPNlite.

ssd_mobilenetV2_FPNlite is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ssd_mobilenetV2_FPNlite](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/ssd_mobilenetV2_FPNlite/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/ssd-mobilenetV2-FPNlite_v1.1_coc02017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu,
   Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
