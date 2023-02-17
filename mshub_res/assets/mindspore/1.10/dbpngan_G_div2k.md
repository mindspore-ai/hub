# DBPN

---

model-name: DBPN

backbone-name: DBPN

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: div2k

evaluation: PSNR29.23

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/DBPN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/dbpngan_G_ascend_v1100_div2k_research_cv_PSNR29.23.ckpt>
    asset-sha256: 00ad7584fde0e5a926596ed91bebd5c13aa04086c22ac6def15a9d14dcd7eec1

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
