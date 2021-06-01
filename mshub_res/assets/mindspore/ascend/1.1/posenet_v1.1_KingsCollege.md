# posenet

---

model-name: posenet

backbone-name: posenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: KingsCollege

accuracy: 1

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/posenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/posenet_ascend_v111_KingsCollege_research_cv_bs_75_acc1/posenet_ascend_v111_KingsCollege_research_cv_bs_75_acc1.92_4.24.ckpt>
    asset-sha256: c7bf7c4e93ae7d4bcc939b775a347c5eb3e09e5dbc6d9bade41fc3ba62046b4d

license: Apache2.0

summary: posenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of posenet from the MindSpore model zoo on Gitee at model_zoo/research/cv/posenet.

posenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/posenet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/posenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/posenet_v1.1_KingsCollege"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kendall A, Grimes M, Cipolla R. "PoseNet: A convolutional network for real-time 6-dof camera relocalization.
   "*In IEEE International Conference on Computer Vision (pp. 2938–2946
