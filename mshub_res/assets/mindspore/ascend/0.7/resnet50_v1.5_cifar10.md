# Resnet50

---

model-name: resnet50

backbone-name: resnet50

module-type: CV

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.5

train-dataset: cifar10

accuracy: 0.91



author: [network-fo]

update-time: 2020-08-26

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/resnet

user-id: mindspore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/resnet/resnet50_v1.5_ascend_0.3.0_cifar10_official_classification_20200718/resnet50.ckpt
    asset-sha256: 0fc976f5a3da2c15195e77023657d7d5f8635e23d6def443380c750e3d99247f
  -
    file-format: geir
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/resnet/resnet50_v1.5_ascend_0.3.0_cifar10_official_classification_20200718/resnet50.geir
    asset-sha256: 1849a8a78e9182d32567ea4fef1834ac765ce537ca6de3b1ec822efd6fb9b10b

license: Apache2.0
---

## Summary

This MindSpore Hub model uses the implementation of Resnet50 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

This model has been trained on Cifar10 using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from PIL import Image
import cv2

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/0.7/resnet50_v1.5_cifar10"
image_shape = mshub.get_desired_input_shape(model)

image = Image.open('cifar10/a.jpg')
transforms = py_transforms.ComposeOp([py_transforms.ToTensor()])

network = mshub.load(model)
network.set_train(False)
out = network(transforms(image))
```

## Citation

1. He K , Zhang X , Ren S , et al. Deep Residual Learning for Image Recognition[J]. 2016.
