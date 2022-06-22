# EGnet

---

model-name: EGnet

backbone-name: EGnet

module-type: cv

fine-tunable: True

model-version: 1.7

train-dataset: dutstr

evaluation: sodacc90.58 | ecssdacc94.18 | pascalsacc87.88 | dutomronacc77.98 | hkuis93.16

author: MindSpore team

update-time: 2022-06-22

repo-link: <https://gitee.com/mindspore/models/tree/r1.7/research/cv/EGnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.7

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.7/egnet_vgg_ascend_v170_dutstr_research_cv_sodacc90.58_ecssdacc94.18_pascalsacc87.88_dutomronacc77.98_hkuis93.16.ckpt>
    asset-sha256: be9da5a7155bb13903e17dc0ddd486f75e3c92375d2d21c6ad6769c2022cfe05

license: Apache2.0

summary: EGnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of EGnet from the MindSpore model zoo on Gitee at research/cv/EGnet.

EGnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/EGnet](https://gitee.com/mindspore/models/blob/r1.7/research/cv/EGnet/README_CN.md).

All parameters in the module are trainable.

## Citation

Zhao J X, Liu J J, Fan D P, et al. EGNet: Edge guidance network for salient object detection[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019: 8779-8788.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
