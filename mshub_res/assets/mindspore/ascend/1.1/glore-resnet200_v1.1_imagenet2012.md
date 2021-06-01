# Glore_resnet200

---

model-name: glore_res200

backbone-name: glore_res200

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 80

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/Glore_resnet200>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/glore-resnet200_ascend_v111_imagenet2012_research_cv_bs128_acc80/glore-resnet200_ascend_v111_imagenet2012_research_cv_bs128_acc80.ckpt>
    asset-sha256: 50455a513c65287a895f8e33b4af7d84b00ca038c27a4630431a65e15a89a74f

license: Apache2.0

summary: glore_res50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of glore_res50 from the MindSpore model zoo on Gitee at model_zoo/research/cv/Glore_resnet200.

glore_res50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/Glore_resnet200](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/Glore_resnet200/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/glore-resnet200_v1.1_imagenet2012"
# set the param if use glore, default is True
useGlore = True
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, use_glore=useGlore)
network.set_train(False)

# ...
```

## Citation

1. Yunpeng Chen, Marcus Rohrbach, Zhicheng Yan, Shuicheng Yan, Jiashi Feng, Yannis Kalantidis.
   Graph-Based Global Reasoning Networks
