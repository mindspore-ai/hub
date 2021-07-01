# textcnn

---

model-name: textcnn

backbone-name: textcnn

module-type: nlp

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: sst2

accuracy: 81

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/nlp/textcnn>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/textcnn_ascend_v120_sst2_official_nlp_bs64_acc81/textcnn_ascend_v120_sst2_official_nlp_bs64_acc81.ckpt>
    asset-sha256: b5c4ae7633b5a599df1e9092cfd8cf832bcc9cf26e3778d9e96734e5a1380ec9

license: Apache2.0

summary: textcnn is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of textcnn from the MindSpore model zoo on Gitee at model_zoo/official/nlp/textcnn.

textcnn is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/nlp/textcnn](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/nlp/textcnn/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

vocab_length = 15463
word_length = 51
num_classes = 2
vec_length = 40

model = "mindspore/ascend/1.2/textcnn_v1.2_sst2"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model,
                     vocab_len=vocab_length,
                     word_len=word_length,
                     num_classes=num_classes,
                     vec_length=vec_length)
network.set_train(False)

# ...
```

## Citation

1. Kim Y. Convolutional neural networks for sentence classification[J]. arXiv preprint arXiv:1408.5882, 2014.
