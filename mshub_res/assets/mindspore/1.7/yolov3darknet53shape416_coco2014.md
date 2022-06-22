# yolov3_darknet53

---

model-name: yolov3_darknet53

backbone-name: yolov3_darknet53

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: coco2014

evaluation: map31.8

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/cv/yolov3_darknet53>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/yolov3darknet53shape416_ascend_v170_coco2014_official_cv_map31.8.ckpt>
    asset-sha256: 4ce32fac5ba1b8469527da8e3e6b7862988546beed6e1c90c0d2a82644d40256

license: Apache2.0

summary: yolov3_darknet53 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_darknet53 from the MindSpore model zoo on Gitee at official/cv/yolov3_darknet53.

yolov3_darknet53 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/yolov3_darknet53](https://gitee.com/mindspore/models/blob/r1.7/official/cv/yolov3_darknet53/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/yolov3darknet53shape416_coco2014"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

YOLOv3: An Incremental Improvement. Joseph Redmon, Ali Farhadi,

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
