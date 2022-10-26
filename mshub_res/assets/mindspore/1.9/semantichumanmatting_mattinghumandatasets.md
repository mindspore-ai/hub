# semantic_human_matting

---

model-name: semantic_human_matting

backbone-name: semantic_human_matting

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: Matting Human Datasets

evaluation: avgsad5.41

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/official/cv/semantic_human_matting>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/semantichumanmatting_ascend_v190_mattinghumandatasets_official_cv_avgsad5.41.ckpt>
    asset-sha256: 76986b88a571922acb5d8dced71ac1c99e4d1ae644f8145ee7834161046a558e

license: Apache2.0

summary: semantic_human_matting is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of semantic_human_matting from the MindSpore model zoo on Gitee at official/cv/semantic_human_matting.

semantic_human_matting is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/semantic_human_matting](https://gitee.com/mindspore/models/blob/r1.9/official/cv/semantic_human_matting/README.md).

All parameters in the module are trainable.

## Citation

[Semantic Human Matting](https://arxiv.org/pdf/1809.01354.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
