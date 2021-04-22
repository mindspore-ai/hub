# ResNet101

---

model-name: resnet101

backbone-name: resnet101

module-type: cv-classification

fine-tunable: True

input-shape: [224, 224, 3]

model-version: 1.1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/resnet>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/resnet101_ascend_v111_imagenet2012_offical_cv_bs32_acc78/resnet101_ascend_v111_imagenet2012_offical_cv_bs32_acc78.ckpt>
    asset-sha256: 5c2ed6fe87011fc83bae9913eb316aa42a439a326afe43451b16d37b94b928b6

license: Apache2.0

summary: resnet101 for image classification

---

## Introduction

This MindSpore Hub model uses the implementation of ResNet101 from the MindSpore model zoo on Gitee at model_zoo/official/cv/resnet.

More details please refer to the MindSpore model zoo on Gitee [model_zoo/official/cv/resnet](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/resnet/README.md).

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

model = "mindspore/ascend/1.1/resnet101_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

1. Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Enhua Wu. "Squeeze-and-Excitation Networks"
