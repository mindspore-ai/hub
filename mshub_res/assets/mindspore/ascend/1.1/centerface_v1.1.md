# CenterFace

---

model-name: centerface

backbone-name: mobilenet_v2

module-type: cv

fine-tunable: True

input-shape: [512, 512, 3]

model-version: 1.1

train-dataset: widerface

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/centerface>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/centerface_ascend_v111_widerface_offical_cv_bs8_easy91/centerface_ascend_v111_widerface_offical_cv_bs8_easy91.ckpt>
    asset-sha256: 531df10674273ab439dd453bacf465bd696d784865719722b6ff74daeecfaee5

license: Apache2.0

summary: centernet for multi-person pose detection

---

## Introduction

This MindSpore Hub model uses the implementation of centerface from the MindSpore model zoo on Gitee at model_zoo/official/cv/centerface.

centerface is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/centerface](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/centerface/README.md).

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

model = "mindspore/ascend/1.1/centerface_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Paper: CenterFace: Joint Face Detection and Alignment Using Face as Point. Xu, Yuanyuan(Huaqiao University) and Yan, Wan(StarClouds) and Sun, Haixin(Xiamen University) and Yang, Genke(Shanghai Jiaotong University) and Luo, Jiliang(Huaqiao University)
