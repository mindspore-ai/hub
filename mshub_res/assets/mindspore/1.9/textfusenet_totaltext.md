# textfusenet

---

model-name: textfusenet

backbone-name: textfusenet

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: TotalText

evaluation: acc82.46

author: MindSpore team

update-time: 2022-10-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/textfusenet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/textfusenet_ascend_v190_totaltext_research_cv_acc82.46.ckpt>
    asset-sha256: ec88457127fa6c8dbe39bd787b7352a51fa748f6106dee7c353d65f66005b7c1

license: Apache2.0

summary: textfusenet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of textfusenet from the MindSpore model zoo on Gitee at research/cv/textfusenet.

textfusenet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/textfusenet](https://gitee.com/mindspore/models/blob/r1.9/research/cv/textfusenet/README.md).

All parameters in the module are trainable.

## Citation

Jian Ye, Zhe Chen, Juhua Liu, Bo Du. "TextFuseNet: Scene Text Detection with Richer Fused Features"

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
