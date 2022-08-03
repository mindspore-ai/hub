# unet2d

---

model-name: unet2d

backbone-name: unet

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: isbichallenge

evaluation: iou90.00

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/unet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/unet2d_ascend_v180_isbichallenge_official_cv_iou90.00.ckpt>
    asset-sha256: 93f9d423c6a6cd98c5123d8800230debff9d1cb276250d637c0b086f1e323a6f

license: Apache2.0

summary: unet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of unet from the MindSpore model zoo on Gitee at official/cv/unet.

unet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/unet](https://gitee.com/mindspore/models/blob/r1.8/official/cv/unet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.8/unet2d_isbichallenge"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Olaf Ronneberger, Philipp Fischer, Thomas Brox. "U-Net: Convolutional Networks for Biomedical Image Segmentation." conditionally accepted at MICCAI 2015. 2015.
2. Z. Zhou, M. M. R. Siddiquee, N. Tajbakhsh and J. Liang, "UNet++: Redesigning Skip Connections to Exploit Multiscale Features in Image Segmentation," in IEEE Transactions on Medical Imaging, vol. 39, no. 6, pp. 1856-1867, June 2020, doi: 10.1109/TMI.2019.2959609.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
