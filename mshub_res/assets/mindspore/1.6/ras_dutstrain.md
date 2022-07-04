# ras

---

model-name: ras

backbone-name: ras

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: dutstrain

evaluation: ECSSC91.7 | DUTSTest81.5 | DUTOMRON74.2 | HKUIS90.1

author: MindSpore team

update-time: 2022-07-04

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/ras>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/ras_ascend_v160_dutstrain_research_cv_ECSSC91.7_DUTSTest81.5_DUTOMRON74.2_HKUIS90.1.ckpt>
    asset-sha256: 54bd0ce2ea705da50b83807b7aaa51d956592f556180e8fada1446daa022a20f

license: Apache2.0

summary: ras is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ras from the MindSpore model zoo on Gitee at research/cv/ras.

ras is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ras](https://gitee.com/mindspore/models/blob/r1.6/research/cv/ras/README.md).

All parameters in the module are trainable.

## Citation

https://ieeexplore.ieee.org/abstract/document/8966594

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
