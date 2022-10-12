# albert

---

model-name: albert

backbone-name: albert

module-type: nlp

fine-tunable: True

model-version: 1.9

train-dataset: sst2

evaluation: acc89.11

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/nlp/albert>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/albert_ascend_v190_sst2_research_nlp_acc89.11.ckpt>
    asset-sha256: 84769afa38111286e320c55c220a0cdf3c68a4f45239576e610ac9fd195ad190

license: Apache2.0

summary: albert is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of albert from the MindSpore model zoo on Gitee at research/nlp/albert.

albert is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/albert](https://gitee.com/mindspore/models/blob/r1.9/research/nlp/albert/README.md).

All parameters in the module are trainable.

## Citation

1. Lan, Z., Chen, M., Goodman, S., Gimpel, K., Sharma, P., & Soricut, R. (2020). ALBERT: A Lite BERT for Self-supervised Learning of Language Representations. ArXiv, abs/1909.11942.
2. Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
