# deeptext

---

model-name: deeptext

backbone-name: deeptext

module-type: cv-scene_text_detection

fine-tunable: True

model-version: 1.9

train-dataset: ICDAR2013 | SCUT-FORU | CocoTextv2

evaluation: F1score84.5

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/deeptext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/deeptext_ascend_v190_icdar2013_official_cv_F1score84.5.ckpt>
    asset-sha256: abda476ba56abe26597d477bf9472749a0e4819d86cfd596a9a3e0e1d37647bc

license: Apache2.0

summary: deeptext is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of deeptext from the MindSpore model zoo on Gitee at official/cv/deeptext.

deeptext is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/deeptext](https://gitee.com/mindspore/models/blob/r1.9/official/cv/deeptext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/deeptext_icdar2013"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Zhuoyao Zhong, Lianwen Jin, Shuangping Huang, South China University of Technology (SCUT), Published in ICASSP 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
