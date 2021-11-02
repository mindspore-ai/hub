# unet3d

---

model-name: unet3d

backbone-name: unet3d

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: luna16

accuracy: 96

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/unet3d>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/unet3d_ascend_v120_luna16_official_cv_bs1_acc96/unet3d_ascend_v120_luna16_official_cv_bs1_acc96.ckpt>
    asset-sha256: 557eb7c3914428458f037bdf6d9320015021ebb3ccdb9740fe01823eed41027a

license: Apache2.0

summary: unet3d is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of unet3d from the MindSpore model zoo on Gitee at model_zoo/official/cv/unet3d.

unet3d is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/unet3d](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/unet3d/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/unet3d_v1.2_luna16"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. ̈Ozg ̈un C ̧ i ̧cek, Ahmed Abdulkadir, Soeren S. Lienkamp, ThomasBrox, Olaf Ronneberger. 3D U-Net: Learning Dense VolumetricSegmentation from Sparse Annotation
