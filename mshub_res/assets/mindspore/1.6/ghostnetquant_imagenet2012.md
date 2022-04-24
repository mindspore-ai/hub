# ghostnet_quant

---

model-name: ghostnet_quant

backbone-name: ghostnet_quant

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc82.5

author: MindSpore team

update-time: 2022-04-27

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/ghostnet_quant>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/ghostnetquant_ascend_v160_imagenet2012_research_cv_top1acc82.5.ckpt>
    asset-sha256: e10180c9cfecb35cb261bc8668f2632990630570f189b108495168d23e935922

license: Apache2.0

summary: ghostnet_quant is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of ghostnet_quant from the MindSpore model zoo on Gitee at research/cv/ghostnet_quant.

ghostnet_quant is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/ghostnet_quant](https://gitee.com/mindspore/models/blob/r1.6/research/cv/ghostnet_quant/Readme.md).

All parameters in the module are trainable.

## Citation

Kai Han, Yunhe Wang, Qi Tian, Jianyuan Guo, Chunjing Xu, Chang Xu. GhostNet: More Features from Cheap Operations. CVPR 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
