# PSENET

---

model-name: psenet

backbone-name: resnet50

module-type: cv-text-detection

fine-tunable: True

input-shape: [640, 640, 3]

model-version: 1.1

accuracy: 0.83

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/psenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/psenet_ascend_v111_icdar2015_offical_cv_bs4_acc83/psenet_ascend_v111_icdar2015_offical_cv_bs4_acc83.ckpt>
    asset-sha256: a9960ccb1f0be186b8917a3e0fbd223c8b3e58e1989be712f613456b4b1a0646

license: Apache2.0

summary: psenet used to test detection of ICDAR2015

---

## Introduction

This MindSpore Hub model uses the implementation of PseNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/psenet.

This model has been trained on ICDAR2015 using the code published on Gitee. More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/cv/psenet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/psenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from model_zoo.official.cv.psenet.src.config import config

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/psenet_v1.1"

network = mshub.load(model, config=config)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/psenet>.
```

## Citation

Paper: Wenhai Wang, Enze Xie, Xiang Li, Wenbo Hou, Tong Lu, Gang Yu, Shuai Shao; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9336-9345
