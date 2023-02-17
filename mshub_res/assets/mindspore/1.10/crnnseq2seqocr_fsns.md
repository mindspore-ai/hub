# crnn_seq2seq_ocr

---

model-name: crnn_seq2seq_ocr

backbone-name: crnn_seq2seq_ocr

module-type: cv-scene_text_recognition

fine-tunable: True

model-version: 1.10

train-dataset: FSNS

evaluation: annotationprecision84 | characterprecision97

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/official/cv/crnn_seq2seq_ocr>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/crnnseq2seqocr_ascend_v1100_fsns_official_cv_annotationprecision84_characterprecision97.ckpt>
    asset-sha256: dddac2d2b3636ce2e53e41c6996ba45e666960e5670592dabd4da260e3a7a08c

license: Apache2.0

summary: crnn_seq2seq_ocr is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of crnn_seq2seq_ocr from the MindSpore model zoo on Gitee at official/cv/crnn_seq2seq_ocr.

crnn_seq2seq_ocr is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/crnn_seq2seq_ocr](https://gitee.com/mindspore/models/blob/r1.10/official/cv/crnn_seq2seq_ocr/README.md).

All parameters in the module are trainable.

## Usage

```python
import mindspore_hub as mshub
from mindspore import context

context.set_context(mode=context.GRAPH_MODE,
                    device_target="Ascend",
                    device_id=0)

model = "mindspore/1.10/crnnseq2seqocr_fsns"
network = mshub.load(model)
network.set_train(False)

# ...
```

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
