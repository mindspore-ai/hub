# Transformer

---

model-name: GNMT_v2

backbone-name: GNMTv2 Model

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128],[1, 128], [1, 128]]

model-version: 1.0

author: MindSpore team

update-time: 2020-12-23

repo-link: <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/gnmt_v2>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.0

license: Apache2.0
summary: gnmt_v2 used to do machine translation.

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/official/nlp/gnmt_v2/gnmt_v2_ascend_1.0_wmt_corpus_official_text_summarization_20201110/gnmt_ascend.ckpt>
    asset-sha256: 0ee1a22237143ae175c90f68c4970ae55fef0a683bc0ac6f5aacd78b6486bc8b

license: Apache2.0
summary: gnmt_v2 used to do machine translation.
---

## Introduction

This MindSpore Hub model uses the implementation of GNMTv2 from the MindSpore model zoo on Gitee at model_zoo/official/nlp/gnmt_v2.

This model support dynamic input shape depanding on the input sequence length, max sequence length is 128. More details please refer to the [MindSpore model zoo on Gitee](https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/gnmt_v2/README.md).

All Parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
import mindspore
from mindspore import context, Tensor, nn
from mindspore.train.model import Model
from mindspore.common import dtype as mstype

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.0/gnmt_v2_wmt"

network = mshub.load(model, is_training=False)
network.set_train(False)
# Use as the same as MindSpore Model to inference, please refer to <https://gitee.com/mindspore/mindspore/tree/master/model_zoo/official/nlp/gnmt_v2>.
```

## Citation

Paper: Wu Y , Schuster M , Chen Z , et al. Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation[J]. 2016.
