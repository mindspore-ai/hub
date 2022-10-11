# FDA-BNN

---

model-name: FDA-BNN

backbone-name: FDA-BNN

module-type: cv

fine-tunable: True

model-version: 1.9

train-dataset: cifar10

evaluation: top1acc86.6 | top5acc99.5

author: MindSpore team

update-time: 2022-10-11

repo-link: <https://gitee.com/mindspore/models/tree/r1.9/research/cv/FDA-BNN>

user-id: MindSpore

used-for: inference

mindspore-version: 1.9

asset:

-
    file-format: ckpt
    asset-link: <https://download.mindspore.cn/models/r1.9/fdabnn_ascend_v190_cifar10_research_cv_top1acc86.6_top5acc99.5.ckpt>
    asset-sha256: 8c6c14514ebd75e7992400b2839b1135438736941408889698120a3e0be56101

license: Apache2.0

summary: FDA-BNN is used for cv

---

## Introduction

This MindSpore Hub model uses the implementation of FDA-BNN from the MindSpore model zoo on Gitee at research/cv/FDA-BNN.

FDA-BNN is a cv network. More details please refer to the MindSpore model zoo on Gitee at [research/cv/FDA-BNN](https://gitee.com/mindspore/models/blob/r1.9/research/cv/FDA-BNN/README.md).

All parameters in the module are trainable.

## Citation

Yixing Xu,  Kai Han, Chang Xu, Yehui Tang, Chunjing Xu, Yunhe Wang. Learning Frequency Domain Approximation for Binary Neural Networks. Accepted by NeurIPS 2021.

## Disclaimer

MindSpore ("we") do not own any ownership or intellectual property rights of the datasets, and the trained models are provided on an "as is" and "as available" basis. We make no representations or warranties of any kind of the datasets and trained models (collectively, “materials”) and will not be liable for any loss, damage, expense or cost arising from the materials. Please ensure that you have permission to use the dataset under the appropriate license for the dataset and in accordance with the terms of the relevant license agreement. The trained models provided are only for research and education purposes.

To Dataset Owners: If you do not wish to have a dataset included in MindSpore, or wish to update it in any way, we will remove or update the content at your request. Please contact us through GitHub or Gitee. Your understanding and contributions to the community are greatly appreciated.

MindSpore is available under the Apache 2.0 license, please see the LICENSE file.
