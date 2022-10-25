# MVD

---

model-name: MVD

backbone-name: MVD

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: sysumm01

evaluation: rank1acc56 | mAP55

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/MVD>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/mvd_allresearch_ascend_v190_sysumm01_research_cv_rank1acc56_mAP55.ckpt>
    asset-sha256: 1e6563e40ab1d7338784ed79cf1884a4b3daf52e6f927dad00c1156748636833

license: Apache2.0

summary: MVD is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of MVD from the MindSpore model zoo on Gitee at research/cv/MVD.

MVD is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/MVD](https://gitee.com/mindspore/models/blob/r1.9/research/cv/MVD/README.md).

All parameters in the module are trainable.

## Citation

[Farewell to Mutual Information: Variational Distillation for Cross-Modal Person Re-Identification](https://openaccess.thecvf.com/content/CVPR2021/papers/Tian_Farewell_to_Mutual_Information_Variational_Distillation_for_Cross-Modal_Person_Re-Identification_CVPR_2021_paper.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
