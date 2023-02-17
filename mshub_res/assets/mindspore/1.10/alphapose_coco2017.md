# AlphaPose

---

model-name: AlphaPose

backbone-name: AlphaPose

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: coco2017

evaluation: acc72.28

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/AlphaPose>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/alphapose_ascend_v1100_coco2017_research_cv_acc72.28.ckpt>
    asset-sha256: cebc135d8fffbedd0d6312857257483ed0e1621f5fdd16e134ef722c19827ab4

license: Apache2.0

summary: AlphaPose is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of AlphaPose from the MindSpore model zoo on Gitee at research/cv/AlphaPose.

AlphaPose is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/AlphaPose](https://gitee.com/mindspore/models/blob/r1.10/research/cv/AlphaPose/README_CN.md).

All parameters in the module are trainable.

## Citation

[RMPE: Regional Multi-Person Pose Estimation](https://arxiv.org/pdf/1612.00137.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
