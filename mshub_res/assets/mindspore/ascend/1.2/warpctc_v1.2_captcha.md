# warpctc

---

model-name: warpctc

backbone-name: warpctc

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: captcha

accuracy: 99

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/warpctc>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/warpctc_ascend_v120_captcha_official_cv_bs64_acc99/warpctc_ascend_v120_captcha_official_cv_bs64_acc99.ckpt>
    asset-sha256: e76be3feade9d85e18b268b6cd70ff91b32d9021bb23c87d57baf291f7f57975

license: Apache2.0

summary: warpctc is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of warpctc from the MindSpore model zoo on Gitee at model_zoo/official/cv/warpctc.

warpctc is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/warpctc](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/warpctc/README.md).

All parameters in the module are trainable.

## Usage

```python
import math as m
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

captcha_height = 64 # from warcpctc deafult_config.yaml
input_size = m.ceil(captcha_height / 64) * 64 * 3

model = "mindspore/ascend/1.2/warpctc_v1.2_captcha"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, input_size=input_size)
network.set_train(False)

# ...
```

## Citation
