# StarGAN

---

model-name: StarGAN

backbone-name: StarGAN

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: celeba

evaluation: -

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/StarGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/stargan_G_ascend_v180_celeba_research_cv.ckpt>
    asset-sha256: d3784354455957b431cd751e093c9645d27f4a225279011d69f894811aff558e

license: Apache2.0

summary: StarGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of StarGAN from the MindSpore model zoo on Gitee at research/cv/StarGAN.

StarGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/StarGAN](https://gitee.com/mindspore/models/blob/r1.8/research/cv/StarGAN/README.md).

All parameters in the module are trainable.

## Citation

StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
