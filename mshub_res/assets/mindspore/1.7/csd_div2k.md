# csd

---

model-name: csd

backbone-name: csd

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: div2k

evaluation: panrS27.1 | psnrT27.5

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/csd>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/csd_ascend_v170_div2k_research_cv_panrS27.1_psnrT27.5.ckpt>
    asset-sha256: 48c4bbe0b55b05739aaaae7a2690a6a0f4a930c6681af9751950c490bb5eec48

license: Apache2.0

summary: csd is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of csd from the MindSpore model zoo on Gitee at research/cv/csd.

csd is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/csd](https://gitee.com/mindspore/models/blob/r1.7/research/cv/csd/README.md).

All parameters in the module are trainable.

## Citation

Towards Compact Single Image Super-Resolution via Contrastive Self-distillation in IJCAI 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
