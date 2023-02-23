# APDrawingGAN

---

model-name: APDrawingGAN

backbone-name: APDrawingGAN

module-type: cv

fine-tunable: True

model-version: 1.10

train-dataset: apdrawingdb

evaluation: -

author: MindSpore team

update-time: 2023-2-17

repo-link: <https://gitee.com/mindspore/models/tree/r1.10/research/cv/APDrawingGAN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.10

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.10/apdrawinggan_Generator_ascend_v1100_apdrawingdb_research_cv.ckpt>
    asset-sha256: 1a8537d6df84e657d820facc6648e267700f6685d1e940b27035c149718ec7c5

license: Apache2.0

summary: APDrawingGAN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of APDrawingGAN from the MindSpore model zoo on Gitee at research/cv/APDrawingGAN.

APDrawingGAN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/APDrawingGAN](https://gitee.com/mindspore/models/blob/r1.10/research/cv/APDrawingGAN/README_CN.md).

All parameters in the module are trainable.

## Citation

[APDrawingGAN: Generating Artistic Portrait Drawings from Face Photos with Hierarchical GANs](https://openaccess.thecvf.com/content_CVPR_2019/papers/Yi_APDrawingGAN_Generating_Artistic_Portrait_Drawings_From_Face_Photos_With_Hierarchical_CVPR_2019_paper.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
