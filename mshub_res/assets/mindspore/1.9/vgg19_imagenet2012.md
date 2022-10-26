# vgg19

---

model-name: vgg19

backbone-name: vgg19

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: ImageNet2012

evaluation: top1acc74.22 | top5acc91.99

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/vgg19>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/vgg19_ascend_v190_imagenet2012_research_cv_top1acc74.22_top5acc91.99.ckpt>
    asset-sha256: eba330c2cfa6ea158716ec7be81075538280a4f006c5afe0ee7053a3d65de998

license: Apache2.0

summary: vgg19 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of vgg19 from the MindSpore model zoo on Gitee at research/cv/vgg19.

vgg19 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/vgg19](https://gitee.com/mindspore/models/blob/r1.9/research/cv/vgg19/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/vgg19_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
