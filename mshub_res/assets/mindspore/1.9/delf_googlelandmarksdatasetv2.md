# delf

---

model-name: delf

backbone-name: delf

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: googlelandmarksdatasetv2

evaluation: oxford5kmAP89.74 | paris6kmAP84.37

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/delf>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/delf_ascend_v190_googlelandmarksdatasetv2_research_cv_oxford5kmAP89.74_paris6kmAP84.37.ckpt>
    asset-sha256: b6b09fde4b2db29e8be9a0f40893aa264815adda3d66c86741b92b17fb1e770c

license: Apache2.0

summary: delf is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of delf from the MindSpore model zoo on Gitee at research/cv/delf.

delf is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/delf](https://gitee.com/mindspore/models/blob/r1.9/research/cv/delf/README_CN.md).

All parameters in the module are trainable.

## Citation

Noh, H. , et al. "Large-Scale Image Retrieval with Attentive Deep Local Features." 2017 IEEE International Conference on Computer Vision (ICCV) IEEE, 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
