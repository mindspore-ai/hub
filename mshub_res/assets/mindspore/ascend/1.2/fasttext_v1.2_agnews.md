# fasttext

---

model-name: fasttext

backbone-name: fasttext

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: agnews

accuracy: 92

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/fasttext>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/fasttext_ascend_v120_agnews_official_nlp_bs512_acc92/fasttext_ascend_v120_agnews_official_nlp_bs512_acc92.ckpt>
    asset-sha256: aebeab53a428c8bbd1ee11738aaea3f6a582f1dc69c1fd1b9ddaf5ef3c12ecc1

license: Apache2.0

summary: fasttext is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of fasttext from the MindSpore model zoo on Gitee at model_zoo/official/nlp/fasttext.

fasttext is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/fasttext](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/fasttext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

vocab_size = 1383812
embedding_dims = 16
num_class = 4

model = "mindspore/ascend/1.2/fasttext_v1.2_agnews"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, vocab_size, embedding_dims, num_class)
network.set_train(False)

# ...
```

## Citation

1. Bag of Tricks for Efficient Text Classification, 2016, A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.