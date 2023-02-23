# seq2seq

---

model-name: seq2seq

backbone-name: seq2seq

module-type: nlp

fine-tunable: True

model-version: 1.10

train-dataset: wmt14

evaluation: BLUE12.9

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/nlp/seq2seq>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/seq2seq_ascend_v1100_wmt14_research_nlp_BLUE12.9.ckpt>
    asset-sha256: f1ea7717ccefafda74727f16b8a3f04b8011c7c298ade859884db17eeeb2897b

license: Apache2.0

summary: seq2seq is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of seq2seq from the MindSpore model zoo on Gitee at research/nlp/seq2seq.

seq2seq is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/seq2seq](https://gitee.com/mindspore/models/blob/r1.10/research/nlp/seq2seq/README_CN.md).

All parameters in the module are trainable.

## Citation

[Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
