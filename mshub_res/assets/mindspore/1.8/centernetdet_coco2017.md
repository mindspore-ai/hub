# centernet_det

---

model-name: centernet_det

backbone-name: centernet_det

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: coco2017

evaluation: mAP41.6 | AP50acc60.1 | AP75acc44.5

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/centernet_det>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/centernetdet_ascend_v180_coco2017_research_cv_mAP41.6_AP50acc60.1_AP75acc44.5.ckpt>
    asset-sha256: 39ccffb7eae3cbcf2821fe093e3f48c9acde272669a7d9f90a2f08964514f4fd

license: Apache2.0

summary: centernet_det is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of centernet_det from the MindSpore model zoo on Gitee at research/cv/centernet_det.

centernet_det is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/centernet_det](https://gitee.com/mindspore/models/blob/r1.8/research/cv/centernet_det/README.md).

All parameters in the module are trainable.

## Citation

Objects as Points. 2019. Xingyi Zhou(UT Austin) and Dequan Wang(UC Berkeley) and Philipp Krahenbuhl(UT Austin)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
