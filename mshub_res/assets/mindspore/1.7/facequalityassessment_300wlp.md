# FaceQualityAssessment

---

model-name: FaceQualityAssessment

backbone-name: FaceQualityAssessment

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: 300wlp

evaluation: IPN19 | MAE18

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/FaceQualityAssessment>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/facequalityassessment_ascend_v170_300wlp_research_cv_IPN19_MAE18.ckpt>
    asset-sha256: 07e44357d9a9a2b30677479e6bfce8a867d8333a16a20f22eca6e08d9f35a4c6

license: Apache2.0

summary: FaceQualityAssessment is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FaceQualityAssessment from the MindSpore model zoo on Gitee at research/cv/FaceQualityAssessment.

FaceQualityAssessment is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/FaceQualityAssessment](https://gitee.com/mindspore/models/blob/r1.7/research/cv/FaceQualityAssessment/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.7/facequalityassessment_300wlp"
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
