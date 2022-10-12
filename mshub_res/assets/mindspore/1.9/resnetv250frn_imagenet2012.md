# resnetv2_50_frn

---

model-name: resnetv2_50_frn

backbone-name: resnetv2_50_frn

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: imagenet2012

evaluation: top1acc77.22 | top5acc93.27

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/resnetv2_50_frn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/resnetv250frn_ascend_v190_imagenet2012_research_cv_top1acc77.22_top5acc93.27.ckpt>
    asset-sha256: 745667f00db73227b73815bc3e35afba8d384eed5606c004fe3c15f5907f296d

license: Apache2.0

summary: resnetv2_50_frn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of resnetv2_50_frn from the MindSpore model zoo on Gitee at research/cv/resnetv2_50_frn.

resnetv2_50_frn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/resnetv2_50_frn](https://gitee.com/mindspore/models/blob/r1.9/research/cv/resnetv2_50_frn/README.md).

All parameters in the module are trainable.

## Citation

Saurabh Singh, Shankar Krishnan. Filter Response Normalization Layer: Eliminating Batch Dependence in the Training of Deep Neural Networks. 2020.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
