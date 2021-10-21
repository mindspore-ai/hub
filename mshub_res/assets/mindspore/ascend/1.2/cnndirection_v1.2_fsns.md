# cnn_direction_model

---

model-name: cnn_direction_model

backbone-name: cnn_direction_model

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: fsns

accuracy: 99

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/cnn_direction_model>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/cnndirection_ascend_v120_fsns_official_cv_bs8_acc99/cnndirection_ascend_v120_fsns_official_cv_bs8_acc99.ckpt>
    asset-sha256: 7f3c235b3bc2ad43012204983bb51f32c9a08b91b12bfec42d1d3f207e02cba1

license: Apache2.0

summary: cnn_direction_model is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of cnn_direction_model from the MindSpore model zoo on Gitee at model_zoo/official/cv/cnn_direction_model.

cnn_direction_model is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/cnn_direction_model](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/cnn_direction_model/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/cnndirection_v1.2_fsns"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
