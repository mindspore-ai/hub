# skipgram

---

model-name: skipgram

backbone-name: skipgram

module-type: nlp

fine-tunable: True

model-version: 1.3

train-dataset: text8

evaluation: acc35.78

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/nlp/skipgram>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/skipgram_ascend_v130_text8_research_nlp_acc35.78.ckpt>
    asset-sha256: 5ce385cfc638b6ab2f10309fb4980792513458db4dfa1cc5adb2b2c382b1457a

license: Apache2.0

summary: skipgram is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of skipgram from the MindSpore model zoo on Gitee at research/nlp/skipgram.

skipgram is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/skipgram](https://gitee.com/mindspore/models/blob/r1.3/research/nlp/skipgram/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/skipgram_text8"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Mikolov T, Chen K, Corrado G, et al. Efficient estimation of word representations in vector space[J]. arXiv preprint arXiv:1301.3781, 2013.
2. Mikolov T, Sutskever I, Chen K, et al. Distributed representations of words and phrases and their compositionality[J]. arXiv preprint arXiv:1310.4546, 2013.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
