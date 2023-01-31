# gnmt_v2

---

model-name: gnmt

backbone-name: gnmt_v2

module-type: nlp

fine-tunable: True

model-version: 1.3

train-dataset: wmtende

evaluation: acc24

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/nlp/gnmt_v2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/gnmtv2_ascend_v130_wmtende_official_nlp_acc24.ckpt>
    asset-sha256: 48546b769601e39e380c2ec3916930501195e200fe84f1ef04d91725b4380e1a

license: Apache2.0

summary: gnmt_v2 is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of gnmt_v2 from the MindSpore model zoo on Gitee at official/nlp/gnmt_v2.

gnmt_v2 is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/gnmt_v2](https://gitee.com/mindspore/models/blob/r1.3/official/nlp/gnmt_v2/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/gnmtv2_wmtende"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
