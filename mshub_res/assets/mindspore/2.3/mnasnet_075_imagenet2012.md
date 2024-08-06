# mnasnet_075

---

model-name: mnasnet_075

backbone-name: mnasnet

module-type: cv

fine-tunable: True

model-version: 2.3

train-dataset: ImageNet2012

evaluation: top1acc71.77 | top5acc90.52

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindcv/tree/v0.4.0/configs/mnasnet>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindcv/mnasnet/mnasnet_075-083b2bc4-910v2.ckpt>
    asset-sha256: 083b2bc4

license: Apache2.0

summary: mnasnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mnasnet from the MindSpore.

mnasnet is a cv network. More details please refer to the MindSpore-Lab on GitHub at [mnasnet](https://github.com/mindspore-lab/mindcv/blob/v0.4.0/configs/mnasnet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/mnasnet_075_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[MnasNet: Platform-Aware Neural Architecture Search for Mobile](https://arxiv.org/pdf/1807.11626.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
