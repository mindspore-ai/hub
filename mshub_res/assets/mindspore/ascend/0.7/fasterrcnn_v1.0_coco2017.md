# FasterRcnn

---

model-name: faster_rcnn

backbone-name: resnet50

module-type: cv-object_detection

fine-tunable: True

input-shape: [768, 1280, 3]

model-version: 1

mAP(0.5): 0.576

author: MindSpore team

update-time: 2020-09-10

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/faster_rcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

license: Apache2.0

summary: fasterrcnn used to detect 80 classes of coco2017

---

## Introduction

This MindSpore Hub model uses the implementation of FasterRcnn from the MindSpore model zoo on Gitee at model_zoo/official/cv/faster_rcnn.

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

model = "mindspore/ascend/0.7/fasterrcnn_v1_coco2017"

network = mshub.load(model, is_training=False)
network.set_train(False)
```

## Citation

1. Ren S , He K , Girshick R , et al. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2015, 39(6).
