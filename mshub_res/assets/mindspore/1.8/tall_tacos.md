# tall

---

model-name: tall

backbone-name: tall

module-type: cv

fine-tunable: True

model-version: 1.8

train-dataset: tacos

evaluation: acc49.77

author: MindSpore team

update-time: 2022-07-19

repo-link: <https://gitee.com/mindspore/models/tree/r1.8/research/cv/tall>

user-id: MindSpore

used-for: inference

mindspore-version: 1.8

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.8/tall_ascend_v180_tacos_research_cv_acc49.77.ckpt>
    asset-sha256: 8c0efe6ac77283e6836cdecd4e8a7fdef18175b16751cd19615d936178877213

license: Apache2.0

summary: tall is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of tall from the MindSpore model zoo on Gitee at research/cv/tall.

tall is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/tall](https://gitee.com/mindspore/models/blob/r1.8/research/cv/tall/README.md).

All parameters in the module are trainable.

## Citation

[TALL](https://openaccess.thecvf.com/content_iccv_2017/html/Gao_TALL_Temporal_Activity_ICCV_2017_paper.html)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
