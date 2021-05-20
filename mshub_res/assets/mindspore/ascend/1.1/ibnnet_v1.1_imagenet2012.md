# ibnnet

---

model-name: ibnnet

backbone-name: ibnnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 77

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/ibnnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/ibnnet_ascend_v111_imagenet2012_research_cv_bs64_acc77/ibnnet_ascend_v111_imagenet2012_research_cv_bs64_acc77.ckpt>
    asset-sha256: d6ee1e4be7e9ac228ad3e1b45ba1d57291d80a00a49b88d769280aab78825ba9

license: Apache2.0

summary: ibnnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ibnnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/ibnnet.

ibnnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/ibnnet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/ibnnet/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/ibnnet_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Pan X ,  Ping L ,  Shi J , et al. Two at Once: Enhancing Learning and Generalization Capacities via IBN-Net[C]//
   European Conference on Computer Vision. Springer, Cham, 2018.
