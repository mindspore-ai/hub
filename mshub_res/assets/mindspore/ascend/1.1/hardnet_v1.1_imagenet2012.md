# hardnet

---

model-name: hardnet

backbone-name: hardnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v111

train-dataset: imagenet2012

accuracy: 77

author: MindSpore team

update-time: 2021-05-17

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/cv/hardnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v111

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/hardnet_ascend_v111_imagenet2012_research_cv_bs256_acc77/hardnet_ascend_v111_imagenet2012_research_cv_bs256_acc77.ckpt>
    asset-sha256: 7bd8f1c87371c71275495efef8ad18e754b303e61b50efe93b2e3f1379b47489

license: Apache2.0

summary: hardnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of hardnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/hardnet.

hardnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/hardnet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/cv/hardnet/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/hardnet_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Chao P ,  Kao C Y ,  Ruan Y , et al. HarDNet: A Low Memory Traffic Network[C]//
   2019 IEEE/CVF International Conference on Computer Vision (ICCV
