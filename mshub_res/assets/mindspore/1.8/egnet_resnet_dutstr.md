# EGnet

---

model-name: EGnet

backbone-name: EGnet

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: dutstr

evaluation: sodacc87.68 | ecssdacc94.20 | pascalsacc88.55 | dutomronacc77.71 | hkuis92.80

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/EGnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/egnet_resnet_ascend_v180_dutstr_research_cv_sodacc87.68_ecssdacc94.20_pascalsacc88.55_dutomronacc77.71_hkuis92.80.ckpt>
    asset-sha256: cb7ba865a6c6fccbbe00158e79ff57c5cf9e928a7f887452ea027d536690e65d

license: Apache2.0

summary: EGnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of EGnet from the MindSpore model zoo on Gitee at research/cv/EGnet.

EGnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/EGnet](https://gitee.com/mindspore/models/blob/r1.8/research/cv/EGnet/README_CN.md).

All parameters in the module are trainable.

## Citation

Zhao J X, Liu J J, Fan D P, et al. EGNet: Edge guidance network for salient object detection[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019: 8779-8788.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
