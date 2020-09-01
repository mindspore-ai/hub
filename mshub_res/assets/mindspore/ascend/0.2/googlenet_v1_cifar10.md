# GoogleNet

---

model-name: GoogleNet

backbone-name: GoogleNet

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.934



author: mindspore team

update-time: 2020-08-25

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/googlenet

user-id: mindspore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.2

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/googlenet/goolenet_ascend_0.2.0_cifar10_official_classification_20200713/googlenet.ckpt
    asset-sha256: 114e5acc31dad444fa8ed2aafa02ca34734419f602b9299f3b53013dfc71b0f7
  -
    file-format: air
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/googlenet/goolenet_ascend_0.2.0_cifar10_official_classification_20200713/googlenet.geir
    asset-sha256: a092a28211fcab98fdabdf00c95098587b8d84d0f33c2a4d29e2f6c43d3b0b60

license: Apache2.0

---

## Summary

This MindSpore Hub model uses the implementation of GoogleNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/googlenet.

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

model = "model_zoo/official/cv/googlenet"
image_shape = mshub.get_desired_input_shape(model)

image = Image.open('cifar10/a.jpg')
transforms = py_transforms.ComposeOp([py_transforms.ToTensor()])

network = mshub.load('mindspore/ascend/0.2/googlenet_v1_cifar10')
network.set_train(False)
out = network(transforms(image))
```

## Citation

1. Szegedy C, Liu W, Jia Y, et al. Going deeper with convolutions[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2015: 1-9.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
