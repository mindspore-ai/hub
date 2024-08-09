# coat_tiny

---

model-name: coat_tiny

backbone-name: coat

module-type: cv

fine-tunable: True

model-version: 2.3

train-dataset: ImageNet2012

evaluation: top1acc79.28 | top5acc94.45

author: MindSpore team

update-time: 2024-8-9

repo-link: <https://github.com/mindspore-lab/mindcv/tree/v0.4.0/configs/coat>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindcv/coat/coat_tiny-dcca16b1-910v2.ckpt>
    asset-sha256: dcca16b1

license: Apache2.0

summary: coat is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of coat from the MindSpore.

coat is a cv network. More details please refer to the MindSpore-Lab on GitHub at [coat](https://github.com/mindspore-lab/mindcv/blob/v0.4.0/configs/coat/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/coat_tiny_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Co-Scale Conv-Attentional Image Transformers](https://arxiv.org/pdf/2104.06399v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
