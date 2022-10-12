# SRGAN

---

model-name: SRGAN

backbone-name: SRGAN

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: div2k

evaluation: PSNR27.07

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/SRGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/srgan_ascend_v190_div2k_research_cv_PSNR27.07.ckpt>
    asset-sha256: 5ec7e2e43b4e9abdee38e5bdb8f3703571c884f4827629065bd504822641ecc9

license: Apache2.0

summary: SRGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of SRGAN from the MindSpore model zoo on Gitee at research/cv/SRGAN.

SRGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/SRGAN](https://gitee.com/mindspore/models/blob/r1.9/research/cv/SRGAN/README.md).

All parameters in the module are trainable.

## Citation

Christian Ledig, Lucas thesis, Ferenc Huszar, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew Aitken, Alykhan Tejani, Johannes Totz, Zehan Wang, Wenzhe Shi Twitter.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
