# resnet50_thor

---

model-name: resnet50_thor

backbone-name: resnet_thor

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: imagenet2012

evaluation: top1acc76.08 | top5acc92.81

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/resnet_thor>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/resnet50thor_ascend_v150_imagenet2012_official_cv_top1acc76.08_top5acc92.81.ckpt>
    asset-sha256: ad9b3b0bef58cbc204493b84dd0da3972acdceb4d273233a99f890adbc905ffc

license: Apache2.0

summary: resnet_thor is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnet_thor from the MindSpore model zoo on Gitee at official/cv/resnet_thor.

resnet_thor is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/resnet_thor](https://gitee.com/mindspore/models/blob/r1.5/official/cv/resnet_thor/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/resnet50thor_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
