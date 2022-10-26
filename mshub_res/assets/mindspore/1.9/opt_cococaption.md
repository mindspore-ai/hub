# opt

---

model-name: opt

backbone-name: opt

module-type: mm

fine-tunable: True

model-version: 1.9

train-dataset: cococaption

evaluation: -

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/mm/opt>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/opt_ascend_v190_cococaption_research_mm.ckpt>
    asset-sha256: 6a259dc936facab67b3088f0af41608ff48f35ee7f7cb2712424b995dea0b6be

license: Apache2.0

summary: opt is used for mm

---

## Introduction

This MindSpore Hub model uses the implementation of opt from the MindSpore model zoo on Gitee at research/mm/opt.

opt is a mm network. More details please refer to the MindSpore model zoo on Gitee at [research/mm/opt](https://gitee.com/mindspore/models/blob/r1.9/research/mm/opt/README.md).

All parameters in the module are trainable.

## Citation

[OPT: Omni-Perception Pre-Trainer for Cross-Modal Understanding and Generation](https://arxiv.org/pdf/2107.00249v2.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
