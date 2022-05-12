# pnasnet

---

model-name: pnasnet

backbone-name: pnasnet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc74.06 | top5acc91.77

author: MindSpore team

update-time: 2022-05-12

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/research/cv/pnasnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/pnasnet_ascend_v160_imagenet2012_research_cv_top1acc74.06_top5acc91.77.ckpt>
    asset-sha256: 976311df78fba263aadda6e95e9e320e91779fb1740747ec1d3accfc8e26922a

license: Apache2.0

summary: pnasnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of pnasnet from the MindSpore model zoo on Gitee at research/cv/pnasnet.

pnasnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/pnasnet](https://gitee.com/mindspore/models/blob/r1.6/research/cv/pnasnet/README.md).

All parameters in the module are trainable.

## Citation

Chenxi Liu, etc. Progressive Neural Architecture Search. 2018.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
