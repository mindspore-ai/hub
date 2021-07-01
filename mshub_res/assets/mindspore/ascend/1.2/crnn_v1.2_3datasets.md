# crnn

---

model-name: crnn

backbone-name: crnn

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: 3datasets

accuracy: 3

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/crnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/crnn_ascend_v120_3datasets_official_cv_bs64_acc3/crnn_ascend_v120_3datasets_official_cv_bs64_acc3.ckpt>
    asset-sha256: fc85e1507eb6edee8646234d0187d0dac83a9b519bfd94bc06b048ab41d01840

license: Apache2.0

summary: crnn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of crnn from the MindSpore model zoo on Gitee at model_zoo/official/cv/crnn.

crnn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/crnn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/crnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/crnn_v1.2_3datasets"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Baoguang Shi, Xiang Bai, Cong Yao, "An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition", ArXiv, vol. abs/1507.05717, 2015.
