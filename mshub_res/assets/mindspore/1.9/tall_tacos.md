# tall

---

model-name: tall

backbone-name: tall

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: TACoS

evaluation: acc50.75

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/tall>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/tall_ascend_v190_tacos_research_cv_acc50.75.ckpt>
    asset-sha256: ae8abfa377159b85b3698d27aeed9e15d9dddff95dac7c575268bae9175284bc

license: Apache2.0

summary: tall is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of tall from the MindSpore model zoo on Gitee at research/cv/tall.

tall is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/tall](https://gitee.com/mindspore/models/blob/r1.9/research/cv/tall/README.md).

All parameters in the module are trainable.

## Citation

[TALL: Temporal Activity Localization via Language Query](https://openaccess.thecvf.com/content_ICCV_2017/papers/Gao_TALL_Temporal_Activity_ICCV_2017_paper.pdf)

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
