# GhostNet-SSD

---

model-name: ghostnet_ssd

backbone-name: ghostnet1.3x

module-type: CV

fine-tunable: True

input-shape: [3, 300, 300]

model-version: 1.0

train-dataset: coco

mAP: 0.241



author: Noah CVLab

update-time: 2020-09-08

repo-link: https://gitee.com/mindspore/mindspore/tree/master/model_zoo/research/cv/ssd_ghostnet

user-id: noah-cvlab

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

asset:
  -
    file-format: ckpt
    asset-link: https://download.mindspore.cn/model_zoo/research/cv/ssd_ghostnet/ssd-500_458.ckpt
    asset-sha256: 8b7790e5c034db9d3640fc0e03f95ab822cd5051e84308cbfef616028b488f3a

license: Apache2.0

summary: ssd_ghostnet is used to detect 80 classes of coco2017

---


## Introduction

This MindSpore Hub model uses the implementation of ssd_ghostnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssd_ghostnet.

This model has been trained on mscoco2017 using the code published on Gitee.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "noah-cvlab/ascend/1.0/ghostnet_ssd_v1.0_coco2017"
network = mshub.load(model)
network.set_train(False)

```

## Citation

1. [Paper](https://arxiv.org/abs/1512.02325):   Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
