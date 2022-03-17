# CycleGAN

---

model-name: CycleGAN

backbone-name: CycleGAN

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: horse2zebra

evaluation: -

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/CycleGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/cyclegan_GB_ascend_v130_horse2zebra_research_cv.ckpt>
    asset-sha256: 7e674623287672c6c221f9a7914429f60c02cd510ba662de36df6ed49ac035a5

license: Apache2.0

summary: CycleGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of CycleGAN from the MindSpore model zoo on Gitee at research/cv/CycleGAN.

CycleGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/CycleGAN](https://gitee.com/mindspore/models/blob/r1.3/research/cv/CycleGAN/README.md).

All parameters in the module are trainable.

## Citation

Zhu J Y , Park T , Isola P , et al. Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks[J]. 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
