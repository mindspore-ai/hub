# retinanet_resnet152

---

model-name: retinanet_resnet152

backbone-name: retinanet_resnet152

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: coco2017

accuracy: 88

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/retinanet_resnet152>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/retinanet-resnet152_ascend_v111_coco2017_research_cv_bs_32_iou35/retinanet-resnet152_ascend_v111_coco2017_research_cv_bs_32_iou35.ckpt>
    asset-sha256: 171657b5cf1f983e331836c1e9e0fedfa3d09be4cb9e4ef90bee8c4eaa8a7652

license: Apache2.0

summary: retinanet_resnet152 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of retinanet_resnet152 from the MindSpore model zoo on Gitee at model_zoo/research/cv/retinanet_resnet152.

retinanet_resnet152 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/retinanet_resnet152](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/retinanet_resnet152/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/retinanet-resnet152_v1.1_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Lin T Y , Goyal P , Girshick R , et al. Focal Loss for Dense Object Detection[C]//
   2017 IEEE International Conference on Computer Vision (ICCV). IEEE, 2017:2999-3007.
