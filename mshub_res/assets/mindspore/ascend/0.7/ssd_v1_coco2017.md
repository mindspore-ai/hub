# SSD

---

model-name: ssd

backbone-name: mobilenetV2

module-type: CV

fine-tunable: True

input-shape: [300, 300, 3]

model-version: 1

train-dataset: coco

map(0.95): 0.23



author: [network-fo]

update-time: 2020-09-10

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/ssd

user-id: mindspore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/ssd/ssd_ascend_0.3.0_coco2017_official_object_detection_20200717/ssd.ckpt
    asset-sha256: 29f52e7f8e3033e15d4423e0e1410b157cc81ff9fd31c1eef30ae862766c3617

    file-format: air
    asset-link: https://download.mindspore.cn/model_zoo/official/cv/ssd/ssd_ascend_0.3.0_coco2017_official_object_detection_20200717/ssd.geir
    asset-sha256: a385d49b3471582fbfec4a762afec771fe36a9dec706a4614256126641c5e7cc

license: Apache2.0

summary: ssd used to detect 80 classes of coco2017
---


## Introduction

This MindSpore Hub model uses the implementation of SSD from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssd.

This model has been trained on coco2017 using the code published on Gitee.

All parameters in the module are trainable.

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

model = "mindspore/ascend/0.7/ssd_v1_coco2017"
image_shape = mshub.get_desired_input_shape(model)

image = Image.open('coco2017/a.jpg')
transforms = py_transforms.ComposeOp([py_transforms.ToTensor()])

network = mshub.load(model)
network.set_train(False)
out = network(transforms(image))
```

## Citation

1. Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
