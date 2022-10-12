# Auto-DeepLab

---

model-name: Auto-DeepLab

backbone-name: Auto-DeepLab

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cityscapes

evaluation: miou78.13

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/Auto-DeepLab>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/autodeeplab_1.5M_ascend_v190_cityscapes_research_cv_miou78.13.ckpt>
    asset-sha256: d21ec854e263d46430da483f8ef41b524662f0ce4ee4dfc4dda3570444069755

license: Apache2.0

summary: Auto-DeepLab is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Auto-DeepLab from the MindSpore model zoo on Gitee at research/cv/Auto-DeepLab.

Auto-DeepLab is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Auto-DeepLab](https://gitee.com/mindspore/models/blob/r1.9/research/cv/Auto-DeepLab/README.md).

All parameters in the module are trainable.

## Citation

Chenxi Liu, Liang-Chieh Chen, Florian Schroff, Hartwig Adam, Wei Hua, Alan L. Yuille, Li Fei-Fei; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 82-92

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
