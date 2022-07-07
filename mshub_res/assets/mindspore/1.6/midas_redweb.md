# midas

---

model-name: midas

backbone-name: midas

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: redweb

evaluation: Sintel32.43 | TUM14.57 | Kitti24.78

author: MindSpore team

update-time: 2022-07-04

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/midas>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/midas_ascend_v160_redweb_research_cv_Sintel32.43_TUM14.57_Kitti24.78.ckpt>
    asset-sha256: a8e090947fb777033547ec7ba00a00d68e691f2a150fb18ca106fde133a0b363

license: Apache2.0

summary: midas is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of midas from the MindSpore model zoo on Gitee at research/cv/midas.

midas is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/midas](https://gitee.com/mindspore/models/blob/r1.6/research/cv/midas/README.md).

All parameters in the module are trainable.

## Citation

Ranftl*, Katrin Lasinger*, David Hafner, Konrad Schindler, and Vladlen Koltun.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
