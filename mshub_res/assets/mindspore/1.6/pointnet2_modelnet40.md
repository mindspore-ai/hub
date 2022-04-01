# pointnet2

---

model-name: pointnet2

backbone-name: pointnet2

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: modelnet40

evaluation: acc91.83

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/pointnet2>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/pointnet2_ascend_v160_modelnet40_research_cv_acc91.83.ckpt>
    asset-sha256: d0dfc830f9b5635e7ee0d433b29626ec765374b3f408bbe533282822e5ab8dbb

license: Apache2.0

summary: pointnet2 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of pointnet2 from the MindSpore model zoo on Gitee at research/cv/pointnet2.

pointnet2 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/pointnet2](https://gitee.com/mindspore/models/blob/r1.6/research/cv/pointnet2/README.md).

All parameters in the module are trainable.

## Citation

Qi, Charles R., et al. "Pointnet++: Deep hierarchical feature learning on point sets in a metric space." arXiv preprint arXiv:1706.02413 (2017).

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
