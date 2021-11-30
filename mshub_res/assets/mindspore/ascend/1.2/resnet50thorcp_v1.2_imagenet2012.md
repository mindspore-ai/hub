# resnet50thorcp

---

model-name: resnet50thorcp

backbone-name: resnet50thorcp

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 76

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/resnet_thor>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/resnet50thorcp_ascend_v120_imagenet2012_official_cv_bs256_acc76/resnet50thorcp_ascend_v120_imagenet2012_official_cv_bs256_acc76.ckpt>
    asset-sha256: 2b7a2e074b825f56baa19b63b9f78eeb94b02670721a6a4a0523b641bb7590b2

license: Apache2.0

summary: resnet50thorcp is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet50thorcp from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet50thorcp.

resnet50thorcp is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/resnet50thorcp](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/resnet_thor/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/resnet50thorcp_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, class_num=1001)
network.set_train(False)

# ...
```

## Citation

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.