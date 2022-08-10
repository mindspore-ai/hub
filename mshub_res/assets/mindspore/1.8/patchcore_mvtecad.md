# patchcore

---

model-name: patchcore

backbone-name: patchcore

module-type: cv-defect_detection

fine-tunable: True

model-version: 1.8

train-dataset: MVTec AD

evaluation: meanimage-level98.28 | meanpixel-level97.72

author: MindSpore team

update-time: 2022-08-08

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/official/cv/patchcore>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/patchcore_ascend_v180_mvtecad_official_cv_meanimage-level98.28_meanpixel-level97.72.ckpt>
    asset-sha256: 1342f00c640e2309eef894789239615f36db0fa75a3e93dbb12c13330b256d31

license: Apache2.0

summary: patchcore is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of patchcore from the MindSpore model zoo on Gitee at official/cv/patchcore.

patchcore is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/patchcore](https://gitee.com/mindspore/models/blob/r1.8/official/cv/patchcore/README_CN.md).

All parameters in the module are trainable.

## Citation

Karsten Roth, Latha Pemula, Joaquin Zepeda, Bernhard Scholkopf, Thomas Brox, Peter Gehler.Towards Total Recall in Industrial Anomaly Detection.2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
