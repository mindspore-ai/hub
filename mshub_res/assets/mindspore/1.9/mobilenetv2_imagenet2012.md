# mobilenetv2

---

model-name: mobilenetv2

backbone-name: mobilenetv2

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc71.88

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/mobilenetv2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/mobilenetv2_ascend_v190_imagenet2012_official_cv_top1acc71.88.ckpt>
    asset-sha256: f1796a887a3e8699f048c78b58a477cbee1464509af66aed65a09536cfbd4f48

license: Apache2.0

summary: mobilenetv2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv2 from the MindSpore model zoo on Gitee at official/cv/mobilenetv2.

mobilenetv2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/mobilenetv2](https://gitee.com/mindspore/models/blob/r1.9/official/cv/mobilenetv2/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/mobilenetv2_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
