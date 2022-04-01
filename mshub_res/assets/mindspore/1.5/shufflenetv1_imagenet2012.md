# shufflenetv1

---

model-name: shufflenetv1

backbone-name: shufflenetv1

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: imagenet2012

evaluation: top1acc73.83 | top5acc91.54

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/shufflenetv1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/shufflenetv1_ascend_v150_imagenet2012_official_cv_top1acc73.83_top5acc91.54.ckpt>
    asset-sha256: 9e484f77bf133ba65ecc6ac28c04d76e45fc822fdf4fb1636fd83dd30de0e462

license: Apache2.0

summary: shufflenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of shufflenetv1 from the MindSpore model zoo on Gitee at official/cv/shufflenetv1.

shufflenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/shufflenetv1](https://gitee.com/mindspore/models/blob/r1.5/official/cv/shufflenetv1/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/shufflenetv1_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Xiangyu Zhang, Xinyu Zhou, Mengxiao Lin, Jian Sun. "ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices." *Proceedings of the IEEE conference on computer vision and pattern recognition*. 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
