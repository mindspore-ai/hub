# mass

---

model-name: mass

backbone-name: mass

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: gigaword

accuracy: 46

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/mass>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/mass_ascend_v120_gigaword_official_nlp_bs192_acc46/mass_ascend_v120_gigaword_official_nlp_bs192_acc46.ckpt>
    asset-sha256: b1896f6f13fadb0ce84a5580c8175ca12814bc85778aaeaa2fab16f8d9d4fb3b

license: Apache2.0

summary: mass is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of mass from the MindSpore model zoo on Gitee at model_zoo/official/nlp/mass.

mass is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/mass](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/mass/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/mass_v1.2_gigaword"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Song, Kaitao, Xu Tan, Tao Qin, Jianfeng Lu and Tie-Yan Liu. “MASS: Masked Sequence to Sequence Pre-training for Language Generation.” ICML (2019).
