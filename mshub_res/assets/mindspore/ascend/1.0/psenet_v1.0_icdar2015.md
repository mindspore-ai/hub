# PSENET

---

model-name: psenet

backbone-name: resnet50

module-type: cv

fine-tunable: True

input-shape: [640, 640, 3]

model-version: 1

accuracy: 0.81

author: MindSpore team

update-time: 2020-12-31

repo-link: <https://gitee.com/mindspore/models/tree/master/official/cv/psenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/psenet/psenet_ascend_1.1.0_icdar2015_official_text_detection_20210111/psenet.ckpt>  
    asset-sha256: f5cf126c1059b9d4aa1ad9f30a954a385882ea79f25ea3d19c13c67ead4f1a2y  

license: Apache2.0

summary: psenet used to test detection of ICDAR2015

---

## Introduction

This MindSpore Hub model uses the implementation of PseNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/psenet.

This model has been trained on ICDAR2015 using the code published on Gitee. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/models/tree/master/official/cv/psenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import config

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/psenet_v1.0_icdar2015"

network = mshub.load(model, config=config)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/models/tree/master/official/cv/psenet>.
```

## Citation

Paper: Wenhai Wang, Enze Xie, Xiang Li, Wenbo Hou, Tong Lu, Gang Yu, Shuai Shao; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9336-9345
