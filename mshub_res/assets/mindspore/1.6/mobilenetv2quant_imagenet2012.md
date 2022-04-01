# mobilenetv2_quant

---

model-name: mobilenetv2_quant

backbone-name: mobilenetv2_quant

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc71 | top5acc90

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/mobilenetv2_quant>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/mobilenetv2quant_ascend_v160_imagenet2012_official_cv_top1acc71_top5acc90.ckpt>
    asset-sha256: 159439c2a76851460f42d66087f12558c8a0a7ec781c2ec4978e8684ae29887f

license: Apache2.0

summary: mobilenetv2_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of mobilenetv2_quant from the MindSpore model zoo on Gitee at official/cv/mobilenetv2_quant.

mobilenetv2_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/mobilenetv2_quant](https://gitee.com/mindspore/models/blob/r1.6/official/cv/mobilenetv2_quant/Readme.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.6/mobilenetv2quant_imagenet2012"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

Howard, Andrew, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang et al. "Searching for MobileNetV2." In Proceedings of the IEEE International Conference on Computer Vision, pp. 1314-1324. 2019.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
