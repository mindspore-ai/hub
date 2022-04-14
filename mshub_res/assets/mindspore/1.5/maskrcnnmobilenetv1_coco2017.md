# maskrcnn_mobilenetv1

---

model-name: maskrcnn_mobilenetv1

backbone-name: maskrcnn_mobilenetv1

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: coco2017

evaluation: bbox24.00 | segm21.5

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/cv/maskrcnn_mobilenetv1>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/maskrcnnmobilenetv1_ascend_v150_coco2017_official_cv_bbox24.00_segm21.5.ckpt>
    asset-sha256: 2e2baa51f404c4204c1303b432bca181491633c8f62dbfd38cdd34fa2543d743

license: Apache2.0

summary: maskrcnn_mobilenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of maskrcnn_mobilenetv1 from the MindSpore model zoo on Gitee at official/cv/maskrcnn_mobilenetv1.

maskrcnn_mobilenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/maskrcnn_mobilenetv1](https://gitee.com/mindspore/models/blob/r1.5/official/cv/maskrcnn_mobilenetv1/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.5/maskrcnnmobilenetv1_coco2017"
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
