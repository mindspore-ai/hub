# bert_finetune

---

model-name: bert_base

backbone-name: bert

module-type: nlp-natural_language_understanding

fine-tunable: True

model-version: 1.9

train-dataset: cluener

evaluation: acc91.87

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/bert>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/bertfinetune_crf_ascend_v190_cluener_official_nlp_acc91.87.ckpt>
    asset-sha256: ca13d2d814ac2467e1310c202a5fbcc90345ec027c79bfc641f2ee415d70b3f4

license: Apache2.0

summary: bert is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of bert from the MindSpore model zoo on Gitee at official/nlp/bert.

bert is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/bert](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/bert/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/bertfinetune_crf_cluener"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)
2. [NEZHA: Neural Contextualized Representation for Chinese Language Understanding](https://arxiv.org/pdf/1909.00204.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
