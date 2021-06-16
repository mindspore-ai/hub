# CNN&CTC

---

model-name: cnnctc

backbone-name: resnet50

module-type: cv

fine-tunable: True

input-shape: [32, 100, 3]

model-version: 1.1

train-dataset: MJSynth

accuracy: 0.85

author: MindSpore team

update-time: 2021-4-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/cv/cnnctc>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

-
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/cnnctc_ascend_v111_offical_cv_bs192_acc85/cnnctc_ascend_v111_offical_cv_bs192_acc85.ckpt>
    asset-sha256: c6a340120565c3b93ed7e63a9bc2a69428510000051338f4ae0f6b66ea4623dd

license: Apache2.0

summary: cnnctc used to test detection of MJSyncth and SynthText

---

## Introduction

This MindSpore Hub model uses the implementation of cnnctc from the MindSpore model zoo on Gitee at model_zoo/official/cv/cnnctc.

cnnctc is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/cnnctc](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/cv/cnnctc/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from model_zoo.official.cv.cnnctc.src.config import Config_CNNCTC

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.1/cnnctc_v1.1_MJSynth"

config = Config_CNNCTC
network = mshub.load(model, config.NUM_CLASS, config.HIDDEN_SIZE, config.FINAL_FEATURE_WIDTH)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/cnnctc>.
```

## Citation

Paper: J. Baek, G. Kim, J. Lee, S. Park, D. Han, S. Yun, S. J. Oh, and H. Lee, “What is wrong with scene text recognition model comparisons? dataset and model analysis,” ArXiv, vol. abs/1904.01906, 2019.
