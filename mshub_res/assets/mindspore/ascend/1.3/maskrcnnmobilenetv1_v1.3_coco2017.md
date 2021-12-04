# maskrcnn_mobilenetv1

---

model-name: maskrcnn_mobilenetv1

backbone-name: MobileNetv1

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.3

train-dataset: coco2017

accuracy: 22.2

author: MindSpore team

update-time: 2021-09-27

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.3/model_zoo/official/cv/maskrcnn_mobilenetv1>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.3/maskrcnnmobilenetv1_ascend_v130_coco2017_official_cv_bs2_accbbox%3D22.2_segm%3D15.8/maskrcnnmobilenetv1_ascend_v130_coco2017_official_cv_bs2_accbbox%3D22.2_segm%3D15.8.ckpt>
    asset-sha256: 24b7da5bdca127b0c646adb873029a34d0b6be7c561de6f8e99bb6bccfc0f8db

license: Apache2.0

summary: maskrcnn_mobilenetv1 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of maskrcnn_mobilenetv1 from the MindSpore model zoo on Gitee at model_zoo/official/cv/maskrcnn_mobilenetv1.

maskrcnn_mobilenetv1 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/maskrcnn_mobilenetv1](https://gitee.com/mindspore/mindspore/blob/r1.3/model_zoo/official/cv/maskrcnn_mobilenetv1/README.md).

All parameters in the module are trainable.

backbone: [MobileNetv1](https://download.mindspore.cn/model_zoo/r1.3/mobilenetv1_ascend_v130_imagenet2012_official_cv_bs256_acc0/)

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.3/maskrcnnmobilenetv1_v1.3_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Kaiming He, Georgia Gkioxari, Piotr Dollar and Ross Girshick. "MaskRCNN"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.