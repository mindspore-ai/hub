# yolov4

---

model-name: yolov4_shape416

backbone-name: yolov4

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: coco2017

evaluation: acc44

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/cv/yolov4>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/yolov4_ascend_v170_coco2017_official_cv_acc44.ckpt>
    asset-sha256: e318152734c9bb89c2907f4d26bf0dff63241d7dffc52b2dc48c93353f13fde8

license: Apache2.0

summary: yolov4 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov4 from the MindSpore model zoo on Gitee at official/cv/yolov4.

yolov4 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/yolov4](https://gitee.com/mindspore/models/blob/r1.7/official/cv/yolov4/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/yolov4_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Bochkovskiy A, Wang C Y, Liao H Y M. YOLOv4: Optimal Speed and Accuracy of Object Detection[J]. arXiv preprint arXiv:2004.10934, 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
