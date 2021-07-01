# gpt

---

model-name: gpt

backbone-name: gpt

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: openweb

accuracy: 7

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/gpt>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/gpt_ascend_v120_openweb_official_nlp_bs4_acc7/gpt_ascend_v120_openweb_official_nlp_bs4_acc7.ckpt>
    asset-sha256: 7985b7029bbf2b21686a9d7b17b9c8edb26b7e0a95d8b60f8052c1c41bfde22f

license: Apache2.0

summary: gpt is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of gpt from the MindSpore model zoo on Gitee at model_zoo/official/nlp/gpt.

gpt is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/gpt](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/gpt/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/gpt_v1.2_openweb"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Tom B.Brown, Benjamin Mann, Nick Ryder et al. [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165). arXiv preprint arXiv:2005.14165
