# lstm

---

model-name: lstm

backbone-name: lstm

module-type: nlp

fine-tunable: True

model-version: 1.5

train-dataset: aclimdbv1

evaluation: acc86.18

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/official/nlp/lstm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/lstm_ascend_v150_aclimdbv1_official_nlp_acc86.18.ckpt>
    asset-sha256: 7cc4125a91a2e792037cb17da99c2662c1b62ac9a4cc73f65fa6f43ba07e8ac6

license: Apache2.0

summary: lstm is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of lstm from the MindSpore model zoo on Gitee at official/nlp/lstm.

lstm is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [official/nlp/lstm](https://gitee.com/mindspore/models/blob/r1.5/official/nlp/lstm/README.md).

All parameters in the module are trainable.

## Citation

Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, Christopher Potts. Learning Word Vectors for Sentiment Analysis. Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies. 2011

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
