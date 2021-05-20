# TextCNN

---

model-name: textcnn

backbone-name: textcnn

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: mr

author: MindSpore team

update-time: 2021-04-15

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.1/model_zoo/official/nlp/textcnn>

user-id: MindSpore

used-for: inference/transfer-learning

train-backend: ascend

infer-backend: ascend

mindspore-version: 1.1

asset:

  -
    file-format: ckpt  
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/textcnn_ascend_v111_mr_offical_nlp_bs64_acc78/textcnn_ascend_v111_mr_offical_nlp_bs64_acc78.ckpt>
    asset-sha256: 1dbfbe14d9156c3678cd49cda734719b1c5d6e79c4733ad4ca9145825d954d81

license: Apache2.0

summary: bert_base used to do classification, sequence labeling or squad tasks on various dataset.

---

## Introduction

This MindSpore Hub model uses the implementation of textcnn from the MindSpore model zoo on Gitee at model_zoo/official/nlp/textcnn.

textcnn is a audio network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/textcnn](https://gitee.com/mindspore/mindspore/blob/r1.1/model_zoo/official/nlp/textcnn/README.md).

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

model = "mindspore/ascend/1.1/textcnn_v1.1_mr"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, vocab_len=20288, word_len=51, num_classes=2, vec_length=40)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.
