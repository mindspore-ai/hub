# tsm

---

model-name: tsm

backbone-name: tsm

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: somethingsomethingv2

evaluation: top1acc58.0 | top5acc85.0

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/tsm>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/tsm_ascend_v170_somethingsomethingv2_research_cv_top1acc58.0_top5acc85.0.ckpt>
    asset-sha256: 7bbf6027e8311ec5ead1e5f98ff5acb92020b325de000dba765f058810d0e5b4

license: Apache2.0

summary: tsm is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of tsm from the MindSpore model zoo on Gitee at research/cv/tsm.

tsm is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/tsm](https://gitee.com/mindspore/models/blob/r1.7/research/cv/tsm/README_CN.md).

All parameters in the module are trainable.

## Citation

Lin, Ji, Chuang Gan and Song Han. “TSM: Temporal Shift Module for Efficient Video Understanding.” 2019 IEEE/CVF International Conference on Computer Vision (ICCV) (2019): 7082-7092.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
