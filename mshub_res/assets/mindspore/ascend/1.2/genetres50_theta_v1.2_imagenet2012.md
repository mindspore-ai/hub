# GENet_Res50

---

model-name: GENet_Res50

backbone-name: GENet_Res50

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 78.07

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/GENet_Res50>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/genetres50_theta_ascend_v120_imagenet2012_research_cv_bs256_top1acc78.07__top5acc93.93/genetres50_theta_ascend_v120_imagenet2012_research_cv_bs256_top1acc78.07__top5acc93.93.ckpt>
    asset-sha256: 44826193cafce1e97018e6b77712ecd077e2d5af4a03b2f3034b9772be80563d

license: Apache2.0

summary: GENet_Res50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of GENet_Res50 from the MindSpore model zoo on Gitee at model_zoo/research/cv/GENet_Res50.

GENet_Res50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/GENet_Res50](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/GENet_Res50/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/genetres50_theta_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
# extra: whether to use Depth-wise conv to down sample
mlp = "True"
# mlp: bottleneck whether to use 1*1 conv.
extra = "True"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Andrea Vedaldi. Gather-Excite: Exploiting Feature Context in Convolutional Neural Networks

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.