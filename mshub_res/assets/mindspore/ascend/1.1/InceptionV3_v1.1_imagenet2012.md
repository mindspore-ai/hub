# InceptionV3

---

model-name: InceptionV3

backbone-name: InceptionV3

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

train-dataset: imagenet2012

accuracy: 0.78

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/inceptionv3>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/inceptionv3_ascned_v111__imagenet2012_offical_cv_bs128_acc78/inceptionv3_ascned_v111__imagenet2012_offical_cv_bs128_acc78.ckpt>
    asset-sha256: 4cca09f0ecf07f35616bfd3b67572942cafc554b272545a1d06783b93ce55f42

license: Apache2.0

summary: InceptionV3 used to classify the 1000 classes.

---

## Introduction

This MindSpore Hub model uses the implementation of InceptionV3 from the MindSpore model zoo on Gitee at [model_zoo/official/cv/inceptionv3](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/inceptionv3/README.md).

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/InceptionV3_v1.1_imagenet2012"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, num_classes=1000)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Szegedy, Christian，Vanhoucke, Vincent，Ioffe, Sergey，Shlens, Jonathon，Wojna, Zbigniew. Rethinking the Inception Architecture for Computer Vision[J]. 2015.