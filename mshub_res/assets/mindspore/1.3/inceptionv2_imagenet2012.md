# Inception-v2

---

model-name: Inception-v2

backbone-name: Inception-v2

module-type: cv

fine-tunable: True

model-version: 1.3

train-dataset: imagenet2012

evaluation: top1acc76.35 | top5acc92.97

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.3/research/cv/Inception-v2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.3

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.3/inceptionv2_ascend_v130_imagenet2012_research_cv_top1acc76.35_top5acc92.97.ckpt>
    asset-sha256: f7fb2c861e56154b8f1a85dd49c05b322211fc823e0e776d98ed3157a8f742f1

license: Apache2.0

summary: Inception-v2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of Inception-v2 from the MindSpore model zoo on Gitee at research/cv/Inception-v2.

Inception-v2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/Inception-v2](https://gitee.com/mindspore/models/blob/r1.3/research/cv/Inception-v2/README_CN.md).

All parameters in the module are trainable.

## Citation

Min Sun, Ali Farhadi, Steve Seitz.Ranking Domain-Specific Highlights by Analyzing Edited Videos[J].2014.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
