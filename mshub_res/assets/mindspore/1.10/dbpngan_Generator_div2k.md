# DBPN_GAN

---

model-name: DBPN_GAN

backbone-name: DBPN

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: DIV2K

evaluation: PSNR26.31

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/DBPN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/dbpngan_Generator_ascend_v1100_div2k_research_cv_PSNR26.31.ckpt>
    asset-sha256: c9c41fe06def3a454c60e1c2b9cf61ed614eec1e1b9eab70554d19261ee0169a

license: Apache2.0

summary: DBPN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DBPN from the MindSpore model zoo on Gitee at research/cv/DBPN.

DBPN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DBPN](https://gitee.com/mindspore/models/blob/r1.10/research/cv/DBPN/README.md).

All parameters in the module are trainable.

## Citation

[Deep Back-Projection Networks For Super-Resolution](https://arxiv.org/pdf/1803.02735.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
