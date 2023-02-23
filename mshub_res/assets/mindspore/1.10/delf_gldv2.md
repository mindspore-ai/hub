# delf

---

model-name: delf

backbone-name: delf

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: gldv2

evaluation: oxford5kmap91.85 | paris6k87.87

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/delf>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/delf_ascend_v1100_gldv2_research_cv_oxford5kmap91.85_paris6k87.87.ckpt>
    asset-sha256: e75b91b9a11d2d35ca3f5cee5199b30c08df495b4d70c48df264a04afd10eed3

license: Apache2.0

summary: delf is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of delf from the MindSpore model zoo on Gitee at research/cv/delf.

delf is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/delf](https://gitee.com/mindspore/models/blob/r1.10/research/cv/delf/README_CN.md).

All parameters in the module are trainable.

## Citation

[Large-Scale Image Retrieval with Attentive Deep Local Features](https://arxiv.org/pdf/1612.06321.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
