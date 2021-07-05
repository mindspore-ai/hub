# ssdresnet50fpn

---

model-name: ssd_resnet50_fpn

backbone-name: ssd_resnet50_fpn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: coco2017

accuracy: 24

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/ssd>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ssdresnet50fpn_ascend_v120_coco2017_official_cv_bs32_acc24/ssdresnet50fpn_ascend_v120_coco2017_official_cv_bs32_acc24.ckpt>
    asset-sha256: c0ee4f9fbc95ef5807e492bd6c8240cc4c525a4e7cb72d392827598a22dfedbe

license: Apache2.0

summary: ssdresnet50fpn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssdresnet50fpn from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssdresnet50fpn.

ssdresnet50fpn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/ssdresnet50fpn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/ssdresnet50fpn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/ssdresnet50fpn_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
