# gpt

---

model-name: gpt

backbone-name: gpt

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: openweb

evaluation: -

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/gpt>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/gpt3_ascend_v190_openweb_official_nlp.ckpt>
    asset-sha256: 0e9cdf716666b5d6e674bc710a4c36f7d915f74148840b68f5e294ab3c0c475f

license: Apache2.0

summary: gpt is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of gpt from the MindSpore model zoo on Gitee at official/nlp/gpt.

gpt is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/gpt](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/gpt/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/gpt3_openweb"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Tom B.Brown, Benjamin Mann, Nick Ryder et al. Language Models are Few-Shot Learners. arXiv preprint arXiv:2005.14165

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
