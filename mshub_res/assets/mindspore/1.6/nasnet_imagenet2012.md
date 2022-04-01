# nasnet

---

model-name: nasnet

backbone-name: nasnet

module-type: cv

fine-tunable: True

model-version: 1.6

train-dataset: imagenet2012

evaluation: top1acc74.05 | top5acc91.59

author: MindSpore team

update-time: 2022-03-30

repo-link: <https://gitee.com/mindspore/models/tree/r1.6/official/cv/nasnet>

user-id: MindSpore

used-for: inference

mindspore-version: 1.6

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.6/nasnet_ascend_v160_imagenet2012_official_cv_top1acc74.05_top5acc91.59.ckpt>
    asset-sha256: 9f84e8d6305d05ce9bc72d62d424364b4888b217e6eb25acc0557595c9cc70c6

license: Apache2.0

summary: nasnet is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of nasnet from the MindSpore model zoo on Gitee at official/cv/nasnet.

nasnet is a cv network. More details please refer to the MindSpore model zoo on Gitee at [official/cv/nasnet](https://gitee.com/mindspore/models/blob/r1.6/official/cv/nasnet/README.md).

All parameters in the module are trainable.

## Citation

Barret Zoph, Vijay Vasudevan, Jonathon Shlens, Quoc V. Le. Learning Transferable Architectures for Scalable Image Recognition. 2017.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
