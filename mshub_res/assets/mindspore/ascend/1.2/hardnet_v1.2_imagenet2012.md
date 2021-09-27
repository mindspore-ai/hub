# hardnet

---

model-name: hardnet

backbone-name: hardnet

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: imagenet2012

accuracy: 77.65

author: MindSpore team

update-time: 2021-09-14

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/cv/hardnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/hardnet_ascend_v120_imagenet2012_research_cv_bs256_top1acc77.65__top5acc93.25/hardnet_ascend_v120_imagenet2012_research_cv_bs256_top1acc77.65__top5acc93.25.ckpt>
    asset-sha256: 299aad036e2bab5a7dc97b621756b9a0985e2ecb03e26ff7492565c655ce7dc9

license: Apache2.0

summary: hardnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of hardnet from the MindSpore model zoo on Gitee at model_zoo/research/cv/hardnet.

hardnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/cv/hardnet](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/cv/hardnet/README_CN.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore
import mindspore_hub as mshub
from mindspore import Tensor
from mindspore import nn
from mindspore import context
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/hardnet_v1.2_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Chao P ,  Kao C Y ,  Ruan Y , et al. HarDNet: A Low Memory Traffic Network[C]// 2019 IEEE/CVF International Conference on Computer Vision (ICCV
