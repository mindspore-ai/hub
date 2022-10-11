# pcb_rpp

---

model-name: pcb_rpp

backbone-name: pcb_rpp

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: market1501

evaluation: mAP80.9 | rank1acc93.2

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/pcb_rpp>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/pcbrpp_ascend_v190_market1501_research_cv_mAP80.9_rank1acc93.2.ckpt>
    asset-sha256: ce861314eb173bed1fabf421490bcad68b7e9fc0acef35aab20670ffef411e0b

license: Apache2.0

summary: pcb_rpp is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of pcb_rpp from the MindSpore model zoo on Gitee at research/cv/pcb_rpp.

pcb_rpp is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/pcb_rpp](https://gitee.com/mindspore/models/blob/r1.9/research/cv/pcb_rpp/README.md).

All parameters in the module are trainable.

## Citation

Sun Y., Zheng L., et al. “Beyond Part Models: Person Retrieval with Refined Part Pooling (and a Strong Convolutional Baseline)”. COMPUTER VISION - ECCV 2018, PT IV, (2018): 501-518.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
