# resnext101

---

model-name: resnext101

backbone-name: resnext

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1caa79.38 | top5acc94.71

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/resnext>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/resnext101_ascend_v160_imagenet2012_official_cv_top1caa79.38_top5acc94.71.ckpt>
    asset-sha256: 5f1bc48c45403e75e5639b3d73b11d700aadff39139de1f9f40adba4457548ec

license: Apache2.0

summary: resnext is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnext from the MindSpore model zoo on Gitee at official/cv/resnext.

resnext is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/resnext](https://gitee.com/mindspore/models/blob/r1.6/official/cv/resnext/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/resnext101_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Xie S, Girshick R, Dollár, Piotr, et al. Aggregated Residual Transformations for Deep Neural Networks. 2016.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
