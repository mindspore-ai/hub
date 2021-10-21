# simple_pose

---

model-name: simple_pose

backbone-name: simple_pose

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: coco2017

accuracy: 70

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/simple_pose>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/simplepose_ascend_v130_coco2017_official_cv_bs64_acc70/simplepose_ascend_v130_coco2017_official_cv_bs64_acc70.ckpt>
    asset-sha256: 206c944b9a756c17475c97864469cfb3c5e56b8737ecf6dccaf544b9fc75f0df

license: Apache2.0

summary: simple_pose is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simple_pose from the MindSpore model zoo on Gitee at model_zoo/official/cv/simple_pose.

simple_pose is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/simple_pose](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/simple_pose/README.md).

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

model = "mindspore/ascend/1.3/simplepose_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, is_train=False)
network.set_train(False)

# ...
```

## Citation

1. B. Xiao, H. Wu, and Y. Wei, “Simple baselines for human pose estimation and tracking,” in Proc. Eur. Conf. Comput. Vis., 2018, pp. 472–487.
