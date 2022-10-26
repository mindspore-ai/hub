# FCANet

---

model-name: FCANet

backbone-name: FCANet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: augmentedpascal

evaluation: gracut2.38 | berkeley4.75

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/FCANet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fcanet_ascend_v190_augmentedpascal_research_cv_gracut2.38_berkeley4.75.ckpt>
    asset-sha256: fcd13f4b29e0cf3a1f5fd8deb584b44b37810019bf45e4688b29d98ab156924e

license: Apache2.0

summary: FCANet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FCANet from the MindSpore model zoo on Gitee at research/cv/FCANet.

FCANet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/FCANet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/FCANet/README_CN.md).

All parameters in the module are trainable.

## Citation

[Interactive Image Segmentation with First Click Attention](https://openaccess.thecvf.com/content_CVPR_2020/papers/Lin_Interactive_Image_Segmentation_With_First_Click_Attention_CVPR_2020_paper.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
