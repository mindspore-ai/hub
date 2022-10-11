# lstm_crf

---

model-name: lstm_crf

backbone-name: lstm_crf

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: conll2000

evaluation: f1acc93.48

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/lstm_crf>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/lstmcrf_ascend_v190_conll2000_research_nlp_f1acc93.48.ckpt>
    asset-sha256: 81617b85c25cc8268d0b9f5da33138078d25df900f9d2f71ca0d315ea6e71914

license: Apache2.0

summary: lstm_crf is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of lstm_crf from the MindSpore model zoo on Gitee at research/nlp/lstm_crf.

lstm_crf is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/lstm_crf](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/lstm_crf/README.md).

All parameters in the module are trainable.

## Citation

[Paper](https://arxiv.org/abs/1508.01991):  Zhiheng Huang, Wei Xu, Kai Yu. [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
