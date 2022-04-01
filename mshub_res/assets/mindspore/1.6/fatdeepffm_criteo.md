# Fat-DeepFFM

---

model-name: Fat-DeepFFM

backbone-name: Fat-DeepFFM

module-type: recommend

fine-tunable: True

model-version: 1.6

train-dataset: criteo

evaluation: acc80.91

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/recommend/Fat-DeepFFM>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/fatdeepffm_ascend_v160_criteo_research_recommend_acc80.91.ckpt>
    asset-sha256: c347768ae3632983113fdf0583aa766db4300cd9abd9653699d135bfcd8dc938

license: Apache2.0

summary: Fat-DeepFFM is used for recommend

---

## Introduction

This MindSpore Hub model uses the implementation of Fat-DeepFFM from the MindSpore model zoo on Gitee at research/recommend/Fat-DeepFFM.

Fat-DeepFFM is a recommend network. More details please refer to the MindSpore model zoo on Gitee at [research/recommend/Fat-DeepFFM](https://gitee.com/mindspore/models/blob/r1.6/research/recommend/Fat-DeepFFM/README.md).

All parameters in the module are trainable.

## Citation

Junlin Zhang , Tongwen Huang , Zhiqi Zhang FAT-DeepFFM: Field Attentive Deep Field-aware Factorization Machine

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
