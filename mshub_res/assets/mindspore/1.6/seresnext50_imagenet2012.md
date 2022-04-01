# SE_ResNeXt50

---

model-name: SE_ResNeXt50

backbone-name: SE_ResNeXt50

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc79 | top5acc94

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/SE_ResNeXt50>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/seresnext50_ascend_v160_imagenet2012_research_cv_top1acc79_top5acc94.ckpt>
    asset-sha256: ba9443c3aa8ca6aa55fe4cbd23afb3aedd94573c1cea8d613ffad810baed55a6

license: Apache2.0

summary: SE_ResNeXt50 is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of SE_ResNeXt50 from the MindSpore model zoo on Gitee at research/cv/SE_ResNeXt50.

SE_ResNeXt50 is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/SE_ResNeXt50](https://gitee.com/mindspore/models/blob/r1.6/research/cv/SE_ResNeXt50/README_CN.md).

All parameters in the module are trainable.

## Citation

Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Enhua Wu."Squeeze-and-Excitation Networks"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
