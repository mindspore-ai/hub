# dgu

---

model-name: dgu

backbone-name: dgu

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: udc

accuracy: 0

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
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/dgu_ascend_v111_udc_official_nlp_bs32_acc0/dgu_ascend_v111_udc_official_nlp_bs32_acc0.8224_0.90464_0.97792.ckpt>
    asset-sha256: 6589eaa50d86945095e8e54206014a2138ff45fec7d9f10e0ea158028bcee290

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

model = "mindspore/ascend/1.1/dgu_v1.1_udc"
# set the train parameter
isTrained = False
# set the dataset paramerter
taskName = "udc"

# initialize the number of classes based on the pre-trained model
network = mshub.load(model, trainable=isTrained, task_name=taskName)
network.set_train(False)

# ...
```

## Citation