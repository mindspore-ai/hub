# dscnn

---

model-name: dscnn

backbone-name: dscnn

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: 1.2

train-dataset: speech

accuracy: 93

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/research/nlp/dscnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/dscnn_ascend_v120_speech_research_nlp_bs100_acc93/dscnn_ascend_v120_speech_research_nlp_bs100_acc93.ckpt>
    asset-sha256: 180ca28686f9a3ad4a2ff463988c660edc389baa39f69fa0367b05cdc39b3de4

license: Apache2.0

summary: dscnn is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of dscnn from the MindSpore model zoo on Gitee at model_zoo/research/nlp/dscnn.

dscnn is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/research/nlp/dscnn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/research/nlp/dscnn/README.md).

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

model = "mindspore/ascend/1.2/dscnn_v1.2_speech"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation

1. Zhang, Yundong, Naveen Suda, Liangzhen Lai, and Vikas Chandra. "Hello edge: Keyword spotting on microcontrollers." arXiv preprint arXiv:1711.07128 (2017).
