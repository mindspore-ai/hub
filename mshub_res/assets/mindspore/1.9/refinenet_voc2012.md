# RefineNet

---

model-name: RefineNet

backbone-name: RefineNet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: voc2012

evaluation: acc80

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/RefineNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/refinenet_ascend_v190_voc2012_research_cv_acc80.ckpt>
    asset-sha256: 9dc1819104c292fa88ad4868737fcd8c7fb7d4f7e368dc10610e71941a1571fa

license: Apache2.0

summary: RefineNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of RefineNet from the MindSpore model zoo on Gitee at research/cv/RefineNet.

RefineNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/RefineNet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/RefineNet/README.md).

All parameters in the module are trainable.

## Citation

guosheng.lin，anton.milan，et.al.RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation.arXiv:1611.06612v3 [cs.CV] 25 Nov 2016

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
