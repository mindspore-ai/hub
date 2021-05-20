# simple_baselines

---

model-name: simple_baselines

backbone-name: simple_baselines

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: coco2017

accuracy: 88

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/simple_baselines>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/simple-baselines_ascend_v111_coco2017_research_cv_bs64_iou71/simple-baselines_ascend_v111_coco2017_research_cv_bs64_iou71.ckpt>
    asset-sha256: 5f8c4269fe7d5ff2655c2bce8814bc468d891b7e00e21f4d9a3c3247eee76a5e

license: Apache2.0

summary: simple_baselines is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of simple_baselines from the MindSpore model zoo on Gitee at model_zoo/research/cv/simple_baselines.

simple_baselines is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/simple_baselines](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/simple_baselines/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/simple-baselines_v1.1_coco2017"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Bin Xiao, Haiping Wu, Yichen Wei."Simple baselines for human pose estimation and tracking"
