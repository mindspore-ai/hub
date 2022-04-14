# mobilenetv3

---

model-name: mobilenetv3

backbone-name: mobilenetv3

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: imagenet2012

evaluation: top1acc74.42

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/mobilenetv3>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/mobilenetv3_ascend_v130_imagenet2012_official_cv_top1acc74.42.ckpt>
    asset-sha256: f67f803c26e7ad40d9db4180fb74e1e996bde689b41db1778a934f4fe45308a5

license: Apache2.0

summary: mobilenetv3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv3 from the MindSpore model zoo on Gitee at official/cv/mobilenetv3.

mobilenetv3 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/mobilenetv3](https://gitee.com/mindspore/models/blob/r1.3/official/cv/mobilenetv3/Readme.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/mobilenetv3_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for mobilenetv3." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
