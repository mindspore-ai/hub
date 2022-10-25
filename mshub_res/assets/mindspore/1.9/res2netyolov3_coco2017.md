# res2net_yolov3

---

model-name: res2net_yolov3

backbone-name: res2net_yolov3

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: coco2017

evaluation: mAP32

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/res2net_yolov3>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/res2netyolov3_ascend_v190_coco2017_research_cv_mAP32.ckpt>
    asset-sha256: 8d29fa83f0f50260d77fbe93f0f1149cd7d46d8574e20df290078b5a50ea1a7d

license: Apache2.0

summary: res2net_yolov3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of res2net_yolov3 from the MindSpore model zoo on Gitee at research/cv/res2net_yolov3.

res2net_yolov3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/res2net_yolov3](https://gitee.com/mindspore/models/blob/r1.9/research/cv/res2net_yolov3/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/res2netyolov3_coco2017"
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
