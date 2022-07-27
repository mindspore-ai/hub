# shufflenetv2

---

model-name: shufflenetv2

backbone-name: shufflenetv2

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: imagenet2012

evaluation: top1acc69.49 | top5acc88.65

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/shufflenetv2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/shufflenetv2_ascend_v180_imagenet2012_official_cv_top1acc69.49_top5acc88.65.ckpt>
    asset-sha256: fa0df70441b6c7d051f4bd7ade689c63670dd866104a86c1de37c8d4354ca5c2

license: Apache2.0

summary: shufflenetv2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of shufflenetv2 from the MindSpore model zoo on Gitee at official/cv/shufflenetv2.

shufflenetv2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/shufflenetv2](https://gitee.com/mindspore/models/blob/r1.8/official/cv/shufflenetv2/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/shufflenetv2_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Ma, N., Zhang, X., Zheng, H. T., & Sun, J. (2018). Shufflenet v2: Practical guidelines for efficient cnn architecture design. In Proceedings of the European conference on computer vision (ECCV) (pp. 116-131).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
