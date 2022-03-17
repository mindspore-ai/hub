# ibnnet

---

model-name: ibnnet

backbone-name: ibnnet

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: imagenet2012

evaluation: top1acc77.13 | top5acc93.59

author: MindSpore team

update-time: 2022-03-23

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/ibnnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/ibnnet_ascend_v130_imagenet2012_research_cv_top1acc77.13_top5acc93.59.ckpt>
    asset-sha256: c9ab6f1198b1b930fb2df92715134de798e103c1dd66bca06f3ee826b1a9983e

license: Apache2.0

summary: ibnnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ibnnet from the MindSpore model zoo on Gitee at research/cv/ibnnet.

ibnnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ibnnet](https://gitee.com/mindspore/models/blob/r1.3/research/cv/ibnnet/README_CN.md).

All parameters in the module are trainable.

## Citation

Pan X ,  Ping L ,  Shi J , et al. Two at Once: Enhancing Learning and Generalization Capacities via IBN-Net[C]// European Conference on Computer Vision. Springer, Cham, 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
