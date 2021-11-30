# FCN8s

---

model-name: FCN8s

backbone-name: FCN8s

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: voc2012

accuracy: 64

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/FCN8s>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/fcn8s_ascend_v120_voc2012_official_cv_bs32_acc64/fcn8s_ascend_v120_voc2012_official_cv_bs32_acc64.ckpt>
    asset-sha256: 943b4ca4e75f628a8a81acb40579763ef7f60dc0d8cb72ee2902fcbf8f1002ed

license: Apache2.0

summary: FCN8s is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FCN8s from the MindSpore model zoo on Gitee at model_zoo/official/cv/FCN8s.

FCN8s is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/FCN8s](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/FCN8s/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/fcn8s_v1.2_voc2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Long, Jonathan, Evan Shelhamer, Trevor Darrell. Fully convolutional networks for semantic segmentation.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.