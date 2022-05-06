# IRN

---

model-name: IRN

backbone-name: IRN

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: div2k

evaluation: psnry34.77 | ssimy0.9285

author: MindSpore team

update-time: 2022-04-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/IRN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/irn_x4_ascend_v160_div2k_research_cv_psnry34.77_ssimy0.9285.ckpt>
    asset-sha256: 054d792d4b392cc87c045e43e29817770d52dff4b4efa0dbce6feadfb82159e0

license: Apache2.0

summary: IRN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of IRN from the MindSpore model zoo on Gitee at research/cv/IRN.

IRN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/IRN](https://gitee.com/mindspore/models/blob/r1.6/research/cv/IRN/README.md).

All parameters in the module are trainable.

## Citation

Mingqing Xiao, Shuxin Zheng, Chang Liu, Yaolong Wang, Di He, Guolin Ke, Jiang Bian, Zhouchen Lin, and Tie-Yan Liu. 2020. Invertible Image Rescaling. In European Conference on Computer Vision (ECCV).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
