# DS-CNN

---

model-name: dscnn

backbone-name: dscnn

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: Speech Commands Version1

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/research/nlp/dscnn>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/dscnn_ascend_v111_reseach_nlp_bs100_acc93/dscnn_ascend_v111_reseach_nlp_bs100_acc93.ckpt>
    asset-sha256: 24e20615fe5da2609ce451f1f2fcd3c39d7f6b4046da84bc8362a85ac144462d

license: Apache2.0

summary: This MindSpore Hub model uses the implementation of dscnn.dscnn is a audio network.

---

## Introduction

This MindSpore Hub model uses the implementation of dscnn from the MindSpore model zoo on Gitee at model_zoo/research/nlp/dscnn.

dscnn is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/nlp/dscnn](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/research/nlp/dscnn/README.md).

All parameters in the module are trainable.

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

model = "mindspore/ascend/1.1/dscnn_v1.1"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper:  Zhang, Yundong, Naveen Suda, Liangzhen Lai, and Vikas Chandra. "Hello edge: Keyword spotting on microcontrollers." arXiv preprint arXiv:1711.07128 (2017).
