# retinanet

---

model-name: retinanet

backbone-name: retinanet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: coco2017

accuracy: 35

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/retinanet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/retinanet_ascend_v130_coco2017_official_cv_bs32_acc35/retinanet_ascend_v130_coco2017_official_cv_bs32_acc35.ckpt>
    asset-sha256: 2fda03174122089d884f7fde4115d51145a25d44cca6f9c02f0653a83d17cab6

license: Apache2.0

summary: retinanet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of retinanet from the MindSpore model zoo on Gitee at model_zoo/official/cv/retinanet.

retinanet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/retinanet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/retinanet/README_CN.md).

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

model = "mindspore/ascend/1.3/retinanet_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Lin T Y , Goyal P , Girshick R , et al. Focal Loss for Dense Object Detection[C]// 2017 IEEE International Conference on Computer Vision (ICCV). IEEE, 2017:2999-3007.
