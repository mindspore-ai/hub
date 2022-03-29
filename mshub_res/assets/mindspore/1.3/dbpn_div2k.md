# DBPN

---

model-name: DBPN

backbone-name: DBPN

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: div2k

evaluation: PSNR31.93

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/DBPN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/dbpn_ascend_v130_div2k_research_cv_PSNR31.93.ckpt>
    asset-sha256: 75d74c46e4efc3a4f2e81df53a3ab8817618d8193a6032a971fe02a5e307ef77

license: Apache2.0

summary: DBPN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DBPN from the MindSpore model zoo on Gitee at research/cv/DBPN.

DBPN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DBPN](https://gitee.com/mindspore/models/blob/r1.3/research/cv/DBPN/README.md).

All parameters in the module are trainable.

## Citation

Muhammad Haris, Greg Shakhnarovich, Norimichi Ukita

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
