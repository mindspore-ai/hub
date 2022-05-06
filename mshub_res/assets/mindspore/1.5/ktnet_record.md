# ktnet

---

model-name: ktnet

backbone-name: ktnet

module-type: nlp

fine-tunable: True

model-version: 1.5

train-dataset: record

evaluation: f1score70.72

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/nlp/ktnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/ktnet_ascend_v150_record_research_nlp_f1score70.72.ckpt>
    asset-sha256: 336bb72ac1724bae7d32699c0f4ef6fa737e185f9ed89bdc1b3b885398206238

license: Apache2.0

summary: ktnet is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of ktnet from the MindSpore model zoo on Gitee at research/nlp/ktnet.

ktnet is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/ktnet](https://gitee.com/mindspore/models/blob/r1.5/research/nlp/ktnet/README_CN.md).

All parameters in the module are trainable.

## Citation

Yang A , Wang Q , Liu J , et al. Enhancing Pre-Trained Language Representations with Rich Knowledge for Machine Reading Comprehension[C]// Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics. 2019(https://www.aclweb.org/anthology/P19-1226/).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
