# AlexNet

---

model-name: AlexNet

backbone-name: AlexNet

module-type: CV

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.0

train-dataset: cifar10

accuracy: 0.99



author: [network-fo]

update-time: 2020-07-20

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/alexnet

user-id: mindspore



file-format: ckpt

used-for: inference

train-backend: gpu

infer-backend: gpu

mindspore-version: 0.6

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/alexnet/alexnet_ascend_0.5.0_cifar10_official_classification_20200716/alexnet.ckpt
    asset-sha256: 722e13be6cd6186dddcd68d5c0a50776d9a8ad8e79db3870556f68d4d2f179e4
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/alexnet/alexnet_ascend_0.5.0_cifar10_official_classification_20200716/alexnet.ckpt
    asset-sha256: 722e13be6cd6186dddcd68d5c0a50776d9a8ad8e79db3870556f68d4d2f179e4

license: Apache2.0

---

## Summary

This MindSpore Hub model uses the implementation of AlexNet from the MindSpore model zoo on Gitee at model_zoo/official/cv/alexnet.

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

model = "model_zoo/official/cv/alexnet"
image_shape = mshub.get_desired_input_shape(model)

image = Image.open('cifar10/a.jpg')
transforms = py_transforms.ComposeOp([py_transforms.ToTensor()])

network = mshub.load('model_zoo/official/cv/alexnet')
network.set_train(False)
out = network(transforms(image))
```

## Citation

1. Krizhevsky A, Sutskever I, Hinton G E. Imagenet classification with deep convolutional neural networks[C]//Advances in neural information processing systems. 2012: 1097-1105.
2. Krizhevsky A, Hinton G. Learning multiple layers of features from tiny images[J].2009.
