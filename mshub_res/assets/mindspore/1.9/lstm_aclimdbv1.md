# lstm

---

model-name: lstm

backbone-name: lstm

module-type: nlp-emotion_classification

fine-tunable: True

model-version: 1.9

train-dataset: AclImdb_v1

evaluation: acc83.0

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/nlp/lstm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/lstm_ascend_v190_aclimdbv1_official_nlp_acc83.0.ckpt>
    asset-sha256: c5006b0b41e3f766bfe0f20f65ee6f244f0fed3b8ba04ede171c77f8d1595c9a

license: Apache2.0

summary: lstm is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of lstm from the MindSpore model zoo on Gitee at official/nlp/lstm.

lstm is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/lstm](https://gitee.com/mindspore/models/blob/r1.9/official/nlp/lstm/README.md).

All parameters in the module are trainable.

## Citation

Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts. [Learning Word Vectors for Sentiment Analysis](https://www.aclweb.org/anthology/P11-1015/). Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies. 2011

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
