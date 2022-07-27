# textcnn

---

model-name: textcnn

backbone-name: textcnn

module-type: nlp

fine-tunable: True

model-version: 1.8

train-dataset: sst2

evaluation: acc82.91

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/nlp/textcnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/textcnn_ascend_v180_sst2_official_nlp_acc82.91.ckpt>
    asset-sha256: 7130c9d6d615f72caf1e27340de952f907ebe31a98886a57c0c38779c2eee6b7

license: Apache2.0

summary: textcnn is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of textcnn from the MindSpore model zoo on Gitee at official/nlp/textcnn.

textcnn is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/textcnn](https://gitee.com/mindspore/models/blob/r1.8/official/nlp/textcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/textcnn_sst2"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Kim Y. Convolutional neural networks for sentence classification[J]. arXiv preprint arXiv:1408.5882, 2014.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
