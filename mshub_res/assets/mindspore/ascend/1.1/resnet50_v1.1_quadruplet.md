# metric_learn

---

model-name: metric_learn

backbone-name: metric_learn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: sop

accuracy: 74

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/metric_learn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/resnet50-quadruplet_ascend_v111_sop_research_cv_bs60_acc74/resnet50-quadruplet_ascend_v111_sop_research_cv_bs60_acc74.ckpt>
    asset-sha256: 9897589daa93d4fbb80959f59b4c5319ff12ed495e7bfcd4cf3c895e6d1c3c21

license: Apache2.0

summary: metric_learn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of metric_learn from the MindSpore model zoo on Gitee at model_zoo/research/cv/metric_learn.

metric_learn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/metric_learn](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/metric_learn/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/resnet50_v1.1_quadruplet"
# set the dataset param, default is quadruplet
dataset = "quadruplet"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, task_name=dataset)
network.set_train(False)

# ...
```

## Citation

1. F Schroff, Kalenichenko D,Philbin J."FaceNet: A Unified Embedding for Face Recognition and Clustering"
2. Chen W, Chen X, Zhang J."Beyond triplet loss: A deep quadruplet network for person re-identification"
