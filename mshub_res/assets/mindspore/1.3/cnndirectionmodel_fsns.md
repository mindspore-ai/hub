# cnn_direction_model

---

model-name: cnn_direction_model

backbone-name: cnn_direction_model

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: fsns

evaluation: acc98

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/cnn_direction_model>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/cnndirectionmodel_ascend_v130_fsns_official_cv_acc98.ckpt>
    asset-sha256: 7dffb4205b94d111f5a0d60065cbd78912013645926c8960813ce4b1fe13725c

license: Apache2.0

summary: cnn_direction_model is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of cnn_direction_model from the MindSpore model zoo on Gitee at official/cv/cnn_direction_model.

cnn_direction_model is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/cnn_direction_model](https://gitee.com/mindspore/models/blob/r1.3/official/cv/cnn_direction_model/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/cnndirectionmodel_fsns"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
