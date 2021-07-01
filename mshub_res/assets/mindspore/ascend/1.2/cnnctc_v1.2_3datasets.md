# cnnctc

---

model-name: cnnctc

backbone-name: cnnctc

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: 3datasets

accuracy: 86

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/cnnctc>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/cnnctc_ascend_v120_3datasets_official_cv_bs192_acc86/cnnctc_ascend_v120_3datasets_official_cv_bs192_acc86.ckpt>
    asset-sha256: 1d186dd844e0353d5af4babf5a8b18ccc76f0292517ecaf2cc470e5276168282

license: Apache2.0

summary: cnnctc is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of cnnctc from the MindSpore model zoo on Gitee at model_zoo/official/cv/cnnctc.

cnnctc is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/cnnctc](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/cnnctc/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)
num_class = 37
hidden_size = 512
final_feature_width = 26

model = "mindspore/ascend/1.2/cnnctc_v1.2_3datasets"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model,
                     num_class=num_class,
                     hidden_size=hidden_size,
                     final_feature_width=final_feature_width)
network.set_train(False)

# ...
```

## Citation

1. J. Baek, G. Kim, J. Lee, S. Park, D. Han, S. Yun, S. J. Oh, and H. Lee, “What is wrong with scene text recognition model comparisons? dataset and model analysis,” ArXiv, vol. abs/1904.01906, 2019.
