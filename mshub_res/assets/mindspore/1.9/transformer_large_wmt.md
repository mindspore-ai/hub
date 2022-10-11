# transformer

---

model-name: transformer

backbone-name: transformer

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: wmt

evaluation: bleu28.7

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/transformer>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/transformer_large_ascend_v190_wmt_official_nlp_bleu28.7.ckpt>
    asset-sha256: cc8142f052bd9b5adda54aefb538288a57eb19dccd6e60da81dfd52048188e0b

license: Apache2.0

summary: transformer is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of transformer from the MindSpore model zoo on Gitee at official/nlp/transformer.

transformer is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/transformer](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/transformer/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/transformer_large_wmt"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Ashish Vaswani, Noam Shazeer, Niki Parmar, JakobUszkoreit, Llion Jones, Aidan N Gomez, Ł ukaszKaiser, and Illia Polosukhin. 2017. Attention is all you need. In NIPS 2017, pages 5998–6008.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
