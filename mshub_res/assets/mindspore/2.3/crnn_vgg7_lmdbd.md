# crnn_vgg7

---

model-name: crnn_vgg7

backbone-name: vgg7

module-type: cv

fine-tunable: True

model-version: 2.3

train-dataset: LMDBDataset

evaluation: acc81.3

author: MindSpore team

update-time: 2024-8-1

repo-link: <https://github.com/mindspore-lab/mindocr/tree/v0.4.0/configs/rec/crnn>

user-id: MindSpore

used-for: inference

mindspore-version: 2.3

asset:

-
    file-format: ckpt
    asset-link: <https://download-mindspore.osinfra.cn/toolkits/mindocr/crnn/crnn_vgg7-6faf1b2d-910v2.ckpt>
    asset-sha256: 6faf1b2d

license: Apache2.0

summary: crnn_vgg7 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of crnn_vgg7 from the MindSpore.

crnn_vgg7 is a cv network. More details please refer to the MindSpore-Lab on GitHub at [crnn_vgg7](https://github.com/mindspore-lab/mindocr/blob/v0.4.0/configs/rec/crnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/2.3/crnn_vgg7_lmdbd.md"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition](https://arxiv.org/pdf/1507.05717.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
