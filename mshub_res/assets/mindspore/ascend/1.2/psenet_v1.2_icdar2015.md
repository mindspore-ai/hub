# psenet

---

model-name: psenet

backbone-name: psenet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: icdar2015

accuracy: 84

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/psenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/psenet_ascend_v120_icdar2015_official_cv_bs4_acc84_recall77_hmean81/psenet_ascend_v120_icdar2015_official_cv_bs4_acc84_recall77_hmean81.ckpt>
    asset-sha256: 0a43c2aa54fbb079aa716745607bf784d208f8d49532642b502271d022fb3519

license: Apache2.0

summary: psenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of psenet from the MindSpore model zoo on Gitee at model_zoo/official/cv/psenet.

psenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/psenet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/psenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/psenet_v1.2_icdar2015"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Wenhai Wang, Enze Xie, Xiang Li, Wenbo Hou, Tong Lu, Gang Yu, Shuai Shao; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9336-9345
