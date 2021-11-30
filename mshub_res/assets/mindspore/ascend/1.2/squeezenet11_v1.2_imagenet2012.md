# squeezenet1_1

---

model-name: squeezenet1_1

backbone-name: squeezenet1_1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 58.65

author: MindSpore team

update-time: 2021-09-23

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/squeezenet1_1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/squeezenet11_ascend_v120_imagenet2012_research_cv_bs32_top1acc58.65__top5acc81.15/squeezenet11_ascend_v120_imagenet2012_research_cv_bs32_top1acc58.65__top5acc81.15.ckpt>
    asset-sha256: 125190347bd3ef03e4ed19513e2de2278f3ea2a563007fbfbe6859e74afdb11d

license: Apache2.0

summary: squeezenet1_1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenet1_1 from the MindSpore model zoo on Gitee at model_zoo/research/cv/squeezenet1_1.

squeezenet1_1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/squeezenet1_1](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/squeezenet1_1/README.md).

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

model = "mindspore/ascend/1.2/squeezenet11_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000)
network.set_train(False)

# ...
```

## Citation

1. Forrest N. Iandola and Song Han and Matthew W. Moskewicz and Khalid Ashraf and William J. Dally and Kurt Keutzer. "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.