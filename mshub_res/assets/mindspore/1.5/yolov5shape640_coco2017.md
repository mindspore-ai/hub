# yolov5

---

model-name: yolov5

backbone-name: yolov5

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: coco2017

evaluation: acc36.6

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/yolov5>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/yolov5shape640_ascend_v150_coco2017_official_cv_acc36.6.ckpt>
    asset-sha256: 9e17460882efdf587ee451fcc401d4359f0d1f31eb40825a59c339e65e1ca89b

license: Apache2.0

summary: yolov5 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov5 from the MindSpore model zoo on Gitee at official/cv/yolov5.

yolov5 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/yolov5](https://gitee.com/mindspore/models/blob/r1.5/official/cv/yolov5/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/yolov5shape640_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
