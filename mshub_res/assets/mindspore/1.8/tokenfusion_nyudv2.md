# TokenFusion

---

model-name: TokenFusion

backbone-name: TokenFusion

module-type: cv-object_detection

fine-tunable: True

model-version: 1.8

train-dataset: NYUDv2

evaluation: acc54.8

author: MindSpore team

update-time: 2022-08-10

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/TokenFusion>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/tokenfusion_ascend_v180_nyudv2_research_cv_acc54.8.ckpt>
    asset-sha256: aca709e5907ec3fca31fc003ca6b1d1e4d073a06e2a029ec84d9c5e13921bb2b

license: Apache2.0

summary: TokenFusion is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of TokenFusion from the MindSpore model zoo on Gitee at research/cv/TokenFusion.

TokenFusion is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/TokenFusion](https://gitee.com/mindspore/models/blob/r1.8/research/cv/TokenFusion/README.md).

All parameters in the module are trainable.

## Citation

Yikai Wang, Xinghao Chen, Lele Cao, Wenbing Huang, Fuchun Sun, Yunhe Wang. Multimodal Token Fusion for Vision Transformers. In CVPR 2022.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
