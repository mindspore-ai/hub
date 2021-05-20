# ssd_resnet50

---

model-name: ssd_resnet50

backbone-name: ssd_resnet50

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 32

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/ssd_resnet50>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/ssd-resnet50_ascend_v111_imagenet2012_research_cv_bs32_acc32/ssd-resnet50_ascend_v111_imagenet2012_research_cv_bs32_acc32.ckpt>
    asset-sha256: d036ceea4dba5ca38f4af6d2031441deabb72f3b71bbadbd797a0bbf257989e3

license: Apache2.0

summary: ssd_resnet50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_resnet50 from the MindSpore model zoo on Gitee at model_zoo/research/cv/ssd_resnet50.

ssd_resnet50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ssd_resnet50](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/ssd_resnet50/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/ssd-resnet50_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.
   European Conference on Computer Vision (ECCV), 2016 (In press).
