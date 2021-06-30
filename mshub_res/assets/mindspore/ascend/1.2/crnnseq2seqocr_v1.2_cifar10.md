# crnn_seq2seq_ocr

---

model-name: crnn_seq2seq_ocr

backbone-name: crnn_seq2seq_ocr

module-type: cv

fine-tunable: True

input-shape: [227, 227, 3]

model-version: v1.2

train-dataset: cifar10

accuracy: 96

author: MindSpore team

update-time: 2021-06-29

repo-link: <https://gitee.com/mindspore/mindspore/tree/r1.2/model_zoo/official/cv/crnn_seq2seq_ocr>

user-id: MindSpore

used-for: inference

train-backend: ascend

infer-backend: ascend

mindspore-version: v1.2

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/model_zoo/r1.2/crnnseq2seqocr_ascend_v120_cifar10_official_cv_bs32_accchar_acc96_ann_acc63/crnnseq2seqocr_ascend_v120_cifar10_official_cv_bs32_accchar_acc96_ann_acc63.ckpt>
    asset-sha256: 74f81c9c55a84ac2024d2dd21caefe4c223671ec371963c99f538d64438eefa7

license: Apache2.0

summary: crnn_seq2seq_ocr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of crnn_seq2seq_ocr from the MindSpore model zoo on Gitee at model_zoo/official/cv/crnn_seq2seq_ocr.

crnn_seq2seq_ocr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [model_zoo/official/cv/crnn_seq2seq_ocr](https://gitee.com/mindspore/mindspore/blob/r1.2/model_zoo/official/cv/crnn_seq2seq_ocr/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/ascend/1.2/crnnseq2seqocr_v1.2_cifar10"
# initialize the number of classes based on the pre-trained model
network = mshub.load(model)
network.set_train(False)

# ...
```

## Citation
