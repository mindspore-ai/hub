# maskrcnn

---

model-name: maskrcnn

backbone-name: maskrcnn

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: coco2017

evaluation: acc32.9

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/maskrcnn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/maskrcnn_ascend_v180_coco2017_official_cv_acc32.9.ckpt>
    asset-sha256: 5fa5a1e12cf64538c26a984cd4e1cdd418a5629bfe15b265bb7b49536a6a8a99

license: Apache2.0

summary: maskrcnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of maskrcnn from the MindSpore model zoo on Gitee at official/cv/maskrcnn.

maskrcnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/maskrcnn](https://gitee.com/mindspore/models/blob/r1.8/official/cv/maskrcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/maskrcnn_coco2017"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Kaiming He, Georgia Gkioxari, Piotr Dollar and Ross Girshick. "MaskRCNN"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
