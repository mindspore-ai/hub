# arcface

---

model-name: arcface

backbone-name: arcface

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: ms1mv2

evaluation: lwf99.82 | cfpfp98.44 | agedb98.2 | calfw96.1 | cplfw93.1 | IJBB97.72 | IJBC98.45

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/arcface>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/arcface_ascend_v190_ms1mv2_research_cv_lwf99.82_cfpfp98.44_agedb98.2_calfw96.1_cplfw93.1_IJBB97.72_IJBC98.45.ckpt>
    asset-sha256: 495e83ab06793f26ea49f292a95e7c5aa239b6480b98a3cfdd2c867249e27630

license: Apache2.0

summary: arcface is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of arcface from the MindSpore model zoo on Gitee at research/cv/arcface.

arcface is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/arcface](https://gitee.com/mindspore/models/blob/r1.9/research/cv/arcface/README_CN.md).

All parameters in the module are trainable.

## Citation

Deng J ,  Guo J ,  Zafeiriou S . ArcFace: Additive Angular Margin Loss for Deep Face Recognition[J].  2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
