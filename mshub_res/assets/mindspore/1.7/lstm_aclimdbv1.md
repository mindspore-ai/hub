# lstm

---

model-name: lstm

backbone-name: lstm

module-type: nlp

fine-tunable: True

model-version: 1.7

train-dataset: aclimdbv1

evaluation: acc83.27

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/official/nlp/lstm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/lstm_ascend_v170_aclimdbv1_official_nlp_acc83.27.ckpt>
    asset-sha256: 1753803072319f6538e5850d309afcad306f15b3b0fee995ce2234f1a2bb7e7e

license: Apache2.0

summary: lstm is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of lstm from the MindSpore model zoo on Gitee at official/nlp/lstm.

lstm is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/lstm](https://gitee.com/mindspore/models/blob/r1.7/official/nlp/lstm/README.md).

All parameters in the module are trainable.

## Citation

Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts. [Learning Word Vectors for Sentiment Analysis](https://www.aclweb.org/anthology/P11-1015/). Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies. 2011

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
