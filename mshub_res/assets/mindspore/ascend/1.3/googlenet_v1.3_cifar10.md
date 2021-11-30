# googlenet

---

model-name: googlenet

backbone-name: googlenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: cifar10

accuracy: 92.53

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/googlenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/googlenet_ascend_v130_cifar10_official_cv_bs128_acc92.53/googlenet_ascend_v130_cifar10_official_cv_bs128_acc92.53.ckpt>
    asset-sha256: b2f7fe14782a3ab88ad3534ed5f419b4bbc3b477706258bd6ed8f90f529775e7

license: Apache2.0

summary: googlenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of googlenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/googlenet.

googlenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/googlenet](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/googlenet/README.md).

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

model = "mindspore/ascend/1.3/googlenet_v1.3_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=10)
network.set_train(False)

# ...
```

## Citation

1. Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich. "Going deeper with convolutions." *Proceedings of the IEEE conference on computer vision and pattern recognition*. 2015.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.