# crnn

---

model-name: crnn

backbone-name: crnn

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: synth

evaluation: svtacc80.83 | iiit5kacc79.73

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/crnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/crnn_ascend_v160_synth_official_cv_svtacc80.83_iiit5kacc79.73.ckpt>
    asset-sha256: 640dd154c7d4bbf93de2103f5e58e3595e0085d6fcd07731669666dc9d0745fd

license: Apache2.0

summary: crnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of crnn from the MindSpore model zoo on Gitee at official/cv/crnn.

crnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/crnn](https://gitee.com/mindspore/models/blob/r1.6/official/cv/crnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/crnn_synth"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Baoguang Shi, Xiang Bai, Cong Yao, "An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition", ArXiv, vol. abs/1507.05717, 2015.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
