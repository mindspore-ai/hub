# tprr

---

model-name: tprr

backbone-name: tprr

module-type: nlp

fine-tunable: True

model-version: 1.3

train-dataset: hotpotqa

evaluation: pem91.88 | top1pem88.0 | jointf1acc71.5

author: MindSpore team

update-time: 2022-04-27

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/nlp/tprr>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/tprr_rerankdownstream_ascend_v130_hotpotqa_research_nlp_pem91.88_top1pem88.0_jointf1acc71.5.ckpt>
    asset-sha256: 181b797382d232390960a074695354e583b145b544ad9e130aee64a66cb3b3ce

license: Apache2.0

summary: tprr is used for nlp

---

## Introduction

This MindSpore Hub model uses the implementation of tprr from the MindSpore model zoo on Gitee at research/nlp/tprr.

tprr is a nlp network. More details please refer to the MindSpore model zoo on Gitee at [research/nlp/tprr](https://gitee.com/mindspore/models/blob/r1.3/research/nlp/tprr/README.md).

All parameters in the module are trainable.

## Citation

[Answer Complex Questions: Path Ranker Is All You Need](https://dl.acm.org/doi/abs/10.1145/3404835.3462942)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
