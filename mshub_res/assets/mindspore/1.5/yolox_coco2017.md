# yolox

---

model-name: yolox

backbone-name: yolox

module-type: cv

fine-tunable: True

model-version: 1.5

train-dataset: coco2017

evaluation: map47.3

author: MindSpore team

update-time: 2022-04-24

repo-link: <https://gitee.com/mindspore/models/tree/r1.5/research/cv/yolox>

user-id: MindSpore

used-for: inference

mindspore-version: 1.5

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.5/yolox_ascend_v150_coco2017_research_cv_map47.3.ckpt>
    asset-sha256: 31ee25297c89aa6632de562c891a8fb8f85cfb52d86a2145de303452b591cdb6

license: Apache2.0

summary: yolox is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of yolox from the MindSpore model zoo on Gitee at research/cv/yolox.

yolox is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/yolox](https://gitee.com/mindspore/models/blob/r1.5/research/cv/yolox/README_CN.md).

All parameters in the module are trainable.

## Citation

YOLOX: Exceeding YOLO Series in 2021

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
