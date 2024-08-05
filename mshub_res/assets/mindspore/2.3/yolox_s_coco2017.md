# yolox_s

---

model-name: yolox_s

backbone-name: yolox

module-type: cv

fine-tunable: True

model-version: 2.3

train-dataset: COCO2017

evaluation: mAP41.0

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindyolo/tree/v0.4.0/configs/yolox>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindyolo/yolox/yolox-s_300e_map407-cebd0183-910v2.ckpt>
    asset-sha256: cebd0183

license: Apache2.0

summary: yolox is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolox from the MindSpore.

yolox is a cv network. More details please refer to the MindSpore-Lab on GitHub at [yolox](https://github.com/mindspore-lab/mindyolo/blob/v0.4.0/configs/yolox/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/yolox_s_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[YOLOX: Exceeding YOLO Series in 2021](https://arxiv.org/pdf/2107.08430.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
