# textrcnn

---

model-name: textrcnn

backbone-name: textrcnn

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: polarity_moviereview

evaluation: acc80.76

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/textrcnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/textcrnn_lstm_ascend_v190_polarity_moviereview_research_nlp_acc80.76.ckpt>
    asset-sha256: 5f9d9fbf78b31fb4f51d3b5c9e92f1a97b0e4388b11b060ad4001307e1615e74

license: Apache2.0

summary: textrcnn is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of textrcnn from the MindSpore model zoo on Gitee at research/nlp/textrcnn.

textrcnn is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/textrcnn](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/textrcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/textcrnn_lstm_polarity_moviereview"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Recurrent Convolutional Neural Networks for Text Classification](http://www.nlpr.ia.ac.cn/cip/~liukang/liukangPageFile/Recurrent%20Convolutional%20Neural%20Networks%20for%20Text%20Classification.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
