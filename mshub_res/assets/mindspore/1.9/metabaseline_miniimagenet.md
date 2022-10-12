# meta-baseline

---

model-name: meta-baseline

backbone-name: meta-baseline

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: miniimagenet

evaluation: top1acc62 | top5acc78

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/meta-baseline>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/metabaseline_ascend_v190_miniimagenet_research_cv_top1acc62_top5acc78.ckpt>
    asset-sha256: 4d210e142e104ce3bd65ebb170dc04cc93f5edb0fc0ba6f3c8eb75b3b1d730fa

license: Apache2.0

summary: meta-baseline is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of meta-baseline from the MindSpore model zoo on Gitee at research/cv/meta-baseline.

meta-baseline is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/meta-baseline](https://gitee.com/mindspore/models/blob/r1.9/research/cv/meta-baseline/README.md).

All parameters in the module are trainable.

## Citation

Meta-Baseline: Exploring Simple Meta-Learning for Few-Shot Learning.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.