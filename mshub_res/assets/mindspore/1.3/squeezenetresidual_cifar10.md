# squeezenet_residual

---

model-name: squeezenet

backbone-name: squeezenet

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: cifar10

evaluation: top1acc87.25 | top5acc99.57

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/official/cv/squeezenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/squeezenetresidual_ascend_v130_cifar10_official_cv_top1acc87.25_top5acc99.57.ckpt>
    asset-sha256: 5451da81fe3644f6ed2cae202aed49d08780de576b81828db2bfd3f293096e93

license: Apache2.0

summary: squeezenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenet from the MindSpore model zoo on Gitee at official/cv/squeezenet.

squeezenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/squeezenet](https://gitee.com/mindspore/models/blob/r1.3/official/cv/squeezenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.3/squeezenetresidual_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Forrest N. Iandola and Song Han and Matthew W. Moskewicz and Khalid Ashraf and William J. Dally and Kurt Keutzer. "SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
