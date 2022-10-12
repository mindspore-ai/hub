# bert_thor

---

model-name: bert_thor

backbone-name: bert_thor

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: cnnews128

evaluation: acc71.21

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/bert_thor>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/bertlarge_ascend_v190_cnnews128_official_nlp_acc71.21.ckpt>
    asset-sha256: 05ea53283419af7fb9358fccf99a8b5a47e2ed09a8592d9d4be62e1f1c0e77d5

license: Apache2.0

summary: bert_thor is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of bert_thor from the MindSpore model zoo on Gitee at official/nlp/bert_thor.

bert_thor is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/bert_thor](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/bert_thor/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/bertlarge_cnnews128"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
