# transformer

---

model-name: transformer

backbone-name: transformer

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: wmtende

accuracy: 28

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/transformer>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/transformer_ascend_v120_wmtende_official_nlp_bs96_acc28/transformer_ascend_v120_wmtende_official_nlp_bs96_acc28.ckpt>
    asset-sha256: bb81f2745b3de06b00495aa3596100532e3af3557c5c5c0431fb72e5c4b2bb72

license: Apache2.0

summary: transformer is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of transformer from the MindSpore model zoo on Gitee at model_zoo/official/nlp/transformer.

transformer is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/transformer](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/transformer/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/transformer_v1.2_wmtende"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Ashish Vaswani, Noam Shazeer, Niki Parmar, JakobUszkoreit, Llion Jones, Aidan N Gomez, Ł ukaszKaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS 2017, pages 5998–6008.
