# unet3d

---

model-name: unet3d

backbone-name: unet3d

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: luna16

evaluation: acc96.54

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/unet3d>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/unet3d_ascend_v190_luna16_official_cv_acc96.54.ckpt>
    asset-sha256: 557eb7c3914428458f037bdf6d9320015021ebb3ccdb9740fe01823eed41027a

license: Apache2.0

summary: unet3d is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of unet3d from the MindSpore model zoo on Gitee at official/cv/unet3d.

unet3d is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/unet3d](https://gitee.com/mindspore/models/blob/r1.9/official/cv/unet3d/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.9/unet3d_luna16"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

[3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation](https://arxiv.org/pdf/1606.06650v1.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
