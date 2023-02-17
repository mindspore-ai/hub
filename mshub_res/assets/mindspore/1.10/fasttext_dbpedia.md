# fasttext

---

model-name: fasttext

backbone-name: fasttext

module-type: nlp-natural_language_understanding

fine-tunable: True

model-version: 1.10

train-dataset: DBPedia Ontology Classification Dataset

evaluation: acc98.6

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/nlp/fasttext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/fasttext_ascend_v1100_dbpedia_official_nlp_acc98.6.ckpt>
    asset-sha256: 9a7a2495d0d4fb52b37459bca8d4e8e1d4f960a61af30af2af2a63adf3bcec05

license: Apache2.0

summary: fasttext is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of fasttext from the MindSpore model zoo on Gitee at official/nlp/fasttext.

fasttext is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/fasttext](https://gitee.com/mindspore/models/blob/r1.10/official/nlp/fasttext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/fasttext_dbpedia"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Bag of Tricks for Efficient Text Classification](https://arxiv.org/pdf/1607.01759.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
