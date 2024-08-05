# yolov7_tiny

---

model-name: yolov7_tiny

backbone-name: yolov7

module-type: cv

fine-tunable: True

model-version: 2.3

train-dataset: COCO2017

evaluation: mAP37.5

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindyolo/tree/v0.4.0/configs/yolov7>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolov7/yolov7-tiny_300e_mAP375-1d2ddf4b-910v2.ckpt>
    asset-sha256: 1d2ddf4b

license: Apache2.0

summary: yolov7 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov7 from the MindSpore.

yolov7 is a cv network. More details please refer to the MindSpore-Lab on GitHub at [yolov7](https://github.com/mindspore-lab/mindyolo/blob/v0.4.0/configs/yolov7/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/yolov7_tiny_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://arxiv.org/pdf/2207.02696.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
