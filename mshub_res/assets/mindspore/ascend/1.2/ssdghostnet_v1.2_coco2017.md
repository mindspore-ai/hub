# ssd_ghostnet

---

model-name: ssd_ghostnet

backbone-name: ssd_ghostnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: coco2017

accuracy: 24

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/ssd_ghostnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/ssdghostnet_ascend_v120_coco2017_research_cv_bs32_acc24/ssdghostnet_ascend_v120_coco2017_research_cv_bs32_acc24.ckpt>
    asset-sha256: a6ee852d90910e41a6707db0f3d602c375d44747afe7ef4718a3b2e7aa195447

license: Apache2.0

summary: ssd_ghostnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_ghostnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/ssd_ghostnet.

ssd_ghostnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ssd_ghostnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/ssd_ghostnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/ssdghostnet_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
