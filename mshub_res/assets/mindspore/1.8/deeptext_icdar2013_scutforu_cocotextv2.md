# deeptext

---

model-name: deeptext

backbone-name: deeptext

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: icdar2013_scutforu_cocotextv2

evaluation: F1score85

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/deeptext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/deeptext_ascend_v180_icdar2013_scutforu_cocotextv2_official_cv_F1score85.ckpt>
    asset-sha256: 0ac5e5cbfd40ddcd16e30b7baa1904ac7ec20c5e3f8f8850aa20fac9baf03f37

license: Apache2.0

summary: deeptext is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of deeptext from the MindSpore model zoo on Gitee at official/cv/deeptext.

deeptext is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/deeptext](https://gitee.com/mindspore/models/blob/r1.8/official/cv/deeptext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/deeptext_icdar2013_scutforu_cocotextv2"
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
