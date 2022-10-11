# DRNet

---

model-name: DRNet

backbone-name: DRNet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: acc77.25

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/DRNet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/drnet_predictor_ascend_v190_imagenet2012_research_cv_acc77.25.ckpt>
    asset-sha256: e14d7ddab57a1a76c4efae2943695c75c7a7200fc9c1851acdcf9cbc9eaefdeb

license: Apache2.0

summary: DRNet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of DRNet from the MindSpore model zoo on Gitee at research/cv/DRNet.

DRNet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/DRNet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/DRNet/README.md).

All parameters in the module are trainable.

## Citation

Mingjian Zhu, Kai Han,  Enhua Wu, Qiulin Zhang, Ying Nie, Zhenzhong Lan, Yunhe Wang. Dynamic Resolution Network. NeurIPS 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
