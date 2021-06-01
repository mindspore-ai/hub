# dgu

---

model-name: dgu

backbone-name: dgu

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: swda

accuracy: 80

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/nlp/dgu>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/dgu_ascend_v111_swda_official_nlp_bs32_acc80/dgu_ascend_v111_swda_official_nlp_bs32_acc80.ckpt>
    asset-sha256: cd1ce5703d11c600bad6db5a7ce7c2d24ca31426ff3ab6cedf503a6d522cdeb5

license: Apache2.0

summary: dgu is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of dgu from the MindSpore model zoo on Gitee at model_zoo/official/nlp/dgu.

dgu is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/dgu](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/nlp/dgu/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/dgu_v1.1_swda"
# set the train parameter
isTrained = False
# set the dataset paramerter
taskName = "swda"

# initialize the number of classes based on the pre-trained model
network = mshub.load(model, trainable=isTrained, task_name=taskName)
network.set_train(False)

# ...
```

## Citation
