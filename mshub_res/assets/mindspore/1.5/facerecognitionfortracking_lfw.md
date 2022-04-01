# FaceRecognitionForTracking

---

model-name: FaceRecognitionForTracking

backbone-name: FaceRecognitionForTracking

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: lfw

evaluation: FAR0.1recall62

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/FaceRecognitionForTracking>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/facerecognitionfortracking_ascend_v150_lfw_research_cv_FAR0.1recall62.ckpt>
    asset-sha256: e1ff7aab52774fea4d997b7afb83de5ec3a9aef5f49657111df8d3220c69cf05

license: Apache2.0

summary: FaceRecognitionForTracking is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceRecognitionForTracking from the MindSpore model zoo on Gitee at research/cv/FaceRecognitionForTracking.

FaceRecognitionForTracking is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/FaceRecognitionForTracking](https://gitee.com/mindspore/models/blob/r1.5/research/cv/FaceRecognitionForTracking/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/facerecognitionfortracking_lfw"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. "Deep Residual Learning for Image Recognition"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
