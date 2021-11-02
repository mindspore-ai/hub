# deeptext

---

model-name: deeptext

backbone-name: deeptext

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: 3datasets

accuracy: 99

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/deeptext>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/deeptext_ascend_v120_3datasets_official_cv_bs2_acc99_recall95/deeptext_ascend_v120_3datasets_official_cv_bs2_acc99_recall95.ckpt>
    asset-sha256: 2edafae0df52b197aabe5a3b0f20363b07be17abac0f954da30408c05b2be9aa

license: Apache2.0

summary: deeptext is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of deeptext from the MindSpore model zoo on Gitee at model_zoo/official/cv/deeptext.

deeptext is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/deeptext](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/deeptext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/deeptext_v1.2_3datasets"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Zhuoyao Zhong, Lianwen Jin, Shuangping Huang, South China University of Technology (SCUT), Published in ICASSP 2017.
