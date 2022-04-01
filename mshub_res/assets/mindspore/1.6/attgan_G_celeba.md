# AttGAN

---

model-name: AttGAN

backbone-name: AttGAN

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: celeba

evaluation: -

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/AttGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/attgan_G_ascend_v160_celeba_research_cv.ckpt>
    asset-sha256: cc3c9f53714cafa0279d3856f50d164dd8245b8a67fb0f60e72a36012fef2026

license: Apache2.0

summary: AttGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of AttGAN from the MindSpore model zoo on Gitee at research/cv/AttGAN.

AttGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/AttGAN](https://gitee.com/mindspore/models/blob/r1.6/research/cv/AttGAN/README_CN.md).

All parameters in the module are trainable.

## Citation

Zhenliang He, Wangmeng Zuo, Meina Kan, Shiguang Shan, Xilin Chen, et al. AttGAN: Facial Attribute Editing by Only Changing What You Want[C]// 2017 CVPR. IEEE

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
