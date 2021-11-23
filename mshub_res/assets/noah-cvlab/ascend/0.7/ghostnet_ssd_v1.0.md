# GhostNet-SSD

---

model-name: GhostNet_SSD

backbone-name: ghostnet1.3x

module-type: cv-object_detection

fine-tunable: True

input-shape: [3, 300, 300]

model-version: 1.0

mAP: 0.241

author: Noah's Ark Lab

update-time: 2020-09-08

repo-link: <https://gitee.com/mindspore/models/tree/master/research/cv/ssd_ghostnet>

user-id: noah-cvlab

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 0.7

license: Apache2.0

summary: ssd_ghostnet is ssd model with ghostnet backbone

---

## Introduction

This MindSpore Hub model uses the implementation of ssd_ghostnet from the MindSpore model zoo on Gitee at model_zoo/official/cv/ssd_ghostnet.

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "noah-cvlab/ascend/0.7/ghostnet_ssd_v1.0"
network = mshub.load(model)
network.set_train(False)

```

## Citation

1. [Paper](https://arxiv.org/abs/1512.02325):   Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg.European Conference on Computer Vision (ECCV), 2016 (In press).
2. [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Han_GhostNet_More_Features_From_Cheap_Operations_CVPR_2020_paper.html):   Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu.Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 1580-1589.
