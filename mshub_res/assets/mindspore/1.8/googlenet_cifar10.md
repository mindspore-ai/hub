# googlenet

---

model-name: googlenet

backbone-name: googlenet

module-type: cv-classification

fine-tunable: True

model-version: 1.8

train-dataset: cifar10

evaluation: acc92.1

author: MindSpore team

update-time: 2022-08-10

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/googlenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/googlenet_ascend_v180_cifar10_official_cv_acc92.1.ckpt>
    asset-sha256: 5c7b8383a489bb3410242371f829cebfe83469201f44e9f2c36b797fe5112a29

license: Apache2.0

summary: googlenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of googlenet from the MindSpore model zoo on Gitee at official/cv/googlenet.

googlenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/googlenet](https://gitee.com/mindspore/models/blob/r1.8/official/cv/googlenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/googlenet_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich. "Going deeper with convolutions." *Proceedings of the IEEE conference on computer vision and pattern recognition*. 2015.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
