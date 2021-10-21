# dqn

---

model-name: dqn

backbone-name: dqn

module-type: rl

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: gym

accuracy: 217

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/rl/dqn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/dqn_ascend_v120_gym_official_rl_bs1_acc217/dqn_ascend_v120_gym_official_rl_bs1_acc217.ckpt>
    asset-sha256: d363bed4662b5a7396bc50516b671fa033f9f98916c60007d1934ead5d5a0523

license: Apache2.0

summary: dqn is used for rl

---

## Introduction

This MindSpore Hub model uses the implementation of dqn from the MindSpore model zoo on Gitee at model_zoo/official/rl/dqn.

dqn is a rl network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/rl/dqn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/rl/dqn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/dqn_v1.2_gym"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Volodymyr, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves et al. Human-level control through deep reinforcement learning.
