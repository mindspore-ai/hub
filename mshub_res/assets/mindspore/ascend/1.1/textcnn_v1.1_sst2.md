# TextCNN

---

model-name: textcnn

backbone-name: textcnn

module-type: nlp

fine-tunable: True

input-shape: [[1, 128], [1, 128], [1, 128]]

model-version: 1.1

train-dataset: sst2

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
    asset-link: <https://download.mindspore.cn/model_zoo/r1.1/textcnn_asecnd_v111_sst2_offical_nlp_bs64_acc82/textcnn_asecnd_v111_sst2_offical_nlp_bs64_acc82.ckpt>
    asset-sha256: 39e91986eb3f91c7d71f46b45250843a034a1e14385d6210ec785908349f44e0

license: Apache2.0

summary: TextCNN is an algorithm that uses convolutional neural networks to classify text.TextCNN is very suitable for the semantic analysis of short texts such as Weibo/News/E-commerce reviews and video bullet screens.

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

model = "mindspore/ascend/1.1/textcnn_v1.1_sst2"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model, vocab_len=15463, word_len=51, num_classes=2, vec_length=40)
network.set_train(False)

# Use as the same as MindSpore Model to inference.
# ...
```

## Citation

Paper: Kim Y. Convolutional neural networks for sentence classification[J]. arXiv preprint arXiv:1408.5882, 2014.
