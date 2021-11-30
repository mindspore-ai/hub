# mobilenetv2_quant

---

model-name: mobilenetv2_quant

backbone-name: mobilenetv2_quant

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 72

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/mobilenetv2_quant>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/mobilenetv2quant_ascend_v120_imagenet2012_official_cv_bs192_acc72/mobilenetv2quant_ascend_v120_imagenet2012_official_cv_bs192_acc72.ckpt>
    asset-sha256: 483abdc6a094ff2d782e6d0cb2da71821f2e27f845039095c62302cea100bed3

license: Apache2.0

summary: mobilenetv2_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv2_quant from the MindSpore model zoo on Gitee at model_zoo/official/cv/mobilenetv2_quant.

mobilenetv2_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/mobilenetv2_quant](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/mobilenetv2_quant/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/mobilenetv2quant_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.