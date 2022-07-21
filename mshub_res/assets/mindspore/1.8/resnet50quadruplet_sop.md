# metric_learn

---

model-name: metric_learn

backbone-name: metric_learn

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: sop

evaluation: acc73.85

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/metric_learn>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/resnet50quadruplet_ascend_v180_sop_research_cv_acc73.85.ckpt>
    asset-sha256: 9e9bf1846354e74aebd8e6c4a0016d0971cda52003e341b9d3ef451783a56a6d

license: Apache2.0

summary: metric_learn is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of metric_learn from the MindSpore model zoo on Gitee at research/cv/metric_learn.

metric_learn is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/metric_learn](https://gitee.com/mindspore/models/blob/r1.8/research/cv/metric_learn/README_CN.md).

All parameters in the module are trainable.

## Citation

1. CVPR2015 F Schroff, Kalenichenko D,Philbin J."FaceNet: A Unified Embedding for Face Recognition and Clustering"
2. CVPR2017 Chen W, Chen X, Zhang J."Beyond triplet loss: A deep quadruplet network for person re-identification"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
