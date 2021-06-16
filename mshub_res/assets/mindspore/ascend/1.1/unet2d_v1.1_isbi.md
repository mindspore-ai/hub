# UNET2D

---

model-name: unet2d

backbone-name: unet

module-type: cv-semantic_segmentation

fine-tunable: True

input-shape: [388, 388, 3]

model-version: 1.1

train-dataset: isbi

dice_coeff: 0.908

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/unet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/unet_ascend_v111_isbi_offical_cv_bs16_acc91/unet_ascend_v111_isbi_offical_cv_bs16_acc91.ckpt>
    asset-sha256: 8f8ba6dd04f153391cf71b9a7cadf57052f221158c36fd13f3b944bf4d792de8

license: Apache2.0

summary: unet used to 2D image segmentation of ISBI challenge

---

## Introduction

This MindSpore Hub model uses the implementation of Unet2D from the MindSpore model zoo on Gitee [model_zoo/official/cv/unet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/unet/README.md).

This model has been trained on ISBI Challenge using the code published on Gitee.

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/unet2d_v1.1_isbi"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, n_channels=1, n_classes=2)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper: Olaf Ronneberger, Philipp Fischer, Thomas Brox. "U-Net: Convolutional Networks for Biomedical Image Segmentation." *conditionally accepted at MICCAI 2015*. 2015.
