# unet

---

model-name: unet

backbone-name: unet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: isbi

accuracy: 88

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/unet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/unet_ascend_v120_isbi_official_cv_bs16_acc88/unet_ascend_v120_isbi_official_cv_bs16_acc88.ckpt>
    asset-sha256: 8958839c6c52bc01e554ed0310a1dab6f50ca70acb8fe77270569b06d0b87b9a

license: Apache2.0

summary: unet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of unet from the MindSpore model zoo on Gitee at model_zoo/official/cv/unet.

unet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/unet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/unet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

num_classes = 2
num_channels = 1

model = "mindspore/ascend/1.2/unet_v1.2_isbi"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, n_classes=num_classes, n_channels=num_channels)
network.set_train(False)

# ...
```

## Citation

1. Olaf Ronneberger, Philipp Fischer, Thomas Brox. U-Net: Convolutional Networks for Biomedical Image Segmentation
