# InceptionV4

---

model-name: InceptionV4

backbone-name: InceptionV4

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: imagenet2012

accuracy: 0.80

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/inceptionv4>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/inception4_ascned_v111__imagenet2012_offical_cv_bs128_acc80/inception4_ascned_v111__imagenet2012_offical_cv_bs128_acc80.ckpt>
    asset-sha256: 752b99d9ccbec512870e3903b17d1a756258cf52ca6c0e0d30e6214daf61155e

license: Apache2.0

summary: InceptionV4 used to classify the 1000 classes.

---

## Introduction

This MindSpore Hub model uses the implementation of inceptionv4 from the MindSpore model zoo on Gitee at model_zoo/official/cv/inceptionv4.

inceptionv4 is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/inceptionv4](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/inceptionv4/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/inceptionv4_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Szegedy, Christian，Vanhoucke, Vincent，Ioffe, Sergey，Shlens, Jonathon，Wojna, Zbigniew. Rethinking the Inception Architecture for Computer Vision[J]. 2015.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.