# deeplabv3plus

---

model-name: deeplabv3plus

backbone-name: deeplabv3plus

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: voc2012

evaluation: s8acc79.62 | s8multiscale80.32 | s8multiscaleflip80.61

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/deeplabv3plus>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/deeplabv3plus_s8r2_ascend_v1100_voc2012_research_cv_s8acc79.62_s8multiscale80.32_s8multiscaleflip80.61.ckpt>
    asset-sha256: a9205a37d19d6d335b21b3f037faf078c7f25613e176b1b8fcf9198d5632887c

license: Apache2.0

summary: deeplabv3plus is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of deeplabv3plus from the MindSpore model zoo on Gitee at research/cv/deeplabv3plus.

deeplabv3plus is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/deeplabv3plus](https://gitee.com/mindspore/models/blob/r1.10/research/cv/deeplabv3plus/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/deeplabv3plus_s8r2_voc2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation](https://arxiv.org/pdf/1802.02611.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
