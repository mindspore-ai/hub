# crnn

---

model-name: crnn

backbone-name: crnn

module-type: cv-scene_text_recognition

fine-tunable: True

model-version: 1.9

train-dataset: CRNN-DS

evaluation: SVT80.99 | IIIT5K80.33

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/crnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/crnn_ascend_v190_crnnds_official_cv_SVT80.99_IIIT5K80.33.ckpt>
    asset-sha256: 5d982fd1c8816fa8ac0163ef92d9f0c9291e34af5284c9a0821ebabd55b05f2a

license: Apache2.0

summary: crnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of crnn from the MindSpore model zoo on Gitee at official/cv/crnn.

crnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/crnn](https://gitee.com/mindspore/models/blob/r1.9/official/cv/crnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/crnn_crnnds"
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
