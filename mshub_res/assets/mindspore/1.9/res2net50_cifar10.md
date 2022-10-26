# res2net50

---

model-name: res2net50

backbone-name: res2net

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cifar10

evaluation: top1acc94.86 | top5acc99.88

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/res2net>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/res2net50_ascend_v190_cifar10_research_cv_top1acc94.86_top5acc99.88.ckpt>
    asset-sha256: 51493adc602d5024ea4b6476f55a3bff12723355fbd20da5e3262f4b72e51d2c

license: Apache2.0

summary: res2net is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of res2net from the MindSpore model zoo on Gitee at research/cv/res2net.

res2net is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/res2net](https://gitee.com/mindspore/models/blob/r1.9/research/cv/res2net/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/res2net50_cifar10"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Res2Net: A New Multi-scale Backbone Architecture](https://arxiv.org/pdf/1904.01169.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
