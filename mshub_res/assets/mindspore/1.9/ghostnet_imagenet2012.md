# ghostnet

---

model-name: ghostnet

backbone-name: ghostnet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: ImageNet2012

evaluation: top1acc74.19 | top5acc91.78

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/ghostnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/ghostnet_ascend_v190_imagenet2012_research_cv_top1acc74.19_top5acc91.78.ckpt>
    asset-sha256: 2c1db3f228a130e382356514215c388c2ebf758a637eee76e87e3f6562c4e663

license: Apache2.0

summary: ghostnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ghostnet from the MindSpore model zoo on Gitee at research/cv/ghostnet.

ghostnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ghostnet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/ghostnet/README_CN.md).

All parameters in the module are trainable.

## Citation

Kai Han, Yunhe Wang, Qi Tian."GhostNet: More Features From Cheap Operations".

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
