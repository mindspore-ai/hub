# cnnctc

---

model-name: cnnctc

backbone-name: cnnctc

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: mjstiiit

evaluation: acc85.97

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/cnnctc>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/cnnctc_ascend_v130_mjstiiit_official_cv_acc85.97.ckpt>
    asset-sha256: 3468204da46492286ed466c9bab9572443b4e7d359396a5e38b42ceb3d0a6c6f

license: Apache2.0

summary: cnnctc is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of cnnctc from the MindSpore model zoo on Gitee at official/cv/cnnctc.

cnnctc is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/cnnctc](https://gitee.com/mindspore/models/blob/r1.3/official/cv/cnnctc/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/cnnctc_mjstiiit"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

J. Baek, G. Kim, J. Lee, S. Park, D. Han, S. Yun, S. J. Oh, and H. Lee, “What is wrong with scene text recognition model comparisons? dataset and model analysis,” ArXiv, vol. abs/1904.01906, 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
