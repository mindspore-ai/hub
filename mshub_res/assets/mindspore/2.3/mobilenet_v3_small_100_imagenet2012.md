# mobilenet_v3_small_100

---

model-name: mobilenet_v3_small_100

backbone-name: mobilenetv3

module-type: cv

fine-tunable: True

model-version: 2.3

train-dataset: ImageNet2012

evaluation: top1acc68.07 | top1acc87.77

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindcv/tree/v0.4.0/configs/mobilenetv3>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindcv/mobilenet/mobilenetv3/mobilenet_v3_small_100-6fa3c17d-910v2.ckpt>
    asset-sha256: 6fa3c17d

license: Apache2.0

summary: mobilenetv3 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv3 from the MindSpore.

mobilenetv3 is a cv network. More details please refer to the MindSpore-Lab on GitHub at [mobilenetv3](https://github.com/mindspore-lab/mindcv/blob/v0.4.0/configs/mobilenetv3/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/mobilenetv3_small_100_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[Searching for MobileNetV3](https://arxiv.org/pdf/1905.02244.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
