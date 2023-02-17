# centerface

---

model-name: centerface

backbone-name: centerface

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: widerface

evaluation: easy92.4 | medium91.7 | hard77.9

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/centerface>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/centerface_ascend_v1100_widerface_official_cv_easy92.4_medium91.7_hard77.9.ckpt>
    asset-sha256: 9e2809d1561c0450a0ef063cbacd7690f688931a8bce4fdc6579aa26237de908

license: Apache2.0

summary: centerface is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of centerface from the MindSpore model zoo on Gitee at official/cv/centerface.

centerface is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/centerface](https://gitee.com/mindspore/models/blob/r1.10/official/cv/centerface/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/centerface_widerface"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[CenterFace: Joint Face Detection and Alignment Using Face as Point](https://arxiv.org/ftp/arxiv/papers/1911/1911.03599.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
