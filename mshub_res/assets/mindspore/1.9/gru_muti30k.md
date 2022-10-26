# gru

---

model-name: gru

backbone-name: gru

module-type: nlp-natural_language_understanding

fine-tunable: True

model-version: 1.9

train-dataset: Multi30k

evaluation: bleu30.0

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/gru>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/gru_ascend_v190_muti30k_official_nlp_bleu30.0.ckpt>
    asset-sha256: 3b4442d48f6bac7eb022d7963f7391330ceff4caa75eee4ff2ff948b3e4a17ed

license: Apache2.0

summary: gru is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of gru from the MindSpore model zoo on Gitee at official/nlp/gru.

gru is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/gru](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/gru/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/gru_muti30k"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078.pdf)
2. [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf)
3. [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473v7.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
