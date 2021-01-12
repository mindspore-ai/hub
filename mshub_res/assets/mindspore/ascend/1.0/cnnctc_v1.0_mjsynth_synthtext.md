# CNN&CTC

---

model-name: cnnctc

backbone-name: resnet50

module-type: cv-text-detection

fine-tunable: True

input-shape: [32, 100, 3]

model-version: 1

accuracy: 0.85

author: MindSpore team

update-time: 2020-12-31

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/cnnctc>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/official/cv/cnnctc/cnnctc_ascend_1.1.0_mjsynth_and_synthtext_official_text_recognition_20210111/cnnctc.ckpt>
    asset-sha256: c13a66f3edccb06a7b0f2e44ebe2080dba4760ceb7c7824670452e4c8c62cc3c

license: Apache2.0

summary: cnnctc used to test detection of MJSyncth and SynthText

---

## Introduction

This MindSpore Hub model uses the implementation of CNNCTC from the MindSpore model zoo on Gitee at model_zoo/official/cv/cnnctc.

This model has been trained on MJSyncth and SynthText using the code published on Gitee. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/cnnctc/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype
from mindspore.dataset.transforms import py_transforms
from src.config import Config_CNNCTC

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/cnnctc_v1.0_mjsynth_synthtext"

config = Config_CNNCTC
network = mshub.load(model, config.NUM_CLASS, config.HIDDEN_SIZE, config.FINAL_FEATURE_WIDTH)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/cv/cnnctc>.
```

## Citation

Paper: J. Baek, G. Kim, J. Lee, S. Park, D. Han, S. Yun, S. J. Oh, and H. Lee, “What is wrong with scene text recognition model comparisons? dataset and model analysis,” ArXiv, vol. abs/1904.01906, 2019.
