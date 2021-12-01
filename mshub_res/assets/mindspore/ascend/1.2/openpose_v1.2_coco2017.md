# openpose

---

model-name: openpose

backbone-name: openpose

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: coco2017

accuracy: 40

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/openpose>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/openpose_ascend_v120_coco2017_official_cv_bs10_acc40/openpose_ascend_v120_coco2017_official_cv_bs10_acc40.ckpt>
    asset-sha256: 3097e36da32bf8d7581563bdf3c70b89608919284adbf4233057fbb9a1b165b5

license: Apache2.0

summary: openpose is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of openpose from the MindSpore model zoo on Gitee at model_zoo/official/cv/openpose.

openpose is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/openpose](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/openpose/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/openpose_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Zhe Cao,Tomas Simon,Shih-En Wei,Yaser Sheikh,"Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields",The IEEE Conference on Computer Vision and Pattern Recongnition(CVPR),2017

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.