# yolov3_tiny

---

model-name: yolov3_tiny

backbone-name: yolov3_tiny

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: coco2017

evaluation: mAP17.5 | AP50acc36.0

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/yolov3_tiny>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/yolov3tiny_ascend_v190_coco2017_research_cv_mAP17.5_AP50acc36.0.ckpt>
    asset-sha256: 6fa28f3a69243e659c8c7ffae490278faf7625840668bee2a49e1b3887b0711a

license: Apache2.0

summary: yolov3_tiny is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolov3_tiny from the MindSpore model zoo on Gitee at research/cv/yolov3_tiny.

yolov3_tiny is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/yolov3_tiny](https://gitee.com/mindspore/models/blob/r1.9/research/cv/yolov3_tiny/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/yolov3tiny_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Joseph Redmon, Ali Farhadi. arXiv preprint arXiv:1804.02767, 2018. 2, 4, 7, 11.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
