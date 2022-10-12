# wgan

---

model-name: wgan

backbone-name: wgan

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: lsunbedrooms

evaluation: -

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/wgan>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/wgan_batchnorm_G_ascend_v190_lsunbedrooms_research_cv.ckpt>
    asset-sha256: f1a6d7adb5e168d3913b6bac61dbe77c487f5d5293bca3b951a73144d3a5e4f0

license: Apache2.0

summary: wgan is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of wgan from the MindSpore model zoo on Gitee at research/cv/wgan.

wgan is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/wgan](https://gitee.com/mindspore/models/blob/r1.9/research/cv/wgan/README_CN.md).

All parameters in the module are trainable.

## Citation

Martin Arjovsky, Soumith Chintala, Léon Bottou. "Wasserstein GAN"*In International Conference on Machine Learning(ICML 2017).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
