# faster_rcnn

---

model-name: faster_rcnn

backbone-name: faster_rcnn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: coco2017

accuracy: 59

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/faster_rcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/fasterrcnn_ascend_v120_coco2017_official_cv_bs2_acc59/fasterrcnn_ascend_v120_coco2017_official_cv_bs2_acc59.ckpt>
    asset-sha256: 91e2ccbc5e6e97a5c0d5ef1bea40ae9f1adef37636b552718cdf018b50e7d2ca

license: Apache2.0

summary: faster_rcnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of faster_rcnn from the MindSpore model zoo on Gitee at model_zoo/official/cv/faster_rcnn.

faster_rcnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/faster_rcnn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/faster_rcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/fasterrcnn_v1.2_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Ren S , He K , Girshick R , et al. Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2015, 39(6).
