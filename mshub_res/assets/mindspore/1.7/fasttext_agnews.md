# fasttext

---

model-name: fasttext

backbone-name: fasttext

module-type: nlp

fine-tunable: True

model-version: 1.7

train-dataset: agnews

evaluation: acc92.58

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/nlp/fasttext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/fasttext_ascend_v170_agnews_official_nlp_acc92.58.ckpt>
    asset-sha256: 067f30b7b6cd19bb8a79601f1da365a1189881a3050f82d610b4f107c4d75d97

license: Apache2.0

summary: fasttext is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of fasttext from the MindSpore model zoo on Gitee at official/nlp/fasttext.

fasttext is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/fasttext](https://gitee.com/mindspore/models/blob/r1.7/official/nlp/fasttext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/fasttext_agnews"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

"Bag of Tricks for Efficient Text Classification", 2016, A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
