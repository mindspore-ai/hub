# faster_rcnn

---

model-name: faster_rcnn

backbone-name: faster_rcnn

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: coco2017

evaluation: AP50acc60.6

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/faster_rcnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fasterrcnnresnetv150_ascend_v190_coco2017_official_cv_AP50acc60.6.ckpt>
    asset-sha256: 0119e5d9c267872f48317c13e38205a67eb8070aa1418a67b919693dd3e532ed

license: Apache2.0

summary: faster_rcnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of faster_rcnn from the MindSpore model zoo on Gitee at official/cv/faster_rcnn.

faster_rcnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/faster_rcnn](https://gitee.com/mindspore/models/blob/r1.9/official/cv/faster_rcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/fasterrcnnresnetv150_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Ren S , He K , Girshick R , et al. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2015, 39(6).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.