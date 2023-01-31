# bert_large

---

model-name: bert_thor

backbone-name: bert_thor

module-type: nlp-natural_language_understanding

fine-tunable: True

model-version: 1.8

train-dataset: en-wiki-512

evaluation: acc71.0

author: MindSpore team

update-time: 2022-08-08

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/nlp/bert_thor>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/bertlarge_boost_ascend_v180_enwiki512_official_nlp_acc71.0.ckpt>
    asset-sha256: f80414b9d68628bf3c182a837d7c1ef10c4d6c3cf590e33e8f0c837b1ee98e56

license: Apache2.0

summary: bert_thor is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of bert_thor from the MindSpore model zoo on Gitee at official/nlp/bert_thor.

bert_thor is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/bert_thor](https://gitee.com/mindspore/models/blob/r1.8/official/nlp/bert_thor/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/bertlarge_boost_enwiki512"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
