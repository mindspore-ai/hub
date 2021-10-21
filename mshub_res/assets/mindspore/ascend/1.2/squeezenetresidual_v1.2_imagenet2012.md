# squeezenetresidual

---

model-name: squeezenetresidual

backbone-name: squeezenetresidual

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: imagenet2012

accuracy: 60

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/squeezenet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/squeezenetresidual_ascend_v120_imagenet2012_official_cv_bs32_acc60/squeezenetresidual_ascend_v120_imagenet2012_official_cv_bs32_acc60.ckpt>
    asset-sha256: f37d9abd46fc42d86dcb15da40e88fa08365b29eccca72e08fcaf0167e0b31dd

license: Apache2.0

summary: squeezenetresidual is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of squeezenetresidual from the MindSpore model zoo on Gitee at model_zoo/official/cv/squeezenetresidual.

squeezenetresidual is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/squeezenetresidual](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/squeezenet/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/squeezenetresidual_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, dataset="imagenet2012")
network.set_train(False)

# ...
```

## Citation
