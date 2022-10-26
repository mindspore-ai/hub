# StarGAN

---

model-name: StarGAN

backbone-name: StarGAN

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: CelebA

evaluation: -

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/StarGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/stargan_Generator_ascend_v190_celeba_research_cv.ckpt>
    asset-sha256: 9ada632615378c855509f59f84252768981c243819420bf66db38c0ebea3c6e6

license: Apache2.0

summary: StarGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of StarGAN from the MindSpore model zoo on Gitee at research/cv/StarGAN.

StarGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/StarGAN](https://gitee.com/mindspore/models/blob/r1.9/research/cv/StarGAN/README.md).

All parameters in the module are trainable.

## Citation

[StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation](https://arxiv.org/pdf/1711.09020.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
