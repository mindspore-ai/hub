# yolov3_resnet18

---

model-name: yolov3_resnet18

backbone-name: yolov3_resnet18

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: coco2017

evaluation: class0precision91.76 | class0recall66.27 | class1precision89.09 | class1recall76.93

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/yolov3_resnet18>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/yolov3resnet18_ascend_v190_coco2017_official_cv_class0precision91.76_class0recall66.27_class1precision89.09_class1recall76.93.ckpt>
    asset-sha256: 42c46a3b9518282da79233d0b550c8d5d4c32e79c1ebe8facd155fe8f2e7e75b

license: Apache2.0

summary: yolov3_resnet18 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_resnet18 from the MindSpore model zoo on Gitee at official/cv/yolov3_resnet18.

yolov3_resnet18 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/yolov3_resnet18](https://gitee.com/mindspore/models/blob/r1.9/official/cv/yolov3_resnet18/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/yolov3resnet18_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[YOLOv3: An Incremental Improvement](https://pjreddie.com/media/files/papers/YOLOv3.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
